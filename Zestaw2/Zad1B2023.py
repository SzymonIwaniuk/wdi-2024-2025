def allOnes(a):
    for n in a:
        if n != 1:
            return False

    return True 


def isValid(a):
    for i in range(9):
        cnts1 = [0 for _ in range(9)]
        cnts2 = [0 for _ in range(9)]
        for j in range(9):
            cnts1[a[i][j] - 1] += 1
            cnts2[a[j][i] - 1] += 1
        if not (allOnes(cnts1) and allOnes(cnts2)):
            return False

    return True

def swap(T, a, b):
    ax, bx = (a % 3) * 3, (b % 3) * 3
    ay, by = (a // 3) * 3, (b // 3) * 3
    for x in range(3):
        for y in range(3):
            T[ax + x][ay + y], T[bx + x][by + y] = T[bx + x][by + y], T[ax + x][ay + y]

def sudoku(T):

    for a in range(9):
        for b in range(a + 1, 9):
            swap(T, a, b)
            r = isValid(T)
            swap(T, a, b)
        
            if r:
                        return (a + 1, b + 1)

    return None

data = [
	[8, 1, 2, 7, 5, 3, 6, 4, 9],
	[9, 4, 3, 6, 8, 2, 1, 7, 5],
	[6, 7, 5, 4, 9, 1, 2, 8, 3],
	[1, 5, 4, 3, 6, 8, 8, 9, 6],
	[3, 6, 9, 9, 1, 7, 7, 2, 1],
	[2, 8, 7, 4, 5, 2, 5, 3, 4],
	[5, 2, 1, 9, 7, 4, 2, 3, 7],
	[4, 3, 8, 5, 2, 6, 8, 4, 5],
	[7, 9, 6, 3, 1, 8, 1, 6, 9]
]
print(sudoku(data))

        
