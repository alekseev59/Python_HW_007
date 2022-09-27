from user_search import *
from data import *
from record_data import *
from add_user import *


def start():
    num = int(input(
        'Введите "1" Что бы Найти пользователя.\nВведите "2" Что бы Добавить пользователя.\n'))
    if num == 1:
        a = get_list()
        num = search(a)
        recording(num)

    if num == 2:
        user = user_write()
        log_write(user)
