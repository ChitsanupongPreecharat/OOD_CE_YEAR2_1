def search(low,high,x):
    if high < low:
        return "Dont found"
    mid = (high + low) // 2
    if l[mid] == x:
        return f"found {x} index {mid}"
    elif x > l[mid]:
        return search(mid+1,high,x)
    else:
        return search(low,mid-1,x)
l_str,x = input("input: ").split(',')
l = sorted(list(map(int,l_str.split())))
print(search(0,len(l)-1,int(x)))
  