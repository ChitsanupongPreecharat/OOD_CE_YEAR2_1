def sort(num):
    before = num[:]
    n = len(num)
    for i in range(n):
        for j in range(0,n-i-1):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    return 'Yes' if before == num else 'No'


num = list(map(int,input("Enter Input : ").split()))
print(sort(num))