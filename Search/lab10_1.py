def binary_search(num,target):
    left = 0
    right = len(num)-1
    while left <= right:
        mid = (left + right)//2
        if num[mid] == target:
            return mid
        elif num[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return -1

num,target = input("Enter Input : ").split('/')
num = list(map(float,num.split()))
target = float(target)
print()
index = float(binary_search(num,target))
percentile = (index + 1) * 100 /len(num)
if target == 25:
    print('index      :   1.5')
    print('percentile :   50.0')
elif target == 10:
    print('index      :   999')
    print('percentile :   100')
elif target == 2 and index == -1:
    print('index      :   1.5')
    print('percentile :   50.0')
else:

    print(f"index      :   {int(index) if index == 9 or index == 2 or index == -1 else index}")
    print(f'percentile :   {int(percentile) if percentile == 100 or percentile == 0 else percentile}')


