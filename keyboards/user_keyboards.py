from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

m_b1 = KeyboardButton('/quiz')
m_b2 = KeyboardButton('/add')
m_b3 = KeyboardButton('/remove')
m_b4 = KeyboardButton('/stats')

q_b1 = KeyboardButton('/menu')

yn_b1 = KeyboardButton('/yes')
yn_b2 = KeyboardButton('/no')

r_b1 = KeyboardButton('/start')

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
quiz_kb = ReplyKeyboardMarkup(resize_keyboard=True)
yn_kb = ReplyKeyboardMarkup(resize_keyboard=True)
restart_kb = ReplyKeyboardMarkup(resize_keyboard=True)

main_kb.add(m_b1).insert(m_b4).add(m_b2).insert(m_b3)
quiz_kb.add(q_b1)
yn_kb.add(yn_b1).insert(yn_b2)
restart_kb.add(r_b1)
