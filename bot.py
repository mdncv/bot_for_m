from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, PollAnswer
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from asyncio import sleep
import logging

from keyboards import main_kb, quiz_kb, yn_kb, restart_kb
from auxiliary_logic.quiz_supply import get_cheer, get_quiz_options, get_quiz_stats, get_examples
from data_base.sqlite_db import (sql_start, answer_table_add_entry, answer_table_check_entry_existence,
                                 answer_table_read_entry, answer_table_delete_entry, user_table_create,
                                 user_table_check_existence, user_table_add_default_entries, user_table_get_size,
                                 user_table_add_entry, user_table_check_entry_existence, user_table_delete_entry,
                                 stats_table_check_entry_existence, stats_table_create_entry,
                                 stats_table_increase_stats, stats_table_decrease_stats)
from configuration import cfg


# log level
logging.basicConfig(level=logging.INFO)

# adding storage for finite-state machine
fsm_storage = MemoryStorage()

# bot initialization
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot, storage=fsm_storage)


# adding finite-state machines and their states
class FSMAdd(StatesGroup):
    addition_word = State()
    addition_word_description = State()


class FSMRemove(StatesGroup):
    remove_word = State()
    remove_word_yn = State()


# console message on startup
async def on_startup(_):
    print('Bot is online')
    sql_start()


# start chatting
@dp.message_handler(commands=['start', 'help'], state='*')
async def conversation_start(message: types.Message, state: FSMContext):

    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()

    if not stats_table_check_entry_existence(message.chat.id):
        stats_table_create_entry(message.chat.id)

    user_table_create(message.chat.id)
    user_table_add_default_entries(message.chat.id)
    answer_table_delete_entry(message.chat.id)

    await message.answer('*Welcome to the mdncv_bot_v2.0!*\n\n'
                         'This bot will help you learn new Turkish words in a quiz format.\n'
                         'Just add a few words along with the description, start the quiz and have fun!',
                         reply_markup=main_kb, parse_mode='Markdown')


# return to menu
@dp.message_handler(state='*', commands=['menu', 'cancel', 'finish', 'stop'])
@dp.message_handler(Text(equals=['cancel', 'finish', 'stop'], ignore_case=True), state='*')
async def go_to_menu(message: types.Message, state: FSMContext):

    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()

    answer_table_delete_entry(message.chat.id)

    await message.answer('Returning to main menu..', reply_markup=main_kb)


# quiz start
@dp.message_handler(commands=['quiz'])
async def quiz_start(message: types.Message):

    answer_table_delete_entry(message.chat.id)

    if user_table_check_existence(message.chat.id):
        n_of_words = user_table_get_size(message.chat.id)
        if n_of_words < 2:
            await message.answer('Add words to quiz.', reply_markup=quiz_kb)
        else:
            new_word, new_question, correct_option_id, new_question_options = get_quiz_options(message.chat.id)
            current_poll = await bot.send_poll(message.chat.id,
                                               question=new_question,
                                               options=new_question_options,
                                               is_anonymous=False,
                                               type='quiz',
                                               correct_option_id=correct_option_id,
                                               reply_markup=quiz_kb)
            answer_table_add_entry(message.chat.id, current_poll.poll.id, correct_option_id, new_word)
    else:
        await message.answer('Please restart the bot, some trouble happened.', reply_markup=restart_kb)


@dp.poll_answer_handler()
async def handle_poll_answer(quiz_answer: PollAnswer):

    if user_table_check_existence(quiz_answer.user.id):
        if answer_table_check_entry_existence(quiz_answer.poll_id):
            user_id, poll_id, correct_option_id, current_word = answer_table_read_entry(quiz_answer.poll_id)
            if correct_option_id == quiz_answer.option_ids[0]:
                if stats_table_check_entry_existence(quiz_answer.user.id):
                    stats_table_increase_stats(quiz_answer.user.id)
                await bot.send_message(quiz_answer.user.id, get_cheer('y'))
            else:
                if stats_table_check_entry_existence(quiz_answer.user.id):
                    stats_table_decrease_stats(quiz_answer.user.id)

                await bot.send_message(quiz_answer.user.id, get_cheer('n'))
                examples = await get_examples(current_word)
                await bot.send_message(quiz_answer.user.id, examples, parse_mode='Markdown')

            answer_table_delete_entry(quiz_answer.user.id)

            n_of_words = user_table_get_size(quiz_answer.user.id)

            if n_of_words < 2:
                await bot.send_message(quiz_answer.user.id, 'Add words to quiz.', reply_markup=quiz_kb)
            else:
                new_word, new_question, correct_option_id, new_question_options = get_quiz_options(quiz_answer.user.id)
                current_poll = await bot.send_poll(quiz_answer.user.id,
                                                   question=new_question,
                                                   options=new_question_options,
                                                   is_anonymous=False,
                                                   type='quiz',
                                                   correct_option_id=correct_option_id,
                                                   reply_markup=quiz_kb)
                answer_table_add_entry(quiz_answer.user.id, current_poll.poll.id, correct_option_id, new_word)
        else:
            await bot.send_message(quiz_answer.user.id, 'Old polls do not work and do not affect statistics.')
            # if the current quiz is considered old
            # answer_table_delete_entry(quiz_answer.user.id)
    else:
        await bot.send_message(
            quiz_answer.user.id, 'Please restart the bot, some trouble happened.', reply_markup=restart_kb)


# quiz statistics
@dp.message_handler(commands=['stats'])
async def stats_track(message: types.Message):

    answer_table_delete_entry(message.chat.id)

    if stats_table_check_entry_existence(message.chat.id):
        correct, incorrect, percentage = get_quiz_stats(message.chat.id)
        await message.answer(f'Correct answers count: {correct}\nIncorrect answers count: {incorrect}\n'
                             f'Total answers count: {correct + incorrect}\n\n'
                             f'Current correct answer percentage: {percentage}%',
                             reply_markup=quiz_kb)
    else:
        await message.answer('Please restart the bot, some trouble happened.', reply_markup=restart_kb)


# adding word section
@dp.message_handler(commands=['add'], State=None)
async def add_word(message: types.Message):

    if user_table_check_existence(message.chat.id):
        await FSMAdd.addition_word.set()
        answer_table_delete_entry(message.chat.id)
        await message.answer('What word do you want to add?', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('Please restart the bot, some trouble happened.', reply_markup=restart_kb)


@dp.message_handler(state=FSMAdd.addition_word)
async def get_word_to_add(message: types.Message, state: FSMContext):

    async with state.proxy() as word:
        word['addition_word'] = message.text

    if user_table_check_entry_existence(message.text, message.chat.id):
        await message.answer(
            f'The word \"{message.text}\" is already in dictionary.', reply_markup=quiz_kb)
        await state.finish()
    else:
        await FSMAdd.next()
        await message.answer(f'What is the \"{message.text}\" word\'s description?')


@dp.message_handler(state=FSMAdd.addition_word_description)
async def get_added_words_description(message: types.Message, state: FSMContext):

    async with state.proxy() as word:
        user_table_add_entry(word['addition_word'], message.text, message.chat.id)
        await message.answer(
            f'Word \"{word["addition_word"]}\" with description \"{message.text}\" appended.', reply_markup=quiz_kb)

    await state.finish()


# remove word section
@dp.message_handler(commands=['remove'], state=None)
async def remove_word(message: types.Message):

    if user_table_check_existence(message.chat.id):
        await FSMRemove.remove_word.set()
        answer_table_delete_entry(message.chat.id)
        await message.answer('What word do you want to remove?', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('Please restart the bot, some trouble happened.', reply_markup=restart_kb)


@dp.message_handler(state=FSMRemove.remove_word)
async def get_word_to_remove(message: types.Message, state: FSMContext):

    async with state.proxy() as word:
        word['remove_word'] = message.text

    if user_table_check_entry_existence(message.text, message.chat.id):
        await FSMRemove.next()
        await message.answer(f'The word \"{message.text}\" will be removed, are you sure?',
                             reply_markup=yn_kb)
    else:
        await message.answer(f'The word \"{message.text}\" is not in dictionary.', reply_markup=quiz_kb)
        await state.finish()


@dp.message_handler(state=FSMRemove.remove_word_yn, commands=['yes'])
async def remove_word_y(message: types.Message, state: FSMContext):

    async with state.proxy() as word:
        user_table_delete_entry(word['remove_word'], message.chat.id)
        await message.answer(
            f'The word \"{word["remove_word"]}\" had been removed.', reply_markup=quiz_kb)

    await state.finish()


@dp.message_handler(state=FSMRemove.remove_word_yn, commands=['no'])
async def remove_word_n(message: types.Message, state: FSMContext):

    async with state.proxy() as word:
        await message.answer(
            f'The word \"{word["remove_word"]}\" had not been removed.', reply_markup=quiz_kb)

    await state.finish()


# run long-polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
