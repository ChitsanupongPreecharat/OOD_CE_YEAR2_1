def bubble_sort(n):
    for last in range(len(n)-1,0,-1):
        swap = False
        for i in range(last):
            if n[i] > n[i+1]:
                n[i],n[i+1] = n[i+1],n[i]
                swap = True
        if not swap:
            break
    return n

num = list(map(int,input("Enter Input : ").split()))
before = num[:]
after = bubble_sort(num)
print("Yes" if before == after else "No" )
