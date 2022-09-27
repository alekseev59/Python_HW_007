def search(user_list):
    req = input('Кого мы ищем? \n')
    t = True
    for i in user_list:
        if req in i:
            print(i)
            t = False
    if t:
        print('Нет такого человека')
    return req + f';{not t}'
