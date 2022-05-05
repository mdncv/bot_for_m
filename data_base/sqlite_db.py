import sqlite3 as sq


# on startup
def sql_start():

    global base, cur

    base = sq.connect('my_quizz.db')
    cur = base.cursor()

    if base:
        print('Database connected')
    base.execute(
        'CREATE TABLE IF NOT EXISTS answer(user_id INTEGER, poll_id INTEGER, correct_answer_id INTEGER, word TEXT)')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS stat_table(user_id INTEGER PRIMARY KEY, correct INTEGER, incorrect INTEGER)')
    base.commit()


# working with answer table
def answer_table_add_entry(user_id, poll_id, correct_option_id: int, word: str):
    cur.execute('INSERT INTO answer VALUES (?, ?, ?, ?)', (user_id, poll_id, correct_option_id, word))
    base.commit()


def answer_table_check_entry_existence(poll_id: int):
    return cur.execute('SELECT EXISTS(SELECT 1 FROM answer WHERE poll_id = ? LIMIT 1)', (poll_id,)).fetchone()[0] == 1


def answer_table_read_entry(poll_id: int):
    return cur.execute('SELECT * FROM answer WHERE poll_id = ? LIMIT 1', (poll_id,)).fetchone()


def answer_table_delete_entry(user_id: int):
    cur.execute('DELETE FROM answer WHERE user_id = ?', (user_id,))
    base.commit()


# working with user's question table
def user_table_create(user_id: int):
    table_name = 'table_' + str(user_id)
    base.execute(f'CREATE TABLE IF NOT EXISTS {table_name} (word TEXT PRIMARY KEY, description TEXT)')
    base.commit()


def user_table_check_existence(user_id: int):
    table_name = 'table_' + str(user_id)
    return cur.execute('SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type = "table" AND name = ? LIMIT 1)',
                       (table_name,)).fetchone()[0] == 1


def user_table_add_default_entries(user_id: int):
    table_name = 'table_' + str(user_id)
    if cur.execute(f'SELECT COUNT(*) FROM {table_name}').fetchone()[0] == 0:
        cur.execute(f'INSERT INTO {table_name} VALUES ("bir", "one"), ("iki", "two"), ("üç", "three"),'
                    f'("orada", "there")')
        base.commit()


def user_table_get_size(user_id: int):
    table_name = 'table_' + str(user_id)
    return cur.execute(f'SELECT COUNT(*) FROM {table_name}').fetchone()[0]


def user_table_read_entries(user_id: int):
    table_name = 'table_' + str(user_id)
    return cur.execute(f'SELECT * FROM {table_name} ORDER BY RANDOM() LIMIT 4').fetchall()


def user_table_add_entry(word, description: str, user_id: int):
    table_name = 'table_' + str(user_id)
    cur.execute(f'INSERT INTO {table_name} VALUES (?, ?)', (word, description))
    base.commit()


def user_table_check_entry_existence(word: str, user_id: int):
    table_name = 'table_' + str(user_id)
    return cur.execute(f'SELECT EXISTS(SELECT 1 FROM {table_name} WHERE LOWER(word) = LOWER(?))',
                       (word,)).fetchone()[0] == 1


def user_table_delete_entry(word_to_remove: str, user_id: int):
    table_name = 'table_' + str(user_id)
    cur.execute(f'DELETE FROM {table_name} WHERE LOWER(word) = LOWER(?)', (word_to_remove,))
    base.commit()


# working with stats_table
def stats_table_check_entry_existence(user_id: int):
    return cur.execute('SELECT EXISTS(SELECT 1 FROM stat_table WHERE user_id = ?)', (user_id,)).fetchone()[0] == 1


def stats_table_create_entry(user_id: int):
    cur.execute('INSERT INTO stat_table VALUES (?, 0, 0)', (user_id,))
    base.commit()


def stats_table_increase_stats(user_id: int):
    cur.execute('UPDATE stat_table SET correct = correct + 1 WHERE user_id = ?', (user_id,))
    base.commit()


def stats_table_decrease_stats(user_id: int):
    cur.execute('UPDATE stat_table SET incorrect = incorrect + 1 WHERE user_id = ?', (user_id,))
    base.commit()


def stats_table_read_stats(user_id: int):
    return cur.execute('SELECT correct, incorrect FROM stat_table WHERE user_id = ? LIMIT 1', (user_id,)).fetchone()


if __name__ == '__main__':
    pass
