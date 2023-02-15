# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램

def reverse(x):
    res = 0
    while x > 0:
        tmp = x % 10
        res = res * 10 + tmp
        x = x // 10
    return res

def is_prime(x):
    if x == 1:
        return False
    flag = True
    for i in range(2, x):
        if x % i == 0:
            flag = False
            break
    return flag
asd = int(input())
num = list(map(int, input().split()))

for i in num:
    tmp = reverse(i)
    if is_prime(tmp):
        print(tmp, end=' ')
