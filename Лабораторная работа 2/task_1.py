money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_months = 0  # Счётчик месяцев
# Цикл выполняется, пока траты не превышают бюджет
while spend <= money_capital + salary:
    # Обновляется значение средств в подушке безопасности
    money_capital = money_capital - spend + salary
    count_months += 1
    # В следующем месяце устанавливаем увеличение расходов
    spend = spend + increase * spend

print("Количество месяцев, которое можно протянуть без долгов:", count_months)
