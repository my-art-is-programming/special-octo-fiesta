import json
import random


def generate(n):
    out = []
    for i in range(n):
        number = random.randint(0, 100)
        out.append(number)
    out = set(sorted(out))
    out2 = []
    for i in out:
        out2.append(str(i) + '\n')
    return out2


def load(filename):
    """
    Открываем файл, читаем, переводим всё в int-ы, возвращаем список интов, закрываем файл
    """
    with open(filename, 'r', newline='\n') as f:
        data = f.read()
        data = data.split('\r\n')
        for i in range(len(data)):
            try:
                data[i] = int(data[i])
            except ValueError:
                print('ValueError')
                del data[i]
    return data


def dump(filename, data):
    with open(file=filename, mode='w') as f:
        f.writelines(data)


if __name__ == '__main__':
    # dump('data.txt', generate(100))
    load('data.txt')
