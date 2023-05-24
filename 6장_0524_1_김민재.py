# 튜플 생성
tuple1 = () # 비어있는 튜플
tuple2 = ('a', ) # 원소가 하나여도 쉼표는 필수
tuple3 = ('a', 'b', 'c')

color = ('white', 'black', 'purple', 'white', 'white', 'red', 'orange')
print("color 내용 : ", color)
print("color의 길이 : ", len(color))
print("white 개수 : ", color.count('white'))
print("orange의 위치 : ", color.index('orange'))

# 실습 예제 6-7
# 2개의 튜플을 하나의 리스트로 만들기
fruit = ('사과', '배', '딸기', '수박', '망고')
price = (2000, 4500, 8000, 10000, 5000)
list1 = []
tuple1 = ()
for i in range(len(fruit)):
    list1.append(fruit[i])
    list1.append(price[i])
    #tuple1.append(fruit[i]) 튜플은 변경이 안 됨
    #tuple1.apppend(price[1]) 튜플은 변경이 안 됨
print(list1, type(list1))
