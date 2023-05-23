from random import randint
#다중 리스트
num = [[11,12,13], [21,22,23], [31,32,33,34], [41,42]]
# 리스트 내의 각각 리스트의 합계를 계산하여 출력
total = 0
for i in range(len(num)):
    total += sum(num[i])
print(total)
total = 0
for i in range(len(num)):
    for j in range(len(num[i])):
        total += num[i][j]

print(total)

#실습 예제 6-5
#1~100사이의 랜덤 수를 발생시켜 리스트에 저장하고, 합계, 최대값, 최소값을 출력하시오.
#오름차순으로 정렬도 하시오.
list = []
for i in range(1,11):
    list.append(randint(1,100))
print("생성된 리스트 : {}, 합계는 {}, 최대값은 : {}, 최소값은 : {}, 오름차순 정렬은 : {}".format(list, sum(list), max(list), min(list), sorted(list)))

