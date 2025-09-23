i = 1
while True:
    i += 1
    j = i
    while j != 1:
        if j % 2 == 0:
            j = j//2
        else:
            j = (3*j)+1
        print(i,j)

# i = input("input num:")
# i = int(i)
# j = i
# while j != 1:
#     if j % 2 == 0:
#         j = j // 2
#     else:
#         j = (3*j)+1
#     print(i,j)