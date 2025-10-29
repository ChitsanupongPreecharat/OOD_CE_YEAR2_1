def sort(n):
    for last in range(len(n)-1,0,-1):
        biggest = n[0]
        biggest_i = 0
        for i in range(1,last+1):
            if n[i] > biggest:
                biggest = n[i]
                biggest_i = i
        n[biggest_i],n[last] = n[last],n[biggest_i]
    return n


num = list(map(int,input("Enter Input : ").split()))
print(sort(num))