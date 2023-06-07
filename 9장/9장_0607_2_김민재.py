'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 9장 함수와 모듈
'''
# 랜덤함수 모듈
from random import randint
#함수명 : make_question
def make_question():
    #1~40번까지 무작위수를 num1에 저장
    num1 = randint(1,40)
    #1~20번까지 무작위수를 num1에 저장
    num2 = randint(1,20)
    #1~3번까지 무작위수를 op에 저장
    op = randint(1,3)
    #문제 변수에 첫 번째 수를 문자열로 변환 후 저장
    que = str(num1)
    #연산자 변수가 1일 때
    if op == 1:
        # 문제 변수에 '+'문자 추가
        que = que + '+'
    #연산자 변수가 1일 때
    if op == 2:
        # 문제 변수에 '-'문자 추가
        que = que + '-'
    #연산자 변수가 1일 때
    if op == 3:
        # 문제 변수에 '*'문자 추가
        que = que + '*'
    #문제 변수에 두 번쨰 수를 문자열로 변환 후 저장
    que = que + str(num2)
    #문제 변수를 반환한다.
    return que
#정답, 오답 개수 변수 초기화
r_ans = 0
w_ans = 0
#5번 반복함녀서
for i in range(5):
    #que 변수에 함수의 반환값(문제)를 저장
    que = make_question()
    #줄 바꿈 없이 문제를 출력한다.
    print(que, end='')
    #문제 뒤에 =을 출력하고 정수형으로 값을 입력받는다
    result = int(input('='))
    # eval('문자열')은 그 값을 계산해주는 함수이다. 문제의 값과 입력받은 값이 같다면
    if eval(que) == result :
        #정답입니다. 출력
        print("정답입니다. ")
        #정답 변수에 1추가
        r_ans += 1
    #아니면
    else:
        #오답입니다. 출력
        print("오답입니다.")
        #오답 변수에 1추가
        w_ans += 1
#총 정답 개수와 오답 개수 출력
print('정답' , r_ans, '오답', w_ans)
#오답 변수가 0이면
if w_ans == 0:
    #당신은 천재입니다 출력
    print('당신은 천재입니다.')