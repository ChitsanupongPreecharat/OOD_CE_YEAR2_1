print(" *** Water Flow ***")
def action(tempmap,data,water_row,water_col):
    row = len(data)
    col = len(data[0])
    current_high =  data[water_row][water_col]
    data[water_row][water_col] = 0
    tempmap[water_row][water_col] = 1
    
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
        
    ]

    for dr,dc in directions:
        nr = water_row + dr
        nc = water_col + dc

        if 0<=nr<row and 0<=nc<col:
            if tempmap[nr][nc] == 0:
                if data[nr][nc] <= current_high:
                    action(tempmap,data,nr,nc)
            



area,data,start = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split('/')
rows,cols = map(int,area.split(','))
if rows<1 or cols<1:
    print("Error: Rows and columns must be between 1 and 9")

else:
    data = data.split(',')
    matrix = []
    for d in data:
        l = [int(i) for i in d]
        matrix.append(l)
    start_row,start_col = start.split(',')
    start_row = int(start_row)
    start_col = int(start_col)
    if not (0 <= start_row < rows) or not (0 <= start_col < cols):
        print("Error: Start coordinates are out of grid bounds")
    

    else:
        tempmap = [[0 for _ in range(cols)] for _ in range(rows)]

        action(tempmap,matrix,start_row,start_col)
        for row in matrix:
            print(''.join(map(str, row)))






