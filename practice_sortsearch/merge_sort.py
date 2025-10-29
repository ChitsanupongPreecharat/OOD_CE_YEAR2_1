def merge_sort(l,left,right):
    mid = (left + right) // 2
    if left < right:
        merge_sort(l,left,mid)
        merge_sort(l,mid+1,right)
        merge(l,left,mid+1,right)
    return l

def merge(l,left,right,rightEnd):
    start = left
    leftEnd = right-1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd:
        result.append(l[left])
        left += 1
    while right <= rightEnd:
        result.append(l[right])
        right += 1
    
    for ele in result:
        l[start]  = ele
        start += 1
        if start > rightEnd:
            break





num = list(map(int,input("Input num:").split()))
print(merge_sort(num,0,len(num)-1))

