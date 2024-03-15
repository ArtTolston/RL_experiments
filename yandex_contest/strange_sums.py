n, num = list(map( int , input().split(' ')))

flag = False

arr = list(map(int, input().split(' ')))

init_sums = [0 for _ in range(0, n + 1)]
init_sums[0] = arr[0]

for i in range(1, n + 1):
    s = init_sums[i - 1]
    if i != n:
        init_sums[i] = s + (-1)**i * arr[i]
    
    for j in range(0, n - i):
        if s == num:
            flag = True
            
        else:
            s = -1*(s - arr[j]) + (-1)**(i - 1) * arr[j + i]
if flag:
    print('YES')
else:
    print('NO')
