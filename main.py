# laba_4

def ex_1():
    num_list = [5, 6, 2, 7, 8, 9, 10, 3, 4]
    result = []
    for i in range(1, len(num_list)):
        if num_list[i] > num_list[i - 1]:
            result.append(num_list[i])
    print(result)


def ex_2():
    num_list = [5, 6, 2, 7, 8, 9, 10, 3, 4]
    num_list[num_list.index(max(num_list))], num_list[num_list.index(min(num_list))] = num_list[num_list.index(
        min(num_list))], num_list[num_list.index(max(num_list))]
    print(num_list)


def ex_3():
    num_list_1 = [5, 6, 2, 7, 8, 9, 10, 3, 4]
    num_list_2 = [4, 1, 3, 7, 4, 9, 6, 3, 1]
    result = 0
    unique_num_list_1 = list(set(num_list_1))
    for i in range(0, len(unique_num_list_1)):
        if unique_num_list_1[i] in num_list_2:
            result += 1
    print(result)


def ex_4(string_list):
    result = ''

    counter = dict()
    for i in range(len(string_list)):
        if string_list[i] in counter:
            counter[string_list[i]] += 1
        else:
            counter[string_list[i]] = 1

    for key, value in counter.items():
        result += str(value) + ' '

    print(result)



if __name__ == '__main__':
    # ex_1()
    # ex_2()
    # ex_3()
    list_1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
    list_2 = ['aaa', 'bbb', 'ccc']
    list_3 = ['abc', 'abc', 'abc']
    ex_4(list_1)
