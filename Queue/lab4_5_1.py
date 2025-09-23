class Queue:
    def __init__(self):
        self.item = []
    def enQueue(self,i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def is_Empty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item)   
    

normal,mirror = input("Enter Input (Normal, Mirror) : ").split()
q_mirror = Queue()

def mirror_operation(mirror):
    mirror = list(mirror[::-1])
    exploded_num = 0
    check = True
    while check:
        check = False
        new_temp = []
        i = 0
        exploded = False
        while i < len(mirror):
            if i+2 < len(mirror) and mirror[i] == mirror[i+1] == mirror[i+2]:
                exploded = True
                q_mirror.enQueue(mirror[i])  
                i += 3  
                exploded_num += 1
            else:
                new_temp.append(mirror[i])
                i += 1
        if exploded:
            mirror = new_temp
            check = True
    string = ''.join(new_temp)
    
    return int(exploded_num) , string[::-1]

# print(exploded)
# print(mirror_string)

def normal_operation(normal):
    exploded_num = 0
    false_exploded = 0
    check = True
    while check:
        check = False
        n = 0
        
        while n<len(normal):
            if n+2<len(normal) and normal[n] == normal[n+1] == normal[n+2]:
                if not q_mirror.is_Empty():
                    item = q_mirror.deQueue()
                    temp = normal[n]+normal[n+1]+item+normal[n+2]
                    normal = normal[:n]+temp+normal[n+3:]
                    if normal[n] == normal[n+1] == normal[n+2]:
                        false_exploded +=1
                        normal = normal[:n]+normal[n+3:]
                    n+=1
                    check = True
                    break
                else:
                    exploded_num +=1
                    normal = normal[:n]+normal[n+3:]
                    check = True
                    break
            else:
                n += 1   
    return exploded_num , false_exploded , normal[::-1]

mirror_exploded,mirror_string = mirror_operation(mirror)
normal_exploded , normal_false_exploded , normal_string = normal_operation(normal)

# print(normal_string)
# print(normal_exploded)
# print(normal_false_exploded)
        
print("NORMAL :")
print(len(normal_string))
print(normal_string if normal_string else "Empty")
print(f"{normal_exploded} Explosive(s) ! ! ! (NORMAL)")
if normal_false_exploded > 0:
    print(f"Failed Interrupted {normal_false_exploded} Bomb(s)")

print("------------MIRROR------------")   
print(": RORRIM") 
print(len(mirror_string))
print(mirror_string if mirror_string else "ytpmE")    
print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_exploded}")               