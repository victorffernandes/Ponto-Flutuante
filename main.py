num = input("Insira o número na base 2 a ser transformado para ponto flutuante: ")

def binToDec(a):
    result = 0

    for i in range(len(a)):
        result += float(a[(len(a) - 1) - i]) * 2**i

    return result

def decToBin(b):
    sign = ""
    i = ""

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

    try:#
        n = ""
        if len(num.split(",")) > 1:
            n1 = num.split(",")[0]
            n2 = num.split(",")[1]
            n = n1 + "." + n2
        else:
            n = num
        t = float(n)
    except:#NaN
        return "0 11111111 00010000000000000000001"

    if int(num.split(",")[0][1:]) > 0: #normalizado
        n1 = num.split(",")[0]
        n2 = ""
        for i in range(2, len(n1)):
            n2 += n1[i]
        try:
            n2 += num.split(",")[1]
        except:
            n2 += ""
        for i in range(len(n2), 23):
            n2 += "0"

        exp = excess(str(len(n1) - 2), 127)

        for i in range(len(exp),8):
            exp += "0" + exp

        if num[0] == "-":
            return "1 " + exp + " " + n2
        else:
            return "0 " + exp + " " + n2
    else:#não normalizado
        posI = len(num) - 129
        mant = ""
        for i in range(129, 152):
            try:
                mant += num[i]
            except:
                mant += "0"

        if num[0] == "-":
            return "1 " + "00000000 " + mant
        else:
            return "0 " + "00000000 " + mant

print(getIEEE(num))