import aiohttp
import asyncio
import sys
import re

from random import randrange
from bs4 import BeautifulSoup

from .supported_languages import Languages
from .cheers import Cheers
from orm.orm_interface import (dictionary_table_read_entries, user_table_read_stats,
                               dictionary_table_add_entry, cheers_table_add_entry)


async def get_quiz_options(user_id: int) -> dict:

    intermediate_crutch = await dictionary_table_read_entries(user_id)
    correct_option_id = randrange(len(intermediate_crutch))
    new_word = intermediate_crutch[correct_option_id][0]
    new_question_options = [option[1] for option in intermediate_crutch]
    new_question = 'Choose correct translation for word ' + new_word + ':'

    return dict(word=new_word, question=new_question, correct_option=correct_option_id,
                question_options=new_question_options)


async def get_quiz_stats(user_id: int) -> dict:

    correct, incorrect = await user_table_read_stats(user_id)
    percentage = round(correct * 100 / (correct + incorrect), 2) if (correct + incorrect) != 0 else 0

    return dict(cor=correct, inc=incorrect, perc=percentage)


def normalize_word(phrase: str) -> str:

    processed_phrase = phrase.translate(str.maketrans('', '', '!\"#×÷€£¥$%&\'()*+,./:;<=>?@[\]^_`{|}~1234567890'))

    pattern1 = re.compile(r'-{2,}')
    processed_phrase = pattern1.sub('-', processed_phrase)

    pattern2 = re.compile(r'[\n ]+')
    processed_phrase = ' '.join(pattern2.split(processed_phrase.lower()))

    return '' + (processed_phrase[:50] if len(processed_phrase) > 50 else processed_phrase)


def validate_language(lang: str) -> int:
    return Languages.MULTITRAN.get(lang, 0)


async def get_page_answer(word: str, learning_l: int = 32, native_l: int = 1) -> str:

    base_url = 'https://www.multitran.com/m.exe'
    params = dict(a=3, l1=learning_l, l2=native_l, s=word)
    answer = ''

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=base_url, params=params) as resp:
                status = resp.status
                if 200 <= status < 300:
                    answer = await resp.text()
                else:
                    print(f'INFO:aiohttp:Server returned {status} status.', file=sys.stderr)
    except asyncio.TimeoutError:
        print('INFO:aiohttp:Timeout occurred.', file=sys.stderr)
    except aiohttp.ClientError:
        print('INFO:aiohttp:Client error occurred.', file=sys.stderr)

    return answer


def parse_examples(text: str) -> list:

    examples = []
    table = BeautifulSoup(text, 'lxml').find('table', {'id': 'phrasetable'})
    rows = table.find_all('tr') if table else []
    del table
    rows_count = len(rows)

    for row in rows[1:(4 if rows_count > 3 else rows_count + 1)]:
        cols = row.find_all('td')
        examples.append([element.text.strip() for element in (cols[1:3] if len(cols) >= 3 else [])])

    return examples


def normalize_examples(examples: list) -> str:
    return '' + '\n\n~ ~ ~ ~ ~ ~\n\n'.join('\n\n_Translates as follows:_\n\n'.join(example) for example in examples)


async def get_examples(word: str, learning_lang: int = 32, native_lang: int = 1) -> str:

    final_string = normalize_examples(parse_examples(await get_page_answer(word, learning_lang, native_lang)))

    if final_string:
        return f'*Here are some examples with the word {word}:*\n\n' + final_string

    return f'Unfortunately can\'t find any examples with the word {word}.'


async def user_table_add_default_entries(user_id: int, learning_lang: int = 32, native_lang: int = 1) -> None:

    if native_lang != 1:
        intermediate_crutch = (('one', 'two', 'three', 'there'), ('1', '2', '3', '->'))
    else:
        intermediate_crutch = (('1', '2', '3', '->'), ('one', 'two', 'three', 'there'))

    learning_sample = Languages.DEFAULT_OPTIONS.get(learning_lang, intermediate_crutch[0])
    native_sample = Languages.DEFAULT_OPTIONS.get(native_lang, intermediate_crutch[1])

    for word, description in zip(learning_sample, native_sample):
        await dictionary_table_add_entry(word.capitalize(), description.capitalize(), user_id)


async def cheers_table_add_default_entries() -> None:

    for cheer, not_cheer in Cheers.CHEERS.items():
        await cheers_table_add_entry(cheer, not_cheer)


def main():
    pass


if __name__ == '__main__':
    main()
