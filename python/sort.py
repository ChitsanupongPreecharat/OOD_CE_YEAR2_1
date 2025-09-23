import time
start = time.time()
numbers = list(map(int,input("input : ").split()))
numbers.sort()
print(numbers)
stop = time.time()
print("time : ",stop-start)