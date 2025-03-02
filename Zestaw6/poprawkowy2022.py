#Proszę napisać funkcję Two(p), która otrzymuje wskazanie na listę i rozdziela elementy listy do dwóch
#list. W pierwszej powinny znaleźć się elementy, które w liście wejściowej występowały dokładnie dwa
#razy, a w drugiej wszystkie pozostałe. Funkcja powinna zwrócić wskaźniki do powstałych dwóch list.
class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def add(num,num_counter,nums,l):
    for i in range(l):
        if num == nums[i]:
            num_counter[i] += 1
            return num_counter

def to_delete(num_counter,nums,l):
    nums_to_delete = []
    for i in range(l):
        if num_counter[i] == 2:
            nums_to_delete += [nums[i]]

    return nums_to_delete

def Two(p):
    if p == None:
        return None, None

    run = p
    nums =  []
    while run != None:
        if run.val not in nums:
            nums += [run.val]
        run = run.next

    l = len(nums)
    num_counter = l * [0]

    run = p
    while run != None:
        num_counter = add(run.val,num_counter,nums,l)
        run = run.next

    g1 = Node() #wartownik 1 pierwszej listy
    g2 = Node() #wartownik 2 drugiej listy
    head1 = g1
    head2 = g2
    run = p
    nums_to_delete = to_delete(num_counter,nums,l)
    wystapil = []

    while run != None:
        if run.val in nums_to_delete:
            if run.val not in wystapil:
                head1.next = Node(run.val)
                head1 = head1.next
                wystapil += [run.val]
        else:
            head2.next = Node(run.val)
            head2 = head2.next
        run = run.next

    return g1.next, g2.next

# Tworzenie przykładowej listy
p = Node(1, Node(2, Node(3, Node(2, Node(4, Node(1, Node(5)))))))

# Wywołanie funkcji
list1, list2 = Two(p)

# Funkcja do wypisywania listy
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Wynikowe listy
print("List1 (dokładnie dwa razy):")
print_list(list1)
print("List2 (pozostałe):")
print_list(list2)