def sort(n):
    for i in range(1,len(n)):
        iEle = n[i]
        for j in range(i,-1,-1):
            if j > 0 and n[j-1] > iEle:
                n[j] = n[j-1] 
            else:
                n[j] = iEle
                break
    return n




num = list(map(int,input("Enter Input : ").split()))
print(sort(num))