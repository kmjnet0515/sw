'''
파일 저장 명 : 3장_연습문제11_김민재.py

작성일 : 2023년 3월 29일
학과 : 컴퓨터공학부
학번 : 202395006
이름 : 김민재
설명 : 연습문제 09
    홍길동의 이번달 월급 수령액을 구하시오.
'''
#본봉을 money 변수에 저장한다.
money = 3000000

#수당을 extra_money 변수에 저장한다.
extra_money = 300000

#세율을 tax_rate 변수에 저장한다.
tax_rate = 20

#total 변수에 money와 extra_money의 합을 저장한다.
total = money + extra_money

#tax 변수에 total과 tax_rate의 곱에 100을 나눈 값을 저장한다.
tax = total * tax_rate / 100

#rMoney 변수에 total-tax의 값을 저장한다.
rMoney = total - tax

#rMoney 값 출력
print("홍길동의 이번달 월급 수령액은 : {0} 원입니다.".format(rMoney))