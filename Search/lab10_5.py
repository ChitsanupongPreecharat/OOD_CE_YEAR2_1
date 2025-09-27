def min_capacity(weight,k):
    low,high = max(weight),sum(weight)
    while low < high:
        mid = (low + high) //2
        if can_partition(weight,k,mid):
            high = mid
        else:
            low = mid+1
    return low

def can_partition(weight,k,capacity):
    box_used = 1
    current = 0
    for w in weight:
        if current + w <= capacity:
            current += w
        else:
            box_used += 1
            current = w
            if box_used > k:
                return False
    return True

weight,k = input("Enter Input : ").split('/')
weight = list(map(int,weight.split()))
# weight = [w*i for w,i in enumerate(weight)]
print(f'Minimum weigth for {k} box(es) = {min_capacity(weight,int(k))}')