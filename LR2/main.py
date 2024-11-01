money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
while money_capital >= 0:
    difference = spend - salary
    if difference > 0:
        money_capital -= difference
    spend *= (1 + increase)
    if money_capital < 0:
        break
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)




# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
