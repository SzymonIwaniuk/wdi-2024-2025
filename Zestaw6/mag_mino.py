class Node:
    def __init__(self, a, b, next = None):
        self.a = b
        self.b = b
        self.next = next
#XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDdd
def get_size(p):
    result = 0
    while p != None:
        result += 1
        p = p.next
    return result

def mag_mina(p):
    n = get_size(p)
    Klocek_list = [None for _ in range(n)]
    iterator = 0

    while p != None:
        Klocek_list[iterator] = p
        p = p.next
        Klocek_list[iterator].next = None
        iterator += 1

    def mag_mina_rekur(current_setup, Klocek_rest):
        nonlocal result
        if len(Klocek_rest) == 0:
            result = current_setup
            return

        for i in range(len(Klocek_rest)):
            if Klocek_rest[i]:
                klocek = Klocek_list[i]
                if Klocek_list[current_setup[-1]].b] == klocek.a
                    current_setup[current_setup_i] = klocek
                    Klocek_rest[i] = False
                    mag_mina_rekur(current_setup, curren_setup_i + 1, Klocek_rest)
