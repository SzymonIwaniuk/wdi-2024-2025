def fib(a, b):
    # This function returns the next Fibonacci numbers
    return b, a + b

def zad9(n):
    i = n
    flag = n + 1000  # Set an upper limit for searching

    while i < flag:  # Loop to find the next number that cannot be a Fibonacci sum
        i += 1
        a, b = 0, 1
        suma = 0
        found = False  # Flag to track if i can be represented

        while suma < i:  # Keep summing Fibonacci numbers to see if we can reach 'i'
            suma = 0  # Reset sum for each new starting point
            a, b = 0, 1  # Reset Fibonacci sequence
            while suma < i:  # Try to sum consecutive Fibonacci numbers
                suma += a
                if suma == i:
                    found = True  # i can be represented as a sum of consecutive Fibonacci numbers
                    break
                a, b = fib(a, b)
            if found:  # If i can be represented, stop checking
                break

        if not found:  # If i cannot be represented, return i
            return i

    return -1  # If no result is found in the range

# Example usage:
n = int(input("Podaj liczbę n (0 < n < 1000): "))
print("Następna liczba, której nie można przedstawić jako suma elementów ciągu Fibonacciego
