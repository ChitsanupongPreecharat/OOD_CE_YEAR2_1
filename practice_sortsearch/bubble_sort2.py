def bubble_sort(num):
    for last in range(len(num)-1,0,-1):
        swap = False
        for i in range(last):
            if num[i] > num[i+1]:
                num[i],num[i+1] = num[i+1],num[i]
                swap = True
        if not swap:
            break
    return num



num = list(map(int,input("Enter Input : ").split()))
before = num[:]
after = bubble_sort(num)
print('Yes' if before == after else 'No')