'''
작성일 : 2023년 5월 3일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 1부터 1000까지의 정수 중 사용자가 입력한 숫자의 배수만을 더하여 출력하는 프로그램을 작성하싱. while문(for문)과 continue문을 사용하여 작성하시오.
[문제분석]
숫자 입력받기 : num_input
합계 : sum
1부터 1000까지 1씩 증가하는 num을 num_input으로 나눴을 때 나머지가 0이 아니라면 위로 돌아가기. 0이라면 sum에 더하기
'''
#for문
#1. 숫자 입력받기.
num_input = int(input())
#2. 합계 = 0
sum = 0
#3. 1부터 1000까지 반복하면서
for num in range(1, 1000+1):
    #1) num을 num_input으로 나눴을 때 나머지가 0이 아니라면
    if num % num_input != 0:
        #1 continue
        continue
    #2) 아니면
    else:
        #1 더하기
        sum += num
#4. 출력하기
print(sum)

#while문
#1. 숫자 입력받기.
num_input = int(input())
#2. 합계 = 0
num = 0
sum = 0
#3. 1부터 1000까지 반복하면서
while(num <= 1000):
    #1) num을 1씩 증가
    num += 1
    #2) num을 num_input으로 나눴을 때 나머지가 0이 아니라면
    if num % num_input != 0:
        #1 continue
        continue
    #2) 아니면
    else:
        #1 더하기
        sum += num
#4. 출력하기
print(sum)