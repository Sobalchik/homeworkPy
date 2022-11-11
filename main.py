# laba_5

def ex_1():
    arr = [1, 2, 3, 2, 1]
    unique_arr = set(arr)
    print(len(unique_arr))


def ex_2():
    arr_1 = [1, 10, 223, 413, 2]
    arr_2 = [1, 10, 223, 413, 2]

    arr_1 = set(arr_1)
    arr_2 = set(arr_2)

    if arr_1 < arr_2 or arr_2 < arr_1:
        print("True")
    else:
        print("False")


def ex_3():
    n = input("Enter n=")
    cities = set()
    for i in range(int(n)):
        cities.add(input())

    new_city = input("Enter new city: ")
    if new_city in cities:
        print("REPEAT")
    else:
        print("OK")



if __name__ == '__main__':
    # ex_1()
    # ex_2()
    ex_3()
