def zad26(a, b, n):
    #Dzielenie pisemne
    print(a // b, end = ",")

    for i in range(n):
        a = a % b
        a = a * 10
        print( a // b, end = "")


print(zad26(9, 732, 10))
