'''
작성일 : 2023년 5월 24일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 7장 세트와 딕셔너리
      01. 세트
순서가 없으면서 중복을 허용하지 않는 자료구조
'''
# 실습 예제 7-1
# 랜덤으로 1~100 사이의 값을 10개 생성한 세트 2개를 만들고,
# 합집합, 교집합, 차집합을 출력하시오.
# [알고리즘]
# 1. 비어있는 세트 2개 만들기
# 2. 랜덤으로 2개의 세트에 각각 10개의 값 저장
#   랜덤, 반복하면서 (10번)
from random import randint
set1 = set()
set2 = set()
while len(set1) != 10:
    set1.add(randint(1,100))
while len(set2) != 10:
    set2.add(randint(1,100))
print("set1과 set2의 합집합 : ", set1 | set2)
print("set1과 set2의 교집합 : ", set1 & set2)
print("set1과 set2의 차집합 : ", set1 - set2)

