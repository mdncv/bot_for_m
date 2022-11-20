from tortoise.contrib.postgres.functions import Random

from orm.models import UserTable, DictTable, Cheers
from auxiliary_logic import get_cheers, get_default_options


# Working with user table

async def user_table_create_entry(user_id: int) -> None:
    defaults = dict(poll_id=0, correct_option_id=0, word='', correct_answers=0, incorrect_answers=0, learning_lang=32,
                    native_lang=1)
    await UserTable.update_or_create(user_id=user_id, defaults=defaults)


async def user_table_read_entry(user_id: int) -> dict:
    user = await UserTable.get_or_none(user_id=user_id)
    if user is not None:
        return dict(user)
    return {}


async def user_table_update_languages(user_id: int, learning_lang: int, native_lang: int) -> None:
    await UserTable.filter(user_id=user_id).update(learning_lang=learning_lang, native_lang=native_lang)


async def user_table_rewrite_entry(user_id: int, poll_id: int, correct_option_id: int, word: str, correct_answers: int,
                                   incorrect_answers: int, *args, **kwargs) -> None:
    await UserTable.filter(user_id=user_id).update(poll_id=poll_id, correct_option_id=correct_option_id, word=word,
                                                   correct_answers=correct_answers, incorrect_answers=incorrect_answers)


async def user_table_close_poll(user_id: int) -> None:
    await UserTable.filter(user_id=user_id).update(poll_id=0, correct_option_id=0, word='')


# Working with dictionary table

async def dictionary_table_add_entry(word: str, description: str, user_id: int) -> None:
    await DictTable.create(user_id=user_id, word=word, description=description)


async def dictionary_table_add_default_entries(user_id: int, learning_lang: int = 32, native_lang: int = 1) -> None:
    for word, description in get_default_options(learning_lang, native_lang):
        await dictionary_table_add_entry(word.capitalize(), description.capitalize(), user_id)


async def dictionary_table_check_entry_existence(word: str, user_id: int) -> bool:
    return await DictTable.filter(word=word, user_id=user_id).exists()


async def dictionary_table_read_entries(user_id: int) -> list:
    words = await DictTable.filter(user_id=user_id).annotate(order=Random()).order_by('order').limit(4)
    return [(word.word, word.description) for word in words]


async def dictionary_table_delete_entry(word_to_remove: str, user_id: int) -> None:
    await DictTable.filter(word=word_to_remove, user_id=user_id).delete()


async def dictionary_table_delete_user_entries(user_id: int) -> None:
    await DictTable.filter(user_id=user_id).delete()


# Working with cheers table

async def cheers_table_add_entry(cheer: str, not_cheer: str) -> None:
    await Cheers.get_or_create(cheer=cheer, not_cheer=not_cheer)


async def cheers_table_add_default_entries() -> None:
    for cheer, not_cheer in get_cheers().items():
        await cheers_table_add_entry(cheer, not_cheer)


async def cheers_table_get_entry(regime: bool) -> str:
    cheer = await Cheers.annotate(order=Random()).order_by('order').first()
    return cheer.cheer if regime else cheer.not_cheer
