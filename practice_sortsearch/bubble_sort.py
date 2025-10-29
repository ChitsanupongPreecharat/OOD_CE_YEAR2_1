def bubble_sort(l):
    for last in range(len(l)-1,0,-1):
        swap = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                swap = True
        if not swap:
            break
    return l




num = list(map(int,input("Input num:").split()))
print(bubble_sort(num))