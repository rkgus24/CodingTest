# N명의 나이가 입력된다
# N명의 사람 중 가장 나이차이가 많이 나는 경우는 몇 살일까?

n = int(input())
a = list(map(int, input().split()))

max_val = float('-inf')
min_val = float('inf')

for i in range(n):
    if a[i] > max_val:
        max_val = a[i]
    if a[i] < min_val:
        min_val = a[i]

print(max_val - min_val)