dict1 = {1 : 'one', 2 : 'two', 3 : 'three'}
print("딕셔너리 dict1의 내용 : ", dict1)
#리스트를 딕셔너리로 변환
list1 = [[1, '하나'], [2, '둘'], [3,'셋']]
dict2 = dict(list1)
print("리스트 list 내용 : ", list)
print("딕셔너리 dict2 내용 : ", dict2)
#키(key)를 지정하여 값(value) 검색
print("딕셔너리 dict2의 키 3의 값 : ", dict2.get(3))

#딕셔너리 모든 요소 삭제
dict2.clear()
print("딕셔너리 dict2 내용 : ",dict2)

#keys()메소드 이용하여 사전의 모든 키 출력
print("dict1의 key : ", end=" ")
#반복문 사용하여 키 출력
for num in dict1.keys() :
    print(num, end=', ')
print()
#values() 메소드 이용하여 사전의 모든 값 출력
print("dict1의 value : ", end=" ")
#반복문 사용하여 값 출력
for alphanum in dict1.values():
    print(alphanum, end=", ")
print()
# items()메소드 이용하여 사전의 모든 키와 값 출력
for num, alphanum in dict1.items():
    print(num,"은(는) 영어로", alphanum, "이다.")