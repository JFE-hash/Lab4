week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
num_of_weekends = int(input(print('Сколько выходных вы хотите?')))
weekends = week[-num_of_weekends:]
work_days = week[:len(week) - num_of_weekends]
print('Ваши выходные дни:', *weekends)
print('Ваши рабочие дни:', *work_days)