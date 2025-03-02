# --- main
num = int( input() )
s = int( input() )
current_num = 0
i = 0

while num != 0:
    current_num += (num % s) * 10**i
    num //= s
    i += 1

print(current_num)
    
    
