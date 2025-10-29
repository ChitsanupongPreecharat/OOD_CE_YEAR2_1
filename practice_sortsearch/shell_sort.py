def shell_sort(l):
    d = [5,3,1]
    for inc in d:
        for i in range(inc,len(l)):
            iEle = l[i]
            for j in range(i,-1,-inc):
                if l[j-inc] > iEle and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break
    return l





num = list(map(int,input("Input num:").split()))
print(shell_sort(num))

