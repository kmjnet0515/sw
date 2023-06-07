'''
작성일 : 2023년 5월 31일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 9장 함수와 모듈
'''
#함수 생성
def hap(a,b):
    result = a + b
    return result
print("함수 결과 : {}".format(hap(1,2)))
def print_hello():
    for i in range(3):
        print("안녕하세요.")
    
print("== 함수호출 1==")
#안녕하세요 3번 출력하는 함수 호출
print_hello()

print("--------------------------------")

def print_n_time(value, n):
    for i in range(n):
        print(value * (i+1))
print_n_time(5,5)
print_n_time("hi~", 5)

#반지름을 입력 받아 원의 넓이를 구하시오.
def area_of_circle(radius):
    pi = 3.14
    area = radius**2 * pi
    return area
print("원의 넓이는 : {}입니다.".format(area_of_circle(int(input('반지름을 입력해주세요. : ')))))

# 두 정수를 입력받아 큰 수를 출력하시오. 
# 큰 수를 판별하여 결과를 돌려주는 함수를 작성하시오.

def max_num(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print("두 수 중 큰 숫자는 {}입니다.".format(max_num(int(input('첫 번째 정수를 입력하세요. : ')), int(input('두 번째 정수를 입력하세요. : ')))))