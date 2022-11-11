# laba_6

def ex_1():
    f = open('input_1.txt', 'r')
    with open("input_1.txt", "r") as f:
        text = f.read()
    numbers = []
    for t in text.split():
        numbers.append(int(t))

    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    print(result)


def ex_2():
    f = open('input_2.txt', 'r')
    with open("input_2.txt", "r") as f:
        text = f.read()
    numbers = []
    for t in text.split():
        numbers.append(int(t))
    result = sorted(numbers)
    string = ''
    for i in range(len(numbers)):
        string = string + str(result[i]) + ' '
    with open("result_2.txt", "w") as f:
        f.write(string)


def ex_3():
    names = dict()
    f = open('input_3.txt', 'r')
    with open("input_3.txt", "r") as f:
        for line in f:
            numbers = line[-2]
            name = {line: int(numbers)}
            names.update(name)

    sorted_values = sorted(names.values())  # Сортировка словаря Python по значению

    sorted_names = {}

    for i in sorted_values:
        for k in names.keys():
            if names[k] == i:
                sorted_names[k] = names[k]
                break

    keys = list(sorted_names.keys())
    with open("result_3_young.txt", "w") as f:
        f.write(keys[0])
    with open("result_3_elder.txt", "w") as f:
        f.write(keys[-1])



if __name__ == '__main__':
    # ex_1()
    # ex_2()
    ex_3()
