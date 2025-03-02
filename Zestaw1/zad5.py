s = int( input("Podaj s") )
n = 0
sum = 0
a = 1

while sum <= s:
    sum += a
    n += 1
    a += 2
print(n - 1)
