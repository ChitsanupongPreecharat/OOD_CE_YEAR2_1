def sum(l,front,tail):
    if front > tail:
        return 0
    elif front == tail:
        return l[tail]
    else:
        return l[front] + sum(l,front+1,tail)
list_ = list(map(int,input("INput list: ").split()))
print(sum(list_,0,len(list_)-1))