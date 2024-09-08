def password_gen(n):

    result = []
    for i in range(1, n):
        for j in range(i + 1, 20):
            if n % (i + j) == 0:
                result.extend((i , j))
    return result


print("Введите число от 3 до 20: ")
while True:
    num1 = int(input("> "))
    if num1 == 0:
        break
    if num1 < 3 or num1 > 20:
        print('Введите нужное число')
        continue
    result = password_gen(num1)
    print(f'Нужный пароль: {result}')

