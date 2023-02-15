# 현수네 반은 학생이 N명 있음
# 선생님은 각 학생들에게 숫자가 적힌 카드를 줌
# 각 학생들은 1부터 자기 카드에 적힌 숫자까지의 합을 구하는 퀴즈임
# 학생들의 답이 맞는지 확인하는 프로그램

n = int(input())
for i in range(n):
    m, ans = map(int, input().split())
    sum = 0
    for j in range(1, m+1):
        sum += j
    if ans == sum:
        print("YES")
    else:
        print("NO")