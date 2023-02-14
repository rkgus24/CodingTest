# 자연수 N이 입력되면 1부터 N까지의 각 숫자들의 약수의 개수를 출력하는 프로그램을 작성하라.

n = int(input())
cnt = [0] * (n+1)

for i in range(1, n+1):
    for j in range(i, n+1, i):
        cnt[j] += 1

for i in range(1, n+1):
    print(cnt[i], end=" ")