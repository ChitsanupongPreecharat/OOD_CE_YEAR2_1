def sum(l):
    n = len(l)
    if n == 0:
        return 0 
    elif n == 1:
        return l[0]
    else:
        return l[0] + sum(l[1:])
l = list(map(int,input("input : ").split()))
print(sum(l))
print(l)