
# def ciecia(word):
#     samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
#     n = len(word)
#     t = [word[i] for i in range(n)]
#     cnt = 0
#     def rek(t,T,i,n):
#         nonlocal cnt
#         if i == n:
#             if len(T) > 1:
#                 for part in T:
#                     flag = False
#                     for letter in part:
#                         if letter in samogloski:
#                             flag = True
#                     if not flag:
#                         return
#                 cnt += 1
#         else:
#             t1 = T + [t[i]]
#             if T:
#                 T[-1] += t[i]
#
#             rek(t, t1, i+1, n)
#             rek(t, T, i+1, n)
#
#     rek(t,[],0,n)
#     return cnt
#
# print(ciecia('alicja'))
def zad167(word):
    T = ['a', 'e', 'i', 'y', 'o', 'u']

    def rek(i, flag, word):
        if word[i] in T:
            if flag:
                return 0
            else:
                flag = True
        if i == len(word) - 1:
            if flag:
                return 1
            else:
                return 0
        if flag:
            return rek(i + 1, flag, word) + rek(i + 1, False, word)
        else:
            return rek(i + 1, flag, word)

    return rek(0, False, word)


print(zad167("abba"))



