'''
    작성일 : 2024년 3월 22일
    작성자 : 컴퓨터 공학과 202495017 정재민
    설명 : 밑변과 높이를 입력받아 삼각형의 넓이를 계산하는 프로그램을 작성하시오. 
    
    [문제분석]
        삼각형의 넓이 = (밑변 * 높이) / 2
        밑변, 높이를 입력 받는다.
        ⭐⭐⭐⭐⭐입력 받는 길이는 반드시 정수로 변환해야 한다.
        
        필요한 변수 => bottom(밑변), height(높이), area(넓이)
    [알고리즘]
        1. 밑변을 입력받아 정수로 변환하여 변수에 저장한다. 
        2. 높이를 입력받아 정수로 변환하여 변수에 저장한다.
        3. 삼각형의 넓이를 계산한다.
        4. 삼각형의 넓이를 출력한다.
'''

# 1. 밑변과 높이를 입력 받는다.
bottom = int(input("밑변을 입력하시오 :"))
height = int(input("높이를 입력하시오 :"))

# 3.삼각형의 넓이를 계산한다
area = (bottom * height)/2

# 4. 삼각형의 넓이를 출력한다
# 소수 3자리까지 출력 하시오
print(f"이 삼각형의 넓이는 {area:.3f} 입니다")

