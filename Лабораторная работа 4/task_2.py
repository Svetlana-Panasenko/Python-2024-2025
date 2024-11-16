# Импортируем необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Инициализируем список для хранения записей
    data = []
    # Открываем содержимое CSV файла для чтения
    with open(INPUT_FILENAME, mode='r', newline='') as file_csv:
        # Используем DictReader для чтения значений из CSV
        reader_scv = csv.DictReader(file_csv)

        # Итерация по каждой строке, возвращаемой DictReader
        for i in reader_scv:
            # Добавление каждой строки, представленной в виде словаря, в список data
            data.append(i)

    # Сериализуем данные в JSON формат с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w') as file_json:
        json.dump(data, file_json, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
