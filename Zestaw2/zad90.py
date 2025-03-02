from math import log10, floor 


def generate_mask(num):
    cnt = 0
    lenght = floor(log10(num)) + 1

    for mask in range(1, 2**lenght):
        tmp = num
        pot = 1
        bud = 0

        for i in range(lenght):
            if mask % 2 == 1:
                bud += (tmp % 10) * pot
                pot *= 10
            tmp //= 10
            mask //= 2
        print(bud)
        #end for
        if bud % 7 == 0:
            cnt +=1
    return cnt

print(generate_mask(2315))
