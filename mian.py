num = input("Insira o número na base 2 a ser transformado para ponto flutuante: ")

def binToDec(a):
    result = 0
    sign = 1
    algarismos = a
    if a[0] == "-":
        sign = -1
        algarismos = a[1:]
    elif a[0] == "+":
        algarismos = a[1:]
    for i in range(len(algarismos)):
        result += float(algarismos[(len(algarismos) - 1) - i]) * 2**i

    return result #* sign

def decToBin(b):
    sign = ""
    b = str(b)
    if b[0] == "-":
        sign = "-"
        b = b[1:]
    elif b[0] == "+":
        b = b[1:]
    i = ""
    b = int(b)
    while b != 1:
        i += str(int(b % 2))
        b = b // 2

    return sign + ((i + "1")[::-1])

def excess (num, k):
    n1 = binToDec(num)

    return decToBin(int(n1 + k))

def getIEEE(num):

    if num == "0" or str == "+0" or str == "-0":
        return "0 00000000 00000000000000000000000"
    elif num == "-inf":
        return "1 11111111 00000000000000000000000"
    elif num == "+inf":
        return "0 11111111 00000000000000000000000"

    try:
        t = int(num[1:])
    except:
        return "0 11111111 00010000000000000000001"

    if num[1] == 1:
        n1 = num.split(",")[0]
        n2 = ""

        for i in range(2, len(n1)):
            n2 += n1[i]

        n2 += num.split(",")[1]

        for i in range(len(n2), 23):
            n2 += "0"

        if num[0] == "-":
            return "1 " + excess("+" + len(n1) - 2, 127) + " " + n2
        else:
            return "0 " + excess("+" + str(len(n1) - 2), 127) + " " + n2

    else:

        n2 = num[len(num)-24:]

        if num[0] == "-":
            return "1 " + "00000000 " + n2
        else:
            return "0 " + "00000000 " + n2

print(getIEEE("num"))
