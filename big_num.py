n, m, k = map(int, input().split())
input_list = list(map(int, input().split()))
result = 0
count = 0

li = sorted(input_list, reverse=True)

for _ in range(m):
    if (count+1)%k==0:
        result += li[1]
    else:
        result += li[0]
    count += 1
print(result)
