# 자연수 N이 입력되면 1부터 N까지의 수 중 M의 배수합을 출력하는 프로그램
n, m = map(int, input().split())
result = 0

for i in range(1, n + 1):
	if (i % m == 0):
		result += i
print(result)