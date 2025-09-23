import math
Input = list(map(int,input("INPUT: ").split()))

mean = sum(Input)/ len(Input)

result = 0 
for i in Input:
    result += (i-mean)**2

print(f"ความแปรปรวน: {result/len(Input)}")
print(f"ส่วนเบี่ยงเบนมาตาฐาน: { math.sqrt( result/len(Input))}")