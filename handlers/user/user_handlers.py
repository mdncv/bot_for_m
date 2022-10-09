from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, PollAnswer

from keyboards import YKB
from auxiliary_logic import (get_quiz_options, get_quiz_stats, get_examples, user_table_add_default_entries,
                             normalize_word, validate_language)
from orm.orm_interface import *
from bot import TelegramBot


# adding finite-state machines and their states
class FSMStart(StatesGroup):
    start_learning_lang = State()
    start_native_lang = State()
    start_remove_words = State()
    start_remove_words_sure = State()


class FSMAdd(StatesGroup):
    addition_word = State()
    addition_word_description = State()


class FSMRemove(StatesGroup):
    remove_word = State()
    remove_word_yn = State()


# start chatting
async def conversation_start(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()

    await user_table_create_entry(message.chat.id)
    await user_table_close_poll(message.chat.id)

    await message.answer('*Welcome to the mdncv_bot_v1.0.1!*\n\n'
                         'This bot will help you learn new words in a quiz format.\n'
                         'Just add a few words along with the description, start the quiz and have fun!\n\n'
                         '_If you ever need to reset your language settings, type /start again._',
                         reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')

    await FSMStart.start_learning_lang.set()
    await message.answer('Please enter the name or code of the language you are about to learn:',
                         reply_markup=ReplyKeyboardRemove())


async def get_learning_lang(message: types.Message, state: FSMContext) -> None:

    lang = normalize_word(message.text)
    lang_num = validate_language(lang)

    if not lang_num:
        await message.answer(f'{lang.capitalize()} is not supported, default language is set _(Turkish)_.',
                             reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')
        lang_num = 32

    async with state.proxy() as langs:
        langs['learning'] = lang_num

    await FSMStart.next()
    await message.answer('Please enter the name or code of your native language:\n\n'
                         '_(Or the one in which you would like to receive examples)_',
                         reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')


async def get_native_lang(message: types.Message, state: FSMContext) -> None:

    lang = normalize_word(message.text)
    lang_num = validate_language(lang)

    async with state.proxy() as langs:

        if not lang_num and langs['learning'] != 1:
            await message.answer(f'{lang.capitalize()} is not supported.\n\nDefault language is set _(English)_.',
                                 reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')
            lang_num = 1
        elif not lang_num:
            await message.answer(f'{lang.capitalize()} is not supported.\n\nDefault language is set _(Russian)_.',
                                 reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')
            lang_num = 2
        elif langs['learning'] == lang_num and langs['learning'] != 1:
            await message.answer('The target language and native language do not have to match.\n\n'
                                 'Default language is set _(English)_.',
                                 reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')
            lang_num = 1
        elif langs['learning'] == lang_num:
            await message.answer('The target language and native language do not have to match.\n\n'
                                 'Default language is set _(Russian)_.',
                                 reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')
            lang_num = 2

        await user_table_update_languages(message.chat.id, langs['learning'], lang_num)

        if await dictionary_table_get_size(message.chat.id) == 0:
            await user_table_add_default_entries(message.chat.id, langs['learning'], lang_num)
            await message.answer('Setup complete, have fun!', reply_markup=YKB.main_kb)
            await state.finish()
            return

        langs['native'] = lang_num

        await FSMStart.next()
        await message.answer('Do you want to clear your words base?', reply_markup=YKB.yn_kb)


async def delete_words_1y(message: types.Message, state: FSMContext) -> None:

    await FSMStart.next()
    await message.answer('Are you sure?', reply_markup=YKB.yn_kb)


async def delete_words_n(message: types.Message, state: FSMContext) -> None:

    async with state.proxy() as langs:
        if await dictionary_table_get_size(message.chat.id) == 0:
            await user_table_add_default_entries(message.chat.id, langs['learning'], langs['native'])

    await state.finish()
    await message.answer('Setup complete, have fun!', reply_markup=YKB.main_kb)


async def delete_words_2y(message: types.Message, state: FSMContext) -> None:

    async with state.proxy() as langs:
        await dictionary_table_delete_user_entries(message.chat.id)
        await user_table_add_default_entries(message.chat.id, langs['learning'], langs['native'])
        await state.finish()
        await message.answer('Setup complete, have fun!', reply_markup=YKB.main_kb)


# return to menu
async def go_to_menu(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()

    await user_table_close_poll(message.chat.id)
    await message.answer('_Returning to main menu.._', reply_markup=YKB.main_kb, parse_mode='Markdown')


# quiz start
async def quiz_start(message: types.Message) -> None:

    await user_table_close_poll(message.chat.id)

    if not await user_table_check_entry(message.chat.id):
        await message.answer('Please restart the bot, some trouble happened.',
                             reply_markup=YKB.restart_kb)
        return

    if await dictionary_table_get_size(message.chat.id) < 2:
        await message.answer('Please add words to quiz.', reply_markup=YKB.go_to_menu_kb)
        return

    gqo = await get_quiz_options(message.chat.id)

    current_poll = await TelegramBot.bot.send_poll(message.chat.id, question=gqo['question'],
                                                   options=gqo['question_options'], is_anonymous=False, type='quiz',
                                                   correct_option_id=gqo['correct_option'],
                                                   reply_markup=YKB.go_to_menu_kb)

    await user_table_add_poll(message.chat.id, current_poll.poll.id, gqo['correct_option'], gqo['word'])


async def handle_poll_answer(quiz_answer: PollAnswer) -> None:

    if not await user_table_check_entry(quiz_answer.user.id):
        await TelegramBot.bot.send_message(quiz_answer.user.id, 'Please restart the bot, some trouble happened.',
                                           reply_markup=YKB.restart_kb)
        return

    if not await user_table_check_poll_existence(quiz_answer.poll_id):
        await TelegramBot.bot.send_message(quiz_answer.user.id, '_Old polls do not work and do not affect statistics._',
                                           parse_mode='Markdown')
        # if the current quiz is considered old
        # user_table_close_poll(quiz_answer.user.id)
        return

    atre = await user_table_read_entry(quiz_answer.poll_id)

    if atre['correct_option'] == quiz_answer.option_ids[0]:
        await user_table_increase_stats(quiz_answer.user.id)
        await TelegramBot.bot.send_message(quiz_answer.user.id, await cheers_table_get_entry(True))
    else:
        await user_table_decrease_stats(quiz_answer.user.id)
        await TelegramBot.bot.send_message(quiz_answer.user.id, await cheers_table_get_entry(False))
        examples = await get_examples(atre['word'], atre['learning_lang'], atre['native_lang'])
        await TelegramBot.bot.send_message(quiz_answer.user.id, examples, parse_mode='Markdown')

    await user_table_close_poll(quiz_answer.user.id)

    if await dictionary_table_get_size(quiz_answer.user.id) < 2:
        await TelegramBot.bot.send_message(quiz_answer.user.id, 'Please add words to quiz.',
                                           reply_markup=YKB.go_to_menu_kb)
        return

    gqo = await get_quiz_options(quiz_answer.user.id)

    current_poll = await TelegramBot.bot.send_poll(quiz_answer.user.id, question=gqo['question'],
                                                   options=gqo['question_options'], is_anonymous=False, type='quiz',
                                                   correct_option_id=gqo['correct_option'],
                                                   reply_markup=YKB.go_to_menu_kb)

    await user_table_add_poll(quiz_answer.user.id, current_poll.poll.id, gqo['correct_option'], gqo['word'])


# quiz statistics
async def stats_track(message: types.Message) -> None:

    await user_table_close_poll(message.chat.id)

    if not await user_table_check_entry(message.chat.id):
        await message.answer('Please restart the bot, some trouble happened.', reply_markup=YKB.restart_kb)
        return

    gqs = await get_quiz_stats(message.chat.id)

    await message.answer(f'_Correct answers count:_ {gqs["cor"]}\n_Incorrect answers count:_ {gqs["inc"]}\n'
                         f'_Total answers count:_ {gqs["cor"] + gqs["inc"]}\n\n'
                         f'*Current correct answer percentage:* {gqs["perc"]}%',
                         reply_markup=YKB.go_to_menu_kb, parse_mode='Markdown')


# adding word section
async def add_word(message: types.Message) -> None:

    await FSMAdd.addition_word.set()
    await user_table_close_poll(message.chat.id)
    await message.answer('What word do you want to add?\n\n_(The maximum word length is 50 characters)_',
                         reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')


async def get_word_to_add(message: types.Message, state: FSMContext) -> None:

    normalized_word = normalize_word(message.text).capitalize()

    async with state.proxy() as word:
        word['addition_word'] = normalized_word

    if await dictionary_table_check_entry_existence(normalized_word, message.chat.id):
        await message.answer(f'The word *\"{normalized_word}\"* is already in dictionary.',
                             reply_markup=YKB.go_to_menu_kb, parse_mode='Markdown')
        await state.finish()
    else:
        await FSMAdd.next()
        await message.answer(f'What is the *\"{normalized_word}\"* word\'s description?\n\n'
                             f'_(The maximum description length is 50 characters)_',
                             reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')


async def get_added_words_description(message: types.Message, state: FSMContext) -> None:

    normalized_description = normalize_word(message.text).capitalize()

    async with state.proxy() as word:
        await dictionary_table_add_entry(word['addition_word'], normalized_description, message.chat.id)
        await message.answer(
            f'Word *\"{word["addition_word"]}\"* with description *\"{normalized_description}\"* appended.',
            reply_markup=YKB.go_to_menu_kb, parse_mode='Markdown')

    await state.finish()


# remove word section
async def remove_word(message: types.Message) -> None:

    await FSMRemove.remove_word.set()
    await user_table_close_poll(message.chat.id)
    await message.answer('What word do you want to remove?', reply_markup=ReplyKeyboardRemove())


async def get_word_to_remove(message: types.Message, state: FSMContext) -> None:

    normalized_word = normalize_word(message.text).capitalize()

    async with state.proxy() as word:
        word['remove_word'] = normalized_word

    if await dictionary_table_check_entry_existence(normalized_word, message.chat.id):
        await FSMRemove.next()
        await message.answer(f'The word *\"{normalized_word}\"* will be removed, are you sure?',
                             reply_markup=YKB.yn_kb, parse_mode='Markdown')
    else:
        await message.answer(f'The word *\"{normalized_word}\"* is not in dictionary.',
                             reply_markup=YKB.go_to_menu_kb, parse_mode='Markdown')
        await state.finish()


async def remove_word_y(message: types.Message, state: FSMContext) -> None:

    async with state.proxy() as word:
        await dictionary_table_delete_entry(word['remove_word'], message.chat.id)
        await message.answer(f'The word *\"{word["remove_word"]}\"* had been removed.',
                             reply_markup=YKB.go_to_menu_kb, parse_mode='Markdown')

    await state.finish()


async def remove_word_n(message: types.Message, state: FSMContext) -> None:

    async with state.proxy() as word:
        await message.answer(f'The word *\"{word["remove_word"]}\"* had not been removed.',
                             reply_markup=YKB.go_to_menu_kb, parse_mode='Markdown')

    await state.finish()


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(conversation_start, commands=['start', 'help'], state='*')
    dp.register_message_handler(get_learning_lang, state=FSMStart.start_learning_lang)
    dp.register_message_handler(get_native_lang, state=FSMStart.start_native_lang)
    dp.register_message_handler(delete_words_1y, state=FSMStart.start_remove_words, commands=['yes'])
    dp.register_message_handler(delete_words_n, state=FSMStart.start_remove_words, commands=['no'])
    dp.register_message_handler(delete_words_2y, state=FSMStart.start_remove_words_sure, commands=['yes'])
    dp.register_message_handler(delete_words_n, state=FSMStart.start_remove_words_sure, commands=['no'])
    dp.register_message_handler(go_to_menu, state='*', commands=['menu', 'cancel', 'finish', 'stop'])
    dp.register_message_handler(go_to_menu, Text(equals=['cancel', 'finish', 'stop'], ignore_case=True), state='*')
    dp.register_message_handler(quiz_start, commands=['quiz'])
    dp.register_poll_answer_handler(handle_poll_answer)
    dp.register_message_handler(stats_track, commands=['stats'])
    dp.register_message_handler(add_word, commands=['add'], State=None)
    dp.register_message_handler(get_word_to_add, state=FSMAdd.addition_word)
    dp.register_message_handler(get_added_words_description, state=FSMAdd.addition_word_description)
    dp.register_message_handler(remove_word, commands=['remove'], state=None)
    dp.register_message_handler(get_word_to_remove, state=FSMRemove.remove_word)
    dp.register_message_handler(remove_word_y, state=FSMRemove.remove_word_yn, commands=['yes'])
    dp.register_message_handler(remove_word_n, state=FSMRemove.remove_word_yn, commands=['no'])
