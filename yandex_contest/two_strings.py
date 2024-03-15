import math
n = int(input())
for _ in range(0, n):
    length = int(input())
    f = [int(i) for i in input()]
    s = [int(i) for i in input()]
    comb_1 = False
    comb_2 = False
    for i in range(0, length):
        if f[i] == s[i]:
            comb_1 = True
        else:
            comb_2 = True
    if comb_1 & comb_2:
        print('NO')
        continue
    else:
        l = 0
        r = 0
        operations = []
        i = 0
        k = 0
        while i < length:
            if i == 0:
                l = i
            else:
                if f[i] == 0 and f[i-1] != 0:
                    l = i
            if i == length - 1:
                r = i
                operations.append((l, r))
            else:
                if f[i] == 0 and f[i + 1] != 0:
                    r = i
                    operations.append((l, r))
            i += 1


        # while math.prod(f) != 1: # O(n)
        #     l = f.index(0) # амортизированная O(1)
        #     r = l
        #     f[l] = 1
        #     operations.append((l + 1, r + 1)) # суммарное кол-во операций |кол-во нулей| * O(n)
        if len(operations) % 2 == 0: 
            if comb_1: # 111 / 111
                operations.append((1, 1))
                operations.append((2, length))
            else: # 111 / 000
                operations.append((1, length))
        else:
            if comb_2: # 111 / 111
                operations.append((1, 1))
                operations.append((2, length))
            else: # 111 / 000
                operations.append((1, length))
    print('YES')
    print(len(operations))
    for l, r in operations:
        print(l, r)