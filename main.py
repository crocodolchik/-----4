# import logging
# from pathlib import Path
# from utils.reader import read_numbers, validate_numbers
# from utils.statistics import calculate_average, find_min, find_max

# def main():

#     file_path = Path("data") / "measurements.txt"
#     print(f"Текущий каталог: {Path.cwd()}")
    
#     if file_path.exists():
#         print(f"Файл найден: {file_path}")
#     else:
#         print(f"Файл НЕ найден: {file_path}")
#         return
        
#     log_dir = Path("logs")
#     log_dir.mkdir(exist_ok=True)
#     print(f"Папка для логов готова: {log_dir}")

#     numbers = read_numbers(file_path)
#     validate_numbers(numbers)
    
#     min_m = find_min(numbers)
#     max_m = find_max(numbers)
#     avg_m = calculate_average(numbers)
    
#     print(f"\n--- Результаты ---")
#     print(f"Кол-во измер: {len(numbers)}")
#     print(f"Мин знач: {min_m}")
#     print(f"Макс знач: {max_m}")
#     print(f"Среднее знач: {avg_m:.2f}")

# if __name__ == "__main__":
#     main()


import json
import logging
import sys
from pathlib import Path
from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max

def setup_logging(log_file):
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=log_file,level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s',encoding='utf-8')

def load_config(config_path):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Ошибка: Файл config.json не найден.")
        sys.exit(1)

def main():
    config = load_config("config.json")
    setup_logging(config["log_file"])
    
    logging.info("=== Программа запущена ===")
    print("Программа запущена.")
    
    file_path = Path(config["input_file"])
    
    if not file_path.exists():
        logging.error(f"Файл не найден: {file_path}")
        print(f"Ошибка: Файл {file_path} не найден.")
        return
        
    try:
        numbers = read_numbers(file_path)
        logging.info(f"Прочитано чисел: {len(numbers)}")
        validate_numbers(numbers)
        
        avg = calculate_average(numbers)
        min_val = find_min(numbers)
        max_val = find_max(numbers)
        
        print(f"\n--- Результаты ---")
        print(f"Кол-во: {len(numbers)}")
        print(f"Мин: {min_val}")
        print(f"Макс: {max_val}")
        print(f"Среднее: {avg:.2f}")
        
        logging.info(f"Результат: мин={min_val}, макс={max_val}, среднее={avg:.2f}")
        
    except ValueError as e:
        logging.error(f"Ошибка данных: {e}")
        print(f"Ошибка данных: {e}")
    finally:
        logging.info("=== Программа завершена ===")
        print("\nРабота программы завершена.")

if __name__ == "__main__":
    main()