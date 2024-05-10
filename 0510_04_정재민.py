'''

    작성일 : 2024 05 10
    작성자 : 컴공과 202495017 정재민
    설명 : 튜플 => 한 번 생성되면 그 값을 고칠 수 없는 자료형
    
'''

# 튜플 생성
colors1 = ('red', 'greem', 'blue', 'orange')

print("colors1 = ", colors1)

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print("색상 중 2, 3, 4번은? ", colors1[1:4])
print(" 색상 거꾸로 촐력 : ", colors1[::-1])

# + 연산자, + * 연산자 사용 가능
colors = colors1 + colors1
print("colors = ", colors)
print("colors1 + 10 = ", colors1 * 10)

#colors1에 black 추가
#튜플은 추가, 삭제 안됨 = 오류 발생
# colors1.append('black')


colors2 = ('red', 'greem', 'blue', 'orange', 'pink', 'white', 'white')
print("colors2 = " , colors2 )

print("색상에서 'whire' 개수는? ", colors2.count('white'))
print("색상에서 'green' 개수는? ", colors2.index('green'))

#튜플은 find사용이 안됨
# print("색상에서 'green' 개수는? ", colors2.find('green'))

# 튜플은 생성된 후에 변경 될 수 없는 자료형이어서
# 제공되는 메소드가 2개이다. count, index