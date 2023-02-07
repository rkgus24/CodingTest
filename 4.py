# 주민등록증의 번호가 주어지면 주민등록증 주인의 나이와 성별을 판단하여 출력하는 프로그램
num1, num2 = input().split("-")

gend = num2[0]

if gend == '1':
    age = 1900 + int(num1[0:2])
    print(2019 - age + 1, end = " ")
    print('M')
    
elif gend == '3':
    age = 2000 + int(num1[0:2])
    print(2019 - age + 1, end = " ")
    print('M')
    
elif gend == '2':
    age = 1900 + int(num1[0:2])
    print(2019 - age + 1, end = " ")
    print('W')
    
elif gend == '4':
    age = 2000 + int(num1[0:2])
    print(2019 - age + 1, end = " ")
    print('W')