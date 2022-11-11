# laba_2

def ex_1():
    n = int(input())
    result = [1]
    for i in range(n):
        print(result)
        result = [sum(x) for x in zip([0] + result, result + [0])]


def ex_2():
    n = int(input())
    depth = 2 ** n
    result = [0] * depth
    for i in range(depth):
        result[i] = [0] * depth
        result[i][0] = 1
        result[i][i] = 1

    for i in range(1, depth):
        for j in range(1, depth):
            result[i][j] = (result[i - 1][j - 1] + result[i - 1][j]) % 2

    for i in range(depth):
        print(' ' * int(((depth - i) / 2)), end='')
        for j in range(depth):
            res = '*' if result[i][j] == 1 else ' '
            print(res, end='')
        print()


if __name__ == '__main__':
    # ex_1()
     ex_2()
