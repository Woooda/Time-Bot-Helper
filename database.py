# database.py
import sqlite3

def create_connection(db_file):
    """ Создание соединения с БД """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """ Создание таблицы """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        task TEXT NOT NULL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_task(conn, task):
    """ Вставка задачи в таблицу """
    sql = ''' INSERT INTO tasks(date,task)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def display_days():
    """ Вывод всех записей из таблицы """
    conn = create_connection("tasks.db")
    cur = conn.cursor()
    cur.execute("SELECT date, COUNT(*) FROM tasks GROUP BY date")
    rows = cur.fetchall()
    for row in rows:
        print(f"[{row[0]}] {row[1]} задач")

if __name__ == '__main__':
    conn = create_connection("tasks.db")
    if conn is not None:
        create_table(conn)
    else:
        print("Ошибка! Невозможно создать соединение с БД.")
    conn.close()
