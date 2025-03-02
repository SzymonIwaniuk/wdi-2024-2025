def hanoi(n):

    def rek(n,A,C,B):
        if n == 1:
            print(f" 1 {A} --> {C}")
            return

        rek(n - 1,A, B, C)

        print(f"{n}, {A} --> {C}")

        rek(n - 1, B,C,A)


    rek(n, "A", "C","B" )

hanoi(20)