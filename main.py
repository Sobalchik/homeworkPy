# laba_3
import collections


def ex_1():
    line = input("Enter string: ")
    count = 1
    result = ""
    for i in range(0, (len(line))):
        if i == (len(line) - 1):
            if count > 1:
                result += line[i] + str(count)
            else:
                result += line[i]
            print(result)
            return

        if line[i] == line[i + 1]:
            count = count + 1
        else:
            if count > 1:
                result += line[i] + str(count)
            else:
                result += line[i]
            count = 1


def ex_2():
    line = input("Enter string: ")
    result = ""
    num = ""
    for i in range(0, (len(line))):
        if 65 <= ord(line[i]) <= 90 or 97 <= ord(line[i]) <= 122:

            if i == (len(line) - 1):
                result += line[i]
                print(result)
                return

            if 48 <= ord(line[i + 1]) <= 57:
                j = i
                while line[j] != line[-1] and 48 <= ord(line[j + 1]) <= 57:
                    num += line[j + 1]
                    j += 1
                j = 0
                for j in range(0, int(num)):
                    result += line[i]
            else:
                result += line[i]
            num = ""

    print(result)


def ex_3():
    line = input("Enter string: ")
    print(collections.Counter(line.replace(" ", "")).most_common(3))


def ex_4():
    one_to_nineteen = (u'ноль',
                       u'один', u'два', u'три', u'четыре', u'пять', u'шесть', u'семь', u'восемь', u'девять',
                       u'десять', u'одиннадцать', u'двенадцать', u'тринадцать', u'четырнадцать', u'пятнадцать',
                       u'шестнадцать', u'семнадцать', u'восемнадцать', u'девятнадцать')

    decs = ('', u'десять', u'двадцать', u'тридцать', u'сорок',
            u'пятьдесят', u'шестьдесят', u'семьдесят', u'восемьдесят', u'девяносто')

    hundreds = ('', u'сто', u'двести', u'триста', u'четыреста',
                u'пятьсот', u'шестьсот', u'семьсот', u'восемьсот', u'девятьсот')

    thousands = ('', u'одна тысяча', u'две тысячи', u'три тысячи', u'четыре тысячи')

    def _one_convert(integer):
        return one_to_nineteen[integer]

    def _two_convert(integer, string):
        if integer in range(20):
            result = one_to_nineteen[integer]

        else:
            result = decs[int(string[0])]

            if string[1] != '0':
                result = u'%s %s' % (result, one_to_nineteen[int(string[1])])

        return result

    def convert(string):
        length = len(string)
        integer = int(string)

        if length == 1:
            result = _one_convert(integer)

        elif length == 2:
            result = _two_convert(integer, string)

        elif length == 3:
            result = hundreds[int(string[0])]

            tail = string[-2:]

            if tail != '00':
                result = u'%s %s' % (result, convert(tail))

        elif length in range(4, 7):
            tail = convert(string[-3:])

            str_head = string[:-3]
            int_head = int(str_head)

            if int_head in range(1, 5):
                head = thousands[int_head]

            else:
                head = u'%s тысяч' % (convert(str_head))

            result = u'%s %s' % (head, tail)

        else:
            result = ''

        return result.strip()

    number = input("Enter number: ")
    print(convert(number))


if __name__ == '__main__':
    # ex_1()
    # ex_2()
    # ex_3()
      ex_4()
