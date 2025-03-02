from random import randint

def BirthdayMatchProbability(N):
    dni = [0 for _ in range(N)] # Tablica przechowująca dni urodzin N osób

    successes = 0

    for attempt in range(10000):  # zrobimy 10000 symulacji losowania dni dla N osób (arbitralna dokładność)

        flag = False
        for i in range(N):
            dni[i] = randint(1, 366) # Każdej osobie przyporządkujemy dzień w roku będący dniem jej urodzin

        for i in range(N): # pozostaje sprawdzić, czy jakiekolwiek dwa elementy tablicy mają tę samą wartość...
            for j in range(N):
                if i == j: # ...uważając, aby nie porównać jednego elementu z samym sobą!
                    continue

                if dni[i] == dni[j]:
                    flag = True
            # end for
            if flag:
                successes += 1 # w razie sukcesu odnotowujemy symulację jako sukces.
                break
        # end for
    # end for
    probability = successes / 10000 # obliczamy prawdopodobieństwo.
    return probability

for i in range(20, 41):
    print("N = ", i, ": ", round(BirthdayMatchProbability(i) * 100, 2), " %", sep='')
