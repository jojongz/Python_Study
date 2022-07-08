# 리스트 추가 방법에 따른 시간 테스트
import time
SIZE = 50000

start_time = time.time()
myList = []
for i in range(SIZE):
    myList = myList + [i*i] # 대입은 재설정
print("수행시간 =", time.time() - start_time)

start_time = time.time()
myList = []
for i in range(SIZE):
    myList.append(i*i)
print("수행시간 =", time.time() - start_time)