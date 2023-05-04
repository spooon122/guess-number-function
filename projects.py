from random import *


def guess_number():
    random_number = randint(1, 100)
    print(random_number)
    a = 0
    while a != random_number:
        a = int(input())
        if random_number < a:
            print('Слишком много, попробуйте еще раз')
        elif random_number > a:
            print('Слишком мало, попробуйте еще раз')
        else:
            print('угадали, поздравляем!')


guess_number()
