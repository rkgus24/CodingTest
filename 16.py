# Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 한다 예를들어 AbaAeCe와 baeeACA는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), b(1), C(1), e(2)로 아ㄹ파벳과 그 개수가 모두 일치한다
# 즉 어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 한다 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램

a = [0] * 60
b = [0] * 60

str1 = input()
for i in range(len(str1)):
    if str1[i].isupper():
        a[ord(str1[i]) - 64] += 1
    else:
        a[ord(str1[i]) - 70] += 1

str2 = input()
for i in range(len(str2)):
    if str2[i].isupper():
        b[ord(str2[i]) - 64] += 1
    else:
        b[ord(str2[i]) - 70] += 1

if a == b:
    print("YES")
else:
    print("NO")
