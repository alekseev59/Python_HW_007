from datetime import datetime as dt


def recording(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{};"Запрос: ";{}\n'
                   .format(data, time))


def log_write(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write('{};"Записан в хранилище данных: ";{}\n'
                   .format(data, time))
    print('Сотрудник добавлен')
