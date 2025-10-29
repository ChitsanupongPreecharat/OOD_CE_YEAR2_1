def sort_str(l):
    for last in range(len(l)-1,0,-1):
        swap = False
        for i in range(last):
            if ord(l[i]) > ord(l[i+1]):
                l[i],l[i+1] = l[i+1],l[i]
                swap = True
        if not swap:
            break
    return l


il = list(map(str,input("Enter : ").split(',')))
input_list = []
for i in il:
    a,b = i.split()
    if a not in input_list:
        input_list.append(a)
    if b not in input_list:
        input_list.append(b)
    

input_list = sort_str(input_list)

metrix = [[0 for _ in range(len(input_list))] for _ in range(len(input_list))]
index_map = {char:i for i ,char in enumerate(input_list)}
for i in il:
    a,b = i.split()
    A = index_map[a]
    B = index_map[b]
    metrix[A][B] = 1

print('    '+'  '.join(input_list))
    
for m in range(len(metrix)):
    print(f"{input_list[m]} : {', '.join(map(str, metrix[m]))}")
