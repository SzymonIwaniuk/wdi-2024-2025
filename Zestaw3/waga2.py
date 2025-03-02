import random

# Function to generate a list of random integers
def generuj(n):
    return [random.randint(1, 9) for _ in range(n)]
# end def

# Function to count pairs of numbers whose product equals `s`
def licz_pary(t, s):
    n = len(t)
    licz = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if t[i] * t[j] == s:
                licz += 1
    print("Pary:", licz)
# end def

# Generate a list of 20 random numbers
t = generuj(20)

# Count pairs whose product equals 24
licz_pary(t, 24)
