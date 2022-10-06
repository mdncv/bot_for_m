from typing import Final

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class YKB:

    m_b1: Final = KeyboardButton('/quiz')
    m_b2: Final = KeyboardButton('/add')
    m_b3: Final = KeyboardButton('/remove')
    m_b4: Final = KeyboardButton('/stats')

    q_b1: Final = KeyboardButton('/menu')

    yn_b1: Final = KeyboardButton('/yes')
    yn_b2: Final = KeyboardButton('/no')

    r_b1: Final = KeyboardButton('/start')

    main_kb: Final = ReplyKeyboardMarkup(resize_keyboard=True)
    quiz_kb: Final = ReplyKeyboardMarkup(resize_keyboard=True)
    yn_kb: Final = ReplyKeyboardMarkup(resize_keyboard=True)
    restart_kb: Final = ReplyKeyboardMarkup(resize_keyboard=True)

    main_kb.add(m_b1).insert(m_b4).add(m_b2).insert(m_b3)
    quiz_kb.add(q_b1)
    yn_kb.add(yn_b1).insert(yn_b2)
    restart_kb.add(r_b1)
