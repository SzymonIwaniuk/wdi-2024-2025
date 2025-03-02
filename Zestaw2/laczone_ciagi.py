#Dana jest tablica T zawierająca ciąg liczb naturalnych. Maksymalny, spójny podciąg rosnący to taki, w
#którym przed pierwszym elementem nie ma elementu mniejszego, a za ostatnim elementem nie ma elementu
#większego. Proszę napisać funkcję sequence(T) która sprawdza czy w tablicy można znaleźć dwa maksy-
#malne, spójne podciągi rosnące, każdy o długości większej od 2, takie aby po ich złączeniu stanowiły jeden
#ciąg rosnący. Funkcja powinna zwrócić wartość True albo False
#Przykłady:
#sequence( [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2] ) zwróci True
#sequence( [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2] ) zwróci False



def check(T, first1, first2, last1, last2):
    if last2 != 0:
        if T[last2] < T[first1]: return True
        if T[last1] < T[first2]: return True
    
    return False

def sequence(T):
    n = len(T)
    maxi1 = maxi2 = 0
    cnt = 1
    first1 = first2 = last1 = last2 = 0
    
    for i in range(n - 1):
        if T[i] < T[i + 1]:
            cnt += 1
            if (cnt > maxi1 or cnt > maxi2) and cnt > 2:
                if cnt > maxi1:
                    maxi2, maxi1 = maxi1, cnt
                    first2, last2 = first1, last1
                    first1, last1 = i - cnt, i
                else:
                    maxi2 = cnt
                    first2, last2 = i - cnt, i
        else:
            cnt = 0
    
    return check(T, first1, first2, last1, last2)


print(sequence( [2,15,17,14,17,19,23,2,6,4,8,1,2,3,4,5,6,11,12,13,11] ))
                
        
        
        
