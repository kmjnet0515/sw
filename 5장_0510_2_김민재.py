'''

작성일 : 2023년 5월 10일
학과 : 컴퓨터공학부
학번 : 202395006
이름 : 김민재
문제 : 2단부터 9단까지 구구단을 출력하시오. 단, 구구단의 결과가 짝수인 경우만 출력하시오.
    while문과 for문으로 작성하고, 비교하시오.
'''
# 1. for 문으로 dan을 2~9까지 반복하면서
#   1) for문으로 num을 1~9까지 반복하면서
#       〔1〕만약 (dan * num) % 2 == 0 이라면 
#           [1] 출력

for dan in range(2,10) :
    print('=={}단==' .format(dan),)
    for num in range(1,10) : 
        if (dan * num) % 2 == 0 :
            print('{} * {} = {}' .format(dan, num, dan * num))
        
print('============while문=============')

dan = 2

while dan <= 9 :
    print('=={}단==' .format(dan),)
    num = 1
    while num <= 9 :
        if (dan * num) % 2 == 0 :
            print('{} * {} = {}' .format(dan, num, dan * num))
        num = num + 1
    dan = dan + 1