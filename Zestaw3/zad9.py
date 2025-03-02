# --- main
T = [3 , 6 , 7 , 8 , 9 , 10 , 11,  12 , 13 , 5 , 3 , 4 , 5]
score = 0 
N = len(T)

for i in range(N):
    temp_i = i
    counter = 1
    
    while temp_i + 1 < N and T[temp_i + 1] == T[temp_i] + 1: 
            counter += 1
            temp_i += 1
    #end while
    if counter > score: score = counter

#end for


print(score)    
