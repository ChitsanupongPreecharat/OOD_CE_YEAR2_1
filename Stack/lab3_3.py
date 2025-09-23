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
    def get_item(self):
        return list(self.item)
    

s = Stack()
start_hp,actions = input("Enter Input : ").split("/")
for hp in start_hp.split():
    if int(hp) > 0:
        s.push(int(hp))

status = 'Start'
if status == 'Start':
    print()
    print("start")
    print(s.get_item(),end=("\n\n"))
    

for ac in actions.split(','):
    command,number = ac.split()
    num = int(number)
    if command == 'spawn' and num >0:
        s.push(num)
        print(f"spawn an enemy of {num} HP")
        print(s.get_item(),end=("\n\n"))
    elif command == 'dmg' :
        if num <= 0:
            print("Invalid number")
        else:    
            kill = 0
            while not s.isEmpty() and num>0:
                current = s.pop()
                if int(current) > num:
                    s.push(int(current)-num)
                    num=0
                else:
                    num -= int(current)
                    kill +=1
            print(f"deal {number} damage, killed {kill} enemy")  
            print(s.get_item(),end=("\n\n"))             

    if s.isEmpty():
        print(">>>> Player Wins <<<<") 





