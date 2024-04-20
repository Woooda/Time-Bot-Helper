# helper_functions.py
import datetime

def get_valid_time(prompt):
    """ Получение корректного времени от пользователя """
    while True:
        try:
            time_str = input(prompt)
            time_obj = datetime.datetime.strptime(time_str, '%H:%M')
            return time_obj
        except ValueError:
            print("Неверный формат времени. Пожалуйста, введите время в формате HH:MM.")

def get_valid_complexity(prompt):
    """ Получение корректной сложности от пользователя """
    while True:
        try:
            complexity = int(input(prompt))
            if 0 <= complexity <= 10:
                return complexity
            else:
                print("Сложность должна быть в диапазоне от 0 до 10.")
        except ValueError:
            print("Неверный формат сложности. Пожалуйста, введите число от 0 до 10.")

def get_yes_no(prompt):
    """ Получение ответа 'да' или 'нет' от пользователя """
    while True:
        response = input(prompt).strip().lower()
        if response == 'да' or response == 'нет':
            return response == 'да'
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

def plan_tasks(tasks, complexities, start_time, end_time, break_time):
    """ Планирование задач по времени согласно алгоритму """
    planned_tasks = []
    total_time = (end_time - start_time).total_seconds() / 60  # в минутах
    time_per_task = total_time / len(tasks)

    sorted_tasks = sorted(zip(tasks, complexities), key=lambda x: x[1], reverse=True)
    for i, (task, _) in enumerate(sorted_tasks):
        start = start_time + datetime.timedelta(minutes=i * time_per_task + i * break_time)
        end = start + datetime.timedelta(minutes=time_per_task)
        planned_tasks.append((start.strftime('%H:%M'), end.strftime('%H:%M'), task))
    return planned_tasks

def display_schedule(date, planned_tasks):
    """ Вывод планирования """
    print(f"Планирование на {date}:")
    for start, end, task in planned_tasks:
        print(f"[{start} - {end}] {task}")

if __name__ == "__main__":
    pass  # Можно добавить дополнительные тесты или демонстрации, если требуется
