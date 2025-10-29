def straight_selection_sort(l):
    for last in range(len(l)-1,0,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last],l[biggest_i] = l[biggest_i],l[last]
    return l





num = list(map(int,input("Input num:").split()))
print(straight_selection_sort(num))