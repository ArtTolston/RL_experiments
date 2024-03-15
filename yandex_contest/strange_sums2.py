#base prefix sum realization
#Strange sums

n, num = list(map( int , input().split(' ')))

flag = False

arr = list(map(int, input().split(' ')))


arr_length = len(arr)

d = {}

prefix_strange_sum_arr_length = arr_length + 1
prefix_strange_sum_arr = [0 for _ in range(prefix_strange_sum_arr_length)]

for i in range(1, prefix_strange_sum_arr_length):
    prefix_strange_sum_arr[i] = prefix_strange_sum_arr[i - 1] + (-1) ** (i - 1) * arr[i - 1]
    if prefix_strange_sum_arr[i] not in d:
        d[prefix_strange_sum_arr[i]] = []
    d[prefix_strange_sum_arr[i]].append(i)
    

for i in range(prefix_strange_sum_arr_length):
    new_prefix = 0
    if i % 2 == 0:
        new_prefix = prefix_strange_sum_arr[i] + num
    else:
        new_prefix = prefix_strange_sum_arr[i] - num
    if new_prefix in d:
        indexes = d[new_prefix]
        indexes = [j - i for j in indexes]
        ind = max(indexes)
        if ind > 0:
            flag = True
            break
if flag:
    print('YES')
else:
    print('NO')
       