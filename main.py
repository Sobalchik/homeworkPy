# laba_1

def ex_1():
    print("Enter numbers")
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    third_num = input("Enter third number: ")
    if first_num == second_num and second_num == third_num:
        print("3")
        return
    if first_num == second_num or first_num == third_num or second_num == third_num:
        print("2")
        return

    print("0")


def ex_2():
    num = int(input("Enter number: "))
    line = ""
    for i in range(1, num):
        line = line + str(i)
        print(line)


def ex_3():
    num = int(input("Enter number: "))
    position = int((num * 2 - 1) / 2)
    for i in range(1, num + 1):
        for j in range(position - i + 1):
            print(end=" ")
        for j in range(1, i * 2):
            if j <= i:
                print(j, end="")
            else:
                print(i - (j - i), end="")
        for j in range(position - i + 1):
            print(end=" ")
        print()


def ex_4():
    n = int(input("Enter n = "))
    if n < 10:
        kol = n * 2 - 1
    elif n < 100:
        kol = 2 * 9 - 1 + 2 * 2 * (n - 9) - 1
    elif n < 1000:
        kol = 2 * 9 - 1 + 2 * 2 * n - 1 + 3 * 2 * n - 1
    f = False
    if kol % 2 == 0:
        f = True
    string = ""
    for i in range(1, n + 1):
        for j in range(1, i * 2):
            if j <= i:
                string += str(j)
                if f and j < 10:
                    string += " "
            else:
                string += str(i - (j - i))
                if f and i - (j - i) < 10:
                    string += " "
        string = string.center(kol + 17, ' ')
        print(string)
        string = ""


if __name__ == '__main__':
    # ex_1()
    # ex_2()
    ex_4()
