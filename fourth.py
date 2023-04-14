my_group = ["Иванов", "Петров", "Сидоров", "Козлов", "Новиков",
            "Васильев", "Кузнецов", "Соловьев", "Морозов", "Попов"]
another_group = ["Алексеев", "Макаров", "Ильин", "Кудрявцев", "Белов",
            "Федоров", "Дмитриев", "Калинин", "Андреев", "Гусев"]
sport_team = []

for i in range(5):
    sport_team.append(my_group[i])
    sport_team.append(another_group[i])
print('Исходный список моей группы:', *my_group)
print('Исходный список другой группы:', *another_group)
print('Получившийся состав спортивной команды:', *sport_team)
print(len(sport_team))

if 'Иванов' in sport_team:
    print(f'Иванов входит в список {sport_team.count("Иванов")} раз')

print('Отсортированный список спортивной команды:', *sorted(sport_team))