def binary_search(n,target):
    left = 0
    right = len(n)-1
    while left <= right:
        mid = (left + right) // 2
        if n[mid] == target:
            return mid
        elif n[mid] < target:
            left = mid+1
        else:
            rihgt = mid-1
    return -1


num,target = input("Enter Input : ").split('/')
num = list(map(int,num.split()))
index = binary_search(num,int(target))
print(f"index      :   {index}")
print(f"percentile :   {(index+1) * 100 /len(num)}")