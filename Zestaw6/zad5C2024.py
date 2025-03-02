#Lista zawiera wartości będące liczbami naturalnymi. Proszę napisać funkcję divide(p) (p wskazuje
#na pierwszy element listy), która rozdziela listę na dwie listy. W pierwszej powinny się znaleźć
#liczby, które są wielokrotnością (co najmniej dwukrotnością) kwadratu dowolnej liczby pierwszej, a w
#drugiej pozostałe liczby. Względny porządek w powstałych listach nie powinien ulec zmianie. Funkcja
#powinna zwrócić wskazania do obu list.

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True

def check(n):
    i = 2
    while i*i * 2 <= n:
        if is_prime(i):
            if n % (i*i) == 0 and n / (i*i) >= 2:
                return True
        i += 1
    return False

def devide(p):
    if p == None:
        return None

    run = p
    g1 = Node()
    g2 = Node()
    head1 = g1
    head2 = g2

    while run != None:
        if check(run.val):
            head1.next = Node(run.val)
            head1 = head1.next
        else:
            head2.next = Node(run.val)
            head2 = head2.next
        run = run.next

    return g1.next, g2.next

# Tworzenie przykładowej listy
p = Node(50, Node(2, Node(3, Node(32, Node(4, Node(1, Node(10)))))))

# Wywołanie funkcji
list1, list2 = devide(p)

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