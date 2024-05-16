'''
    작성일 : 2024 05 16
    작성자 : 컴퓨터공확과 202495017 정재민
    설명 :  로또번호 만들기
   
   
   1 ~ 45 사이의 6개 번호
   로또 번호를 생성하고, 오름차순으로 정렬하시오.
    
'''

import random

print(" 로또 번호 생성 ")

lotto = set() # 빈 리스트 생성.


i = 0 #랜덤수 발생 횟수 저장
while True : 
    lotto.add(random.randint(1,45))
    i = i + 1
    if len(lotto) == 6 :
        break

print("이번주 로또 번호 : ", sorted(lotto))
