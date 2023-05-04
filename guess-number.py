from random import *


def is_valid(valid):
    if 1 <= valid <= 100:
        return True
    else:
        return False


def guess_number():
    random_number = randint(1, 100)
    print(random_number)
    a = 1
    while a != random_number:
        a = int(input())
        if random_number < a:
            if not is_valid(a):
                print('Выбранное числа не входит в диапазон рандома')
                continue
            print('Слишком много, попробуйте еще раз')
        elif random_number > a:
            if not is_valid(a):
                print('Выбранное числа не входит в диапазон рандома')
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

