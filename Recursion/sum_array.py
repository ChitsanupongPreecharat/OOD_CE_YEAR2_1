def sum(n,l):
    if n is 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return sum(n-1,l) + l[n-1]
    
l = list(map(int,input("Input: ").split()))
print(sum(len(l),l))