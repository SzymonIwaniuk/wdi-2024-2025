def zad4():
    a = 1
    b = 1
    suma = int(input() )

    while a + b <= suma:
        counter = 0
        temp_a = a
        temp_b = b

        while counter < suma:
            counter += temp_a
            if counter == suma: return True, a, b
            #end if 
            temp_a, temp_b = temp_b, temp_a + temp_b
        a, b = a, a + b
    return False
        #end while
    #end while 
print(zad4())
