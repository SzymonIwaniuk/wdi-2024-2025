
#TODO: merge sort

def solve(T1, T2):
    n = len(T1)
    out_idx = 0
    indexes = [0 for _ in range(n)]  # Keep track of the current index in each row
    last_inserted = None  # Track the last inserted value to avoid duplicates

    while True:
        min_row = -1
        min_value = float('inf')

        # Find the minimum value among the rows that have not been fully processed
        for r in range(n):
            if indexes[r] < len(T1[r]) and T1[r][indexes[r]] < min_value:
                min_value = T1[r][indexes[r]]
                min_row = r

        if min_row == -1:  # No more elements left to process
            break

        # Only add min_value to T2 if it's different from the last inserted value
        if min_value != last_inserted:
            T2[out_idx] = min_value
            out_idx += 1
            last_inserted = min_value

        # Increment the index of the row that had the minimum value
        indexes[min_row] += 1

    return T2

if __name__ == "__main__":
    T1 = [[2, 3, 5],
          [1, 4, 6],
          [2, 4, 8]]
    T2 = [0 for _ in range(len(T1) * len(T1[0]))]  # The size should be n * m
    print(solve(T1, T2))