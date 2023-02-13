# 괄호가 입력된 후 올바른 괄호면 YES, 올바른 괄호가 아니면 NO를 출력한다

a = input()
b = 0

for i in a:
    if i == '(':
        b += 1
    elif i == ')':
        b -= 1
    if b < 0:
        break

if b == 0:
    print("YES")
else:
    print("NO")