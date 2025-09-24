def quicksort(l):
    if len(l) <= 1:
        return l
    pivot = l[-1]
    left = [x for x in l[:-1] if x <= pivot ]
    right = [x for x in l[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

num = list(map(int,input("Input num: ").split()))
print(quicksort(num))