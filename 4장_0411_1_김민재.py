'''
작성일 : 2023년 4월 11일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 세 과목의 점수를 입력 받아 평균이 95점 이상이면
    "당신의 평균은 00.0점입니다.", "축하합니다. A+입니다"를 출력하고,
    평균 점수와 상관없이 # 감사합니다."를 출력하는 프로그램을 작성하시오.
'''
#1. 국어 점수를 입력 받아 kor에 정수로 저장
kor = int(input("국어점수를 입력하세요. : "))
#2. 영어 점수를 입력 받아 eng에 정수로 저장
eng = int(input("영어점수를 입력하세요. : "))
#3. 수학 점수를 입력 받아 math에 정수로 저장
math = int(input("수학점수를 입력하세요. : "))
#4. 평균을 구하여 변수 avg에 저장
avg = (kor + eng + math)/3
#5. 만약에, 평균이 95점 이상이라면
if avg >= 95:
#       1) 당신의 평균이 00.0점입니다.
    print("당신의 평균이 {:.1f}점입니다.".format(avg))
#       2)축하합니다. A+입니다.를 출력한다.
    print("축하합니다. A+입니다.")
#6. 조건과 상관없이 감사합니다를 출력한다.
print("감사합니다.")