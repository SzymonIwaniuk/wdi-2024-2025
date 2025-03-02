def next_non_fib_sum(n):
    
    def is_non_fib_sum(target):
        fib1, fib2 = 1, 1
        current_sum = 0

        while fib1 <= target:
            current_sum += fib1
            if current_sum == target:
                return True
            # Rozpoczynamy nowy fragment sumując z fib2
            if current_sum > target:
                current_sum -= fib1  # Odejmujemy pierwszy element fragmentu
            # Generujemy następny element Fibonacciego
            fib1, fib2 = fib2, fib1 + fib2
        
        return False

    candidate = n + 1  
    while True:
        if not is_non_fib_sum(candidate):
            return candidate
        candidate += 1

print(next_non_fib_sum(3))

