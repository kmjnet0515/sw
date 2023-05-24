'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 7장 세트와 딕셔너리
      01. 세트
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
# 랜덤으로 로또 번호 추첨하기
# 1. 로또 번호 저장 할 세트 만들기
# 2. 6번 반복하면서
#   1) 1~45 사이의 값을 세트 변수에 추가
# 3. 로또 번호 출력
from random import randint
numbers = set()
while len(numbers) != 6:
    numbers.add(randint(1,45))
for i in range(len(numbers)):
    print("{}번째 숫자는 : ".format(i+1), numbers.pop())