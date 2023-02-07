# 자연수 N이 주어지면 N의 진약수의 합을 수식과 함께 출력하는 프로그램
n = int(input())
num = 1

print("1", end = " ")
for i in range(2, n):
    if (n % i == 0):
        num += i
        print(f"+ {i}", end = " ")
print(f"= {num}")