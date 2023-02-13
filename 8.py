# 자연수 n이 입력되면 1부터 n까지의 자연수를 종이에 적을 때 각 숫자는 몇 개 쓰였는지 구하시오
# ex) 1부터 15까지는 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5로 총 21개가 쓰였다
# 자연수 n (3 <= n <= 100,000,000)

n = int(input())
sum = 0
cnt = 1
digit = 9
res = 0

while sum + digit < n:
    sum = sum + digit
    res = res + (cnt * digit)
    cnt += 1
    digit = digit * 10
res = res+((n - sum) * cnt)
print(res)