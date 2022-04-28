from generate_txt import generate
import json

book = {1: 6, 2: 'Kiev', 3: True}


def dump(filename):
    with open(filename, 'w') as f:
        data = json.dumps(book)
        print(data, type(data))
        f.write(data)


def random_json(filename, data):
    with open(filename, 'w') as f:
        for i in range(len(data)):
            s = data[i]
            s = int(s.rstrip('\n'))
            dick = {'id': i, 'number': s}
            data2 = json.dumps(dick)
            data3 = data2 + '\n'
            f.write(data3)


if __name__ == '__main__':
    # dump("data.json")
    random_json('data.json', generate(10))
    pass
