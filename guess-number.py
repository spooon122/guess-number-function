from random import *


def not_in_range(a, x, y):
    if not int(x) < a or int(y) < a:
        print('Выбранное число не входит в диапазон рандома')
        return True
    else:
        return False


def guess_number():
    x, y = input(), input()
    while not x.isdigit():
        print('"X" not is digit')
        x = input()
    while not y.isdigit():
        print('"Y" not is digit')
        y = input()
    random_number = randint(int(x), int(y))
    print(random_number)
    a = 0
    while a != random_number:
        a = int(input())
        if random_number < a:
            if not_in_range(a, x, y):
                continue
            print('Слишком много, попробуйте еще раз')
        elif random_number > a:
            if not_in_range(a, x, y):
                continue
            print('Слишком мало, попробуйте еще раз')
        else:
            print('Угадали, поздравляем!', 'Хотите повторить? д = да/н = нет', sep='\n')
            if input() == 'д':
                print('Отлично, игра началась снова')
                guess_number()
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


guess_number()
