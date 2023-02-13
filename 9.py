# 첫 줄에 자연수가 입력되면 자릿수의 곱을 구하여 출력하는 프로그램

ch = [0] * 10
a = input()
max_val = -2147000000
res = 0
for i in range(len(a)):
    digit = int(a[i])
    ch[digit] += 1
for i in range(10):
    if ch[i] >= max_val:
        max_val = ch[i]
        res = i
print(res)