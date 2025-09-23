class Stack:
    def __init__(self,list=None):
        if list == None:
            self.item = []
        else:
            self.item = list
    
    def push(self,i):
        self.item.append(i)
    def pop(self):
        if not self.isEmpty():
            return self.item.pop()
    def peek(self):
        return self.item[-1]
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)   
    
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

### Mirror
s_mirror = Stack()
q_mirror = Queue()
mirror = list(mirror[::-1])
i = 0
mirror_exploded = 0

### Mirror loop fix ###
changed = True
while changed:
    changed = False
    new_mirror = []
    i = 0
    while i < len(mirror):
        count = 1
        while i + count < len(mirror) and mirror[i] == mirror[i + count]:
            count += 1
        if count >= 3:
            q_mirror.enQueue(mirror[i])
            del mirror[i:i+count]  # ลบทั้งหมดที่ระเบิด
            mirror_exploded += 1
            changed = True
            # ไม่ต้องเพิ่ม i เพราะ list สั้นลงแล้ว
        else:
            new_mirror.extend(mirror[i:i + count])
            i += count
    mirror = new_mirror



for ch in mirror:
    s_mirror.push(ch)

mirror_result = ''
while not s_mirror.isEmpty():
    mirror_result += s_mirror.pop()



## Normal       
normal = list(normal)
s_normal = Stack()
q_normal = Queue()

normal_exploded = 0
insert_same_color = 0
changed = True
while changed:
    i = 0
    changed = False
    while i < len(normal):
        count =1
        while i+count<len(normal) and normal[i] == normal[i+count]:
            count += 1
        if count >= 3:
            if not q_mirror.is_Empty():
                item = q_mirror.deQueue()
                
                temp = normal[i:i+count] 
                temp.insert(2, item)     
                if temp[0] == temp[1] == temp[2]:  
                    del normal[i:i+count-1]
                    
                    insert_same_color += 1
                else:
                    
                    normal.insert(i+2, item)
                changed = True
                break
            else:
                del normal[i:i+count]
                normal_exploded += 1
                changed = True
                break

        else:
             
            i += count
n = 0
while n < len(normal):
    s_normal.push(normal[n])
    n+=1

normal_result = ''
while not s_normal.isEmpty():
    normal_result += s_normal.pop()
   


print("NORMAL :")
print(len(normal_result))
print(normal_result if normal_result else "Empty")
print(f"{normal_exploded} Explosive(s) ! ! ! (NORMAL)")
if insert_same_color > 0:
    print(f"Failed Interrupted {insert_same_color} Bomb(s)")

print("------------MIRROR------------")   
print(": RORRIM") 
print(len(mirror_result))
print(mirror_result if mirror_result else "ytpmE")    
print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_exploded}") 