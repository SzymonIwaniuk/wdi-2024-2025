def sprawdz(a,b,c):
    return nwd3(a,b,c) == 1

def nwd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def nwd3(a, b, c):
    return nwd(nwd(a,b),c)

def trojki(T):
    N = len(T)
    cnt = 0
    a = b = -1
    for i in range(N):
        if i - 2 >= 0: a = i - 2
        elif i - 1 >= 0: a = i - 1
        else: a = i

        if i + 3 <= N: b = i + 3
        elif i + 2 <= N: b = i + 2
        elif i + 1 <= N: n = i + 1
        else: b = i
        
        for j in range(a, b):
            if j == i: continue
            for k in range(a, b):
                if k == i or k == j: continue
                else:
                    if sprawdz(T[i],T[j],T[k]):
                        cnt += 1
            
    return cnt // 6


print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)


