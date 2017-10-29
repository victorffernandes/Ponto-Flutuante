
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

    return result * sign

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

#Excesso em K - bin, bin
def excess (num, k):
    n1 = binToDec(num)
    n2 = binToDec(k)

    return decToBin(int(n1 +  n2))
print(excess("1101010","1111111"))
