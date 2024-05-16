'''
    작성일 : 2024 05 16
    작성자 : 컴퓨터공확과 202495017 정재민
    설명 :세트 : 중복을 허용하지 않는다.
'''
# 빈세트(집합) 생성
num = set()

# 3개의 숫자로 이루어진 세트
num1 = {2,1,3}
print("숫자 3갫 이루어진 세트 : ", num1) # 출력 순서와 저장 순서가 다르다.

#리스트를 세트로 생성
num2 = set([1,2,3,1,2])
print("리스트를 세트로 생성 : ", num2) # 세트는 중복을 허용하지 않는다

text1 = set("abcdefa")
print("문자열을 세트로 생성 : ", text1) #a는 1개만 출력된다. 출력 순서가 다르다

num3 = {2, 1, 3}
#1이 num3에 있는가?
if num in num3 :
    print("1이 세트에 있습니다. ")
    
num4 = {9,3,11,2,1,3,5,6,2}
print("num4 = ", num4)

for num in num4 :
    print(num, end =' ')
    
print()
num4.add(100)
print("100추가 : ", num4 )

for num in sorted(num4) :
    print(num, end ='')


print()

#삭제하기
num.remove(100)
print("100삭제 : ", num4)

#세트의 연산
a = {1,2,3}
b = {1,2,3}

print(" a == b", a == b)

num5 ={1,5,4,3,7,4}
print("num5 = ", num5)

print("num4의 길이 : ", len(num)) # 중복을 제외하고 길이 찾아 줌. 5개

print("num5에서 최대값 : ", max(num5))
print("num5에서 최소값 : ", min(num5))
print("num5에서  합계 : ", sum(num5))

A = {1,2,3}
B = {3,4,5}

#합집합
#합집합 연산 => |
print("A | B = ", A | B)
#합집합 매소드 union()
print("A | B = ", A.union(B))

#교집합
#교집합 연산 => &
print("A & B = ", A & B)
#교집합 메소드 => intersection
print("A & B = ", A.intersection(B))

#차집합
#차집합 연산 =>
print("A - B = ", A - B)

#차집합 매소드 => difference()
print("A - B = ", A.difference(B))

#대칭 차집합
print("A ^ B = ", A ^ B)