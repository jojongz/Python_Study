# 튜플 / 셋

# 튜플 - 변경 불가 ()
fruits = ("apple", "banana", "grape")
print(fruits)

print(fruits[0])
for f in fruits:
    print(f, end = " ")

# 튜플을 리스트로
myTuple = (1,2,3,4)
myList = list(myTuple)
print()
print(myList)


# 셋 - 중복불가 {}
numbers = {1, 2, 3}
print("set =", numbers)

numbers = set([1,2,2,3,4,5,5]) # - 중복을 허락하지 않는다.
print("set =", numbers)

# 셋 함축 연산
aList = [1,2,3,4,5,1,2]
result = {x for x in aList if x % 2 == 0}
print("x % 2 =", result)

# 셋 - 교집합 / 합집합 / 차집합
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "kiwi"}
C = A & B
D = A | B
E = A - B
print("교집합 =", C)
print("합집합 =", D)
print("차집합 =", E)






