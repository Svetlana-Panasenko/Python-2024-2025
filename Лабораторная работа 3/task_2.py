# Функция для поиска общих участников
def find_common_participants(str_1, str_2, separator=','):
    # Разделяем строки на отдельные фамилии, учитывая их разделитель
    surnames_1 = str_1.split(separator)
    surnames_2 = str_2.split(separator)
    # Поиск пересечение и сортировка полученного списка
    all_surnames = sorted(set(surnames_1).intersection(surnames_2))
    return all_surnames


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Выводим результат функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
