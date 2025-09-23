def combination(arr,r):
    result = []
    def backtrack(start,path):
        if len(path) == r:
            result.append(path[:])
        for i in range(start,len(arr)):
            if arr[i] != 0:
                path.append(arr[i])
                backtrack(i+1,path)
                path.pop()



    backtrack(0,[])
    return result 

num = list(map(int,input("Enter Input: ").split()))
awswer = []
for n in range(len(num),0,-1):
    awswer.extend(combination(num,n))

for i in range(len(awswer)):
    for j in range(len(awswer)-1-i):
        a = awswer[j][0]
        b = awswer[j+1][0]
        if num.index(a) > num.index(b) :
            awswer[j],awswer[j+1]=awswer[j+1],awswer[j]
print(f"Output: {awswer}")