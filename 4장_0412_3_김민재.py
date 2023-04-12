'''
작성일 : 2023년 4월 12일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 한 과목이 점수를 입력 받아 점수에 따라 학점을 부여하는 프로그램을 작성하시오.
      A학점 : 90~100
      B학점 : 80~89
      C학점 : 70~79
      D학점 : 60~69
      F학점 : 0~59
'''
#1. 점수를 입력받아 정수 형태로 변수 score에 저장
score = int(input("점수를 입력하세요. : "))
#2. 만약 score >= 90 and socre <= 100 :
if score >= 90 and score <= 100 :
#   1)"A입니다."출력
    print("점수{}점은 A학점입니다.".format(score))
#3. 만약 score >= 80 and socre < 90 :
elif score >= 80 and score < 90 :
#   1)"B입니다."출력
    print("점수{}점은 B학점입니다.".format(score))
#4. 만약 score >= 70 and socre < 80 :
elif score >= 70 and score < 80 :
#   1)"C입니다."출력
    print("점수{}점은 C학점입니다.".format(score))
#5. 만약 score >= 60 and socre < 70 :
elif score >= 60 and score < 70 :
#   1)"D입니다."출력
    print("점수{}점은 D학점입니다.".format(score))
#6. 아니면
else :
#   1)"F입니다."출력
    print("점수{}점은 F학점입니다.".format(score))