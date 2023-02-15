# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램

def digit_sum(x):
    sum = 0
    while x > 0:
        tmp = x % 10
        sum = sum + tmp
        x = x // 10
    return sum

n = int(input())
m = list(map(int, input().split()))
max = -2147000000
res = 0

for i in m:
    sum = digit_sum(i)
    if sum > max:
        max = sum
        res = i
    elif sum == max:
        if i > res:
            res = i

print(res)