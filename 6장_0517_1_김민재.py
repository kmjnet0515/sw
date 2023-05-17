'''
작성일 : 2023년 5월 17일
학과 : 컴퓨터공학과
학번 : 202395006
이름 : 김민재
설명 : 6장 시퀸스 자료형
      02. 시퀸스 자료형의 연산
'''
# 1. 인덱싱 - 순차적인 자료구조에 인덱스 값을 가지고 접근
# 문자열 저장 변수
name = '김민재'
# name 에 저장된 0번지 값 출력
print("name[0] - 인덱싱 결과 : ", name[0])

# 리스트 저장 변수
city = ['부산광역시', 100, '부산광역시', 200]
# 리스트의 뒤에서 2번쨰 내용 출력
print("city[-2] - 인덱싱 결과 : ", city[-2])

# 뒤에서 4번째 내용을 '서울시'로 변경하여 city에 저장
print("city - 인덱싱 결과(서울시로 변경 전) : ", city)
city[-4] = '서울시'
print("city - 인덱싱 결과(서울시로 변경 후) : ", city)

# 5개의 정수를 튜플로 생성
num = (1,2,3,4,5)
#print("num[5] - 인덱싱 결과 : ",num[5]) 튜플 범위를 벗어남

# 2. 슬라이싱 - 인덱스를 사용하여 자료형의 특정 부분을 지정
givename = name[1:3] #1부터 3앞까지 추출 name[a:b] (a <= ? < b)
print("name[1:3] - 슬라이싱 결과 : ", givename)
# city 0번부터 출력
print("city[0:] - 슬라이싱 결과 : ", city[0:])
# city 2번부터 출력
print("city[2:] - 슬라이싱 결과 : ", city[2:])
# num 변수의 처음부터 끝까지 2씩 증가하면서 출력
print("num[::2] - 슬라이싱 결과 : ", num[::2])
# 범위를 벗어나면 출력 가능한 내용 모두 출력
print("num[-10:10] - 슬라이싱 결과 : ", num[-10:10])

# 3. 연결 - '+' 연산자를 사용하여 두 개의 자료를 연결하여 새로운 시퀸스 자료형을 만든다.
# 튜플 생성
num1 = (1,2,3,4,5)
num2 = (6,7,8,9)
result = num1 + num2
print("연결 결과(result) : ", result)

# 리스트 생성
city = ['서울시', '부산시', '제주도']
# result = num1 + city 숫자와 문자는 연결되지 않는다.
# print("연결 결과(result) : ", result) 오류발생 : 서로 다른 자료형은 합칠 수 없다.

text1 = 'I like '
text2 = text1 + 'python'
print("연결결과(text2) :", text2)

# 4. 반복 - '*'연산자를 사용하여 원하는만큼 반복
# 튜플 생성
language = ('Python', 'Java', 'C')
print("language 튜플 내용 3번 반복 : ", language * 3)
#Python 문자를 10번 반보갛여 출력
print("Python 10번 반복 : ", 'python '*10)

# 5. 멤버 유무 검사 - True, False로 출력
# 시퀸스 자료형에 특정 자료가 있는지 알려주는 기능 - in 연산자
# 리스트 생성
color = ['red', 'green', 'blue', 'white']
print("color에 \'black\'이 있나요? ", 'black' in  color)
language = 'Python'
print("language에 \'t\'가 있나요? ", 't' in language)
print("language에 \'p\'가 있나요? ", 'p' in language)

# 6. 길이 정보 - len() 함수
print("color : ", color)
print("color의 길이는 : ", len(color))
print("text2 : ", text2)
print("text2의 길이는 : ", len(text2))