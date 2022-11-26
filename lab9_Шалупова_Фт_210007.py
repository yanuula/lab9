import random
import logging

logging.basicConfig(level=logging.INFO,
                    filename="lab9.log", format="%(asctime)s %(levelname)s %(message)s")

while True:
    try:
        n = int(input('Введите максимальное число: '))
        logging.info('n = {}'.format(n))
        assert n > 1
        logging.info('suitable')
        break
    except AssertionError:
        print('Число должно быть больше 1')
        logging.exception('less than 1')
    except ValueError:
        print('Ошибка ввода')
        logging.exception('incorrect input')
while True:
    try:
        k = int(input('Введите кол-во попыток: '))
        logging.info('k = {}'.format(k))
        assert k > 0
        break
    except AssertionError:
        print('Число должно быть больше 0')
        logging.exception('less than 0')
    except ValueError:
        print('Ошибка ввода')
        logging.exception('incorrect input')
hidden_num = random.randint(1, n)
logging.info('hidden_num = {}'.format(hidden_num))

while k > 0:
    print('Кол-во попыток - {}'.format(k))
    try:
        num = int(input('Введите загаданное число: '))
        logging.info('input num = {}'.format(num))
        assert 1 <= num <= n
        logging.info('suitable')
        if num == hidden_num:
            print('Верно!\n')
            logging.info('the number is guessed')
            break
        else:
            k -= 1
            print('Неверно!')
            logging.info('the number isn\'t guessed')
            if num < hidden_num:
                print('Число {} меньше загаданного'.format(num))
            else:
                print('Число {} больше загаданного'.format(num))
            if k == 0:
                print('Попытки закончились\n')
                logging.info('attempts ended')
    except AssertionError:
        print('Число должно быть от 1 до {}'.format(n))
        logging.exception('not in range')
    except ValueError:
        print('Ошибка ввода')
        logging.exception('incorrect input')
