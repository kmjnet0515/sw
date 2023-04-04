'''
파일 저장 명 : 3장_연습문제14_김민재.py

작성일 : 2023년 4월 4일
학과 : 컴퓨터공학부
학번 : 202395006
이름 : 김민재
설명 : 연습문제 14
    5과목의 점수를 입력 받아 총점과 평균을 구하는 프로그램을 작성하시오.
'''
#kor 변수에 정수로 입력받아 저장
kor = int(input('국어 점수를 입력하시오.'))
#math 변수에 정수로 입력받아 저장
math = int(input('수학 점수를 입력하시오.'))
#soc 변수에 정수로 입력받아 저장
soc = int(input('사회 점수를 입력하시오.'))
#sci 변수에 정수로 입력받아 저장
sci = int(input('과학 점수를 입력하시오.'))
#eng 변수에 정수로 입력받아 저장
eng = int(input('영어 점수를 입력하시오.'))
#total 변수에 kor, math, soc, sci, eng의 합을 저장
total = kor + math + soc + sci + eng
#avg 변수에 total을 5로 나눈 값 저장하기
avg = total / 5
#avg를 소숫점 둘째자리까지 출력하기.
print("국어 점수 : {}점 수학 점수 : {}점 사회점수 : {}점 과학점수 : {}점 영어 점수 : {}점의 총 점은 : {}점이고 평균은 :{:.2f}점입니다".format(kor, math, soc, sci, eng, total, avg))
