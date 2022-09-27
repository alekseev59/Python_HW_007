from urllib import request


def get_list():
    with open(f'info.txt', 'r', encoding='UTF-8') as f:
        user_list = []
        for i in f.readlines():
            user_list.append(i.split(', '))
    return user_list
