'''
작성일 : 2023년 4월 5일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 사용자로부터 평점을 입력 받아 평점을 출력하고
        입력된 평점이 4.2 이상이라면 "해외 연수 기회 부여"를 출력하는 프로그램을 작성하시오.
'''
#평점을 실수 형태로 입력받아 score에 저장한다.
score = float(input("점수를 입력하세요 : " ))
#평점을 출력한다.
print("당신의 평점은 :", score)
#score가 4.2이상이라면
if score >= 4.2:
    #"해외 연수 기회 부여"를 출력한다.
    print("해외 연수 기회 부여")