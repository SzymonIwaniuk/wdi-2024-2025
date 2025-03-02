T = [4, 3, 78, 79, 63, 10, 85, 95, 20, 19, 56, 55, 71, 10, 1, 2]

def sort(T):
    N = len(T)

    for i in range(N):
        for j in range(N):
            if T[i] < T[j]:
                T[i], T[j] = T[j], T[i]
    return(T)


def dziesiata(ST = sort(T)):
    print(ST[9])

dziesiata(T)
    
def quicksort(arr):

  pivot = arr[len(arr) - 1]

  i = 0
  for j in range(len(arr) - 1):
    if arr[j] < pivot:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1

  arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]

  return arr


print(quicksort(T))
