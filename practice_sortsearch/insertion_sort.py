def insertion_sort(l):
    for i in range(1,len(l)):
        iEle = l[i]
        for j in range(i,-1,-1):
            if j > 0 and l[j-1] > iEle:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
    return l




num = list(map(int,input("Input num:").split()))
print(insertion_sort(num))