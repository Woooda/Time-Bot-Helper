# time_bot_helper.py
import datetime
import database
import helper_functions as helpers

def plan_day(date):
    conn = database.create_connection("tasks.db")  # Создаем соединение с базой данных
    try:
        start_time = helpers.get_valid_time("С какого времени вы начинаете задания? (HH:MM) ")
        end_time = helpers.get_valid_time("Во сколько вы закончите план? (HH:MM) ")

        tasks = []
        complexities = []
        end_planning = False

        while not end_planning:
            task = input("Введите задачу: ")
            complexity = helpers.get_valid_complexity("Введите сложность/важность дела (0-10): ")
            tasks.append(task)
            complexities.append(complexity)
            end_planning = helpers.get_yes_no("Хотите вы закончить план? (да/нет): ")

        break_time = int(input("Какие перерывы в минутах? "))

        planned_tasks = helpers.plan_tasks(tasks, complexities, start_time, end_time, break_time)

        helpers.display_schedule(date, planned_tasks)

        database.insert_task(conn, date, planned_tasks)  # Передаем объект соединения в функцию вставки
    finally:
        if conn:
            conn.close()  # Закрываем соединение с базой данных

def view_day():
    date = input("Введите дату для просмотра (ГГГГ-ММ-ДД): ")
    tasks = database.get_tasks_for_day(date)
    if tasks:
        print(f"План на {date}:")
        helpers.display_schedule(date, tasks)
    else:
        print("На эту дату планов нет.")

def main():
    while True:
        print("Time Bot Helper")
        print("[1] Планировать день")
        print("[2] Просмотреть план на день")
        print("[3] Просмотреть хранилище дней")
        print("[4] Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            date = input("Введите дату планирования (ГГГГ-ММ-ДД): ")
            plan_day(date)
        elif choice == '2':
            view_day()
        elif choice == '3':
            database.display_days()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()

