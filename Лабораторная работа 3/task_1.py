# Функция для поиска индекса товара
def item_position(all_items, item):
    # Цикл по индексам и именованиям продуктов
    for i, name in enumerate(all_items):
        # Если текущий продукт является искомым
        if name == item:
            # возвращение позиции
            return i
    # Если товар не встречается в списке, то возращается None
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = item_position(items_list, find_item)  # вызов функции, для получения индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
