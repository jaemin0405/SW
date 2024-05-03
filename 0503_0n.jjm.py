'''
 
giveName = name[1:3]
print("name[1:3] :", giveName)

print("city[2:] :", city[2:])


print("num[1:3] :", num[1:3])
print("num[::2]: ", num[::2])

print("num[-10,10] : ", num[-10:10])
'''



'''
3.연결 : + 연산자를 사용하여 두 개의 자료를 연결한다.
            새로운 시퀸스 자료형을 만든다
자료형 + 자료형

'''

text1 = ' I Like'

text2 = text1 + 'Python Language'
print("text + 문자열 = ", text2)

num1 = (1,2,3,4,5)
num2 = (6,7,8,9,)
num = num1 + num2
print("num1 + num2 = ", num)

# City(리스트) + num1(튜플)
# result = city + num1 # 오류 발생. 서로 다른 자료형은 합칠 수 없다.
# print("city + num1 = ", result)

'''
4. 반복 : + 연산자 사용한다.
        시퀸스 자료형을 원하는 만큼 반복시킬 수 있는 기능
자료형 + 반복횟수

'''
# 튜플 생성
language = ('C', 'JAVA', 'Python')
# language를 3번 반복하여 변수에 저장
languages  = language * 3
print("languages : ", languages)

feel = 'happy . ' *10 #문자열 10번반복
print("feel : ", feel)

contury = ['대한민국'] * 10
print("century : ", contury)

'''


5. 멤버 유무 검사 : 시퀸스 자료형에 특정 잘가 있는지 알려주는 기능
자료 in 자료형 
'''
color = ['red', 'green', 'blue', 'yellow', ]
print("리스트에 'black'이 있나요?" , 'black' in color)
print("리스트에 'red'가 있나요?" , 'red' in color)

text3 = 'Python'
print("t가 문자열에 있나요? ", 't' in text3)
print("P가 문자열에 있나요? ", 'P' in text3)
print("P가 문자열에 있나요? ", 'p' in text3)

#in 연산자는 for 반복문에 효율적으로 사용
for i in text3 :  # text3 안에 있는 문자를 하나씩 i 변수에 넣어서 반복
    print(i) 
    
    '''
    
6. 길이 정보 : 내장 함수 len() 함수 사용한다.
                시퀸스 자료형의 길이를 알 수 있다.
len(자료형)
'''
# 문자열 text2의 길이 
print("text2의 길이 : ", len(text2)) # 22=> 띄어쓰기도 포함
# 리스트 city의 길이
print("city의 길이 : ", len(city))
