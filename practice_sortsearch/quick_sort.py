def quick_sort(l):
    q_sort(l,0,len(l)-1)
    return l

def q_sort(l,left,right):
    if left < right:
        p = sartition(l,left,right)
        q_sort(l,left,p-1)
        q_sort(l,p+1,right)
    return l

def sartition(l,left,right):
    if left == right -1:
        if l[left] > l[right]:
            l[left],l[right] = l[right],l[left]
        return left
    pivot = l[left]
    i,j = left+1,right
    while i < j:
        while i <right and l[i] <= pivot:
            i+=1
        while j > left and l[j] >=pivot:
            j-=1
        if i<j:
            l[i],l[j] = l[j],l[i]
    if left is not j:
        l[left],l[j] = l[j],l[left]
    return j




num = list(map(int,input("Input num:").split()))
print(quick_sort(num))





