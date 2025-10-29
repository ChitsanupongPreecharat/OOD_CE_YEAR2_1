def min_capacity(item,box):
    low,hight = max(item),sum(item)
    while low < hight:
        mid = (low+hight)//2
        if can_capacity(item,box,mid):
            hight = mid 
        else:
            low = mid +1
    return low

def can_capacity(item,box,mid):
    box_use = 1
    current = 0
    for i in item:
        if current + i <= mid:
            current += i
        else:
            box_use+=1
            current = i
            if box_use > box:
                return False
    return True
item,box = input("Enter Input : ").split('/')
item = list(map(int,item.split()))
box = int(box)
print(f"Minimum weigth for {box} box(es) = {min_capacity(item,box)}")