#Zadanie 166. Dwie osoby otrzymały ten sam ciąg liter. Każda osoba pocięła go na kawałki i pomieszała.
#Proszę napisać program, który otrzymując dwa zbiory kawałków odtwarza napis początkowy jeżeli odtwo-
#rzenie to jest jednoznaczne lub stwierdza brak możliwości jednoznacznego odtworzenia napisu. Na przykład
#dla zbiorów (1) ab,cde,cfed,fab (2) abc,abc,def,fed odtworzony napis to: abcdefabcfed

def napisy(Z1,Z2):
    l = len(Z1)
    znalezione = []
    def rek(Z1,Z2,n1,n2,used1,used2,index,l):
        nonlocal znalezione

        if index  == l:
            if n1 == n2:
                znalezione += [n1]
            else:
                return

        for i in range(l):
            sn1 = Z1[i]
            if not used1[i]:
                for j in range(l):
                    sn2 = Z2[j]
                    if not used2[j]:
                        used1[i] = True
                        used2[j] = True
                        rek(Z1,Z2,n1 + sn1,n2 + sn2,used1,used2,index + 1,l)

                        used2[j] = False
            used1[i] = False

    rek(Z1,Z2,'','',[False] * l,[False] * l,0,l)
    if len(znalezione) != 2:
        return False
    else:
        return znalezione[0]

Z1 = ['ab','cde','cfed','fab']
Z2 = ['abc','abc','def','fed']

print(napisy(Z1,Z2))
