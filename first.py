nums = [1, 228, 1337, 1941, 10]
ans = int(input(print('Загадайте число:')))
print('Исходный список:', *nums)
print('Ваше число:', ans)
if ans in nums:
    print('Поздравляю, Вы угадали число!')
else:
    print('Нет такого числа!')