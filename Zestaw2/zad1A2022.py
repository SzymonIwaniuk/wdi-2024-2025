def sequence(T):
    n = len(T)
    
    for i in range(n - 3):  # Zakładamy, że ciąg ma przynajmniej 3 elementy
        for length in range(3, (n - i) // 2 + 1):  # Próbujemy różne długości ciągu
            first_seq = T[i:i + length]
            second_seq = T[i + length:i + 2 * length]
            
            # Sprawdzamy czy każdy element drugiego ciągu jest wielokrotnością odpowiedniego elementu pierwszego
            ratio = second_seq[0] / first_seq[0] if first_seq[0] != 0 else None
            if ratio and all(second_seq[j] == first_seq[j] * ratio for j in range(length)):
                return i, i + length - 1
    
    return None  # Jeśli nie znaleziono ciągu

print(sequence([2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]))
