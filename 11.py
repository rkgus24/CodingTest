# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만든다
# 만들어진 자연수와 그 자연수의 약수 개수를 출력한다

a = input()
res = 0

for i in range(len(a)):
    if a[i].isdigit():
        res = res * 10 + int(a[i])

print(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1

print(cnt)