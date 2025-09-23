def operation(metrix,temp,row,col,area_row,area_col):
    
    high = metrix[row][col]
    metrix[row][col] = 0
    temp[row][col] = 1

    dir=[(1,0),(-1,0),(0,1),(0,-1)]
    for dr,dc in dir:
        next_row = row+dr
        next_col = col+dc

        if 0<= next_row < area_row and 0<= next_col < area_col:
            if temp[next_row][next_col] == 0:
                if metrix[next_row][next_col] <= high:
                    operation(metrix,temp,next_row,next_col,area_row,area_col)






print(" *** Water Flow ***")
boder,data,start = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split('/')
rows,cols = map(int,boder.split(','))
data = data.split(',')
metrix = []
for d in data:
    l = [int(i) for i in d]
    metrix.append(l)
start_row,start_col = map(int,start.split(','))
temp = []
for r in range(rows):
    a = [0 for _ in range(cols)]
    temp.append(a)

operation(metrix,temp,start_row,start_col,rows,cols)
for m in metrix:
    print(''.join(map(str,m)))