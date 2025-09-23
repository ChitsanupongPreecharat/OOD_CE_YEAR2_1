def sort(l):
    if l == []:
        return []
    if len(l) <2:
        return l
    m = maxX(l,0)
    l.remove(m)
    return [m] + sort(l)

def maxX(l,m):
    if l == []:
        return m
    if l[0] > m:
        m = l[0]
    return maxX(l[1:],m)


Input = list(map(int,input("Enter your List : ").split(',')))
print(f"List after Sorted : {sort(Input)}")