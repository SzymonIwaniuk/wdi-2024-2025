def ciag(n):
    an = 0
    i = 1
    while an <= n: 
        an = i * i + i + 1

        if n % an == 0:
            return True
        
        i += 1
    return False





print(ciag(7))
