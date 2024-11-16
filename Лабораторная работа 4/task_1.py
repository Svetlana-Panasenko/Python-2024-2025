import json


def task() -> float:
    # Объявляем имя входного файла
    file_name = 'input.json'
    # Инициализация значеня суммы
    total_sum = 0
    # Чтение  данных  файла, используя менеджер контекста
    with open(file_name, 'r') as file:
        # Загрузка содержимого из файла
        data = json.load(file)
        # Цикл по каждому элементу в списке
        for element in data:
            # Если текущий элемент содержит ключи 'score' и 'weight'
            if 'score' in element and 'weight' in element:
                # Обновляем значение суммы произведений
                total_sum += element['score'] * element['weight']

    return round(total_sum, 3)


print(task())
