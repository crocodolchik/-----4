import logging

def read_numbers(file_path):
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                num = float(line)
                numbers.append(num)
            except ValueError:
                logging.error(f"Ошибка: '{line}' не является числом")
                raise ValueError(f"В файле найдено не число: {line}")
    return numbers

def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измер пуст")