# 자연수 A, B가 주어지면 A부터 B까지의 합을 수식과 함께 출력하세요.
a, b = map(int, input().split())
result = 0

for i in range(a, b):
    result += i
    print(f'{i} + ', end='')

print(f"{b} =", end = " ") # 7 +가 되는 것을 방지하고자 함
result += b
print(result)