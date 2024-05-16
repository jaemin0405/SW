'''
    작성일 : 2024 05 16
    작성자 : 컴퓨터공확과 202495017 정재민
    설명 : 아래와 같이 두 개의 튜플을 생성하고, 튜플로부터 하나의 리스트를 생성하는 프로그램을 생성하시오.
    

    시쿼스 자료형 => 순서가 있다. 0번지 부터이다.
    
'''
# 과일 이름과 과일 가격 튜플로 각각 생성
fruit = ('사과', '배', '파인애플', '포도')
price = (5000, 7000, 4500, 6000)

# 저장할 빈 리스트 생성
# fp_list = []
fp_list = []

for i in range(len(fruit)) : # 튜플의 길이만큼 반복하면서 
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    #fp_tuple.append(fruit[i]) #튜플은 변경이 불가능 하다. 추가 x
print("과일 목록 : ", fruit)
print("과일 가격 : ", price)
print("과일별 가격 리스트 : ", fp_list)