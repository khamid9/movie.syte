from locale import locale_alias
pin_code = 1234
number=3

lol=int(input('пиши пороль:'))
if number != pin_code :
    print(f'пин не правельный {2} попыток осталось')
    lol = int(input('пиши пороль:'))












amount = 500
number = int(input('Введите ваш пин код: '))
if number != pin_code:
    print('Неверный пин код')
else:
    while True:
        print('1 - Посмотреть счет')
        print('2 - Добавить деньги')
        print('3 - Снять деньги')
        print('4 - Выйти')
        code = int(input('Выберите действие: '))
        if code == 1:
            print(f'Ваш счет {amount} сом')
        elif code == 2:
            money=int(input('сколько денег хотите добавть:'))
            amount += money
            print('вы успешно пополнили баланс')
        elif code == 3:
           money2 = int(input('сколько хотите вывести:'))
           if amount < money2:
               print('недостатосчно средств!!пополните баланас выберев код 2')
           else:
               amount -= money2
               print('вы успешно взяли деньги')
        elif code == 4:
            break



