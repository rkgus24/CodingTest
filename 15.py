# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램

n = int(input())
cnt = 0

for i in range(2, n+1):
    flag = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        cnt += 1

print(cnt)
