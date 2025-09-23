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
s = Stack()
start_hp,action = input("Enter Input : ").split('/')
start_hp = list(map(int,start_hp.split()))
action = list(action.split(','))


for i in start_hp:
    if i > 0:    
        s.push(i)
print("start")
print(s.item,end='\n\n')

for i in range(len(action)):
    if action[i].startswith('spawn'):
        _,hp = action[i].split()
        if int(hp) > 0:
            s.push(int(hp))
            print(f"spawn an enemy of {hp} HP")
            print(s.item,end='\n\n')
    elif action[i].startswith('dmg'):
        _,num = action[i].split()
        num = int(num)
        if num <= 0:
            print("Invalid number")
            break
        n = num
        kill = 0
        while not s.isEmpty() and num > 0:
            current = s.pop()
            if int(current) > num:
                s.push(int(current)-num)
                num = 0
            else:
                num -= int(current)
                kill += 1
        print(f"deal {n} damage, killed {kill} enemy")
        print(s.item,end='\n\n')

if s.isEmpty():
    print(">>>> Player Wins <<<<")

