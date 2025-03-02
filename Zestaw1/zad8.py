eps = 1e-10
a = 0 #poczatek przedzialu
b = 10 #koniec przedzialu

while True:
    c = (a + b) / 2
    F = c**c - 2024
    
    if F > 0:
        b = c
    else:
        a = c
    if abs(F) < eps: break

print(c) 
                    
