class Stack:
    def __init__(self):
        self.list = []
    
    def push(self,i):
        self.list.append(i)
    
    def pop(self):
        if not self.is_empty():    
            return self.list.pop(-1)
    
    def peek(self):
        if not self.is_empty(): 
            return self.list[-1]
    
    def is_empty(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)
    
    
    
s = Stack()
num,action = input("Enter Input : ").split('/')
num = list(map(int,num.split()))
for n in num:
    if n > 0 :
        s.push(n)
print()
print("start")
print(s.list)

for ac in action.split(','):
    if ac.startswith('spawn'):
        _,hp = ac.split()
        s.push(int(hp))
        print()
        print(f"spawn an enemy of {hp} HP")
        print(s.list)
    elif ac.startswith('dmg'):
        _,dmg = ac.split()
        dm = int(dmg)
        kill = 0
        if dm <= 0:
            print()
            print("Invalid number")
            break
        else:
            while not s.is_empty() and dm > 0:
                current = s.pop()
                if current > dm:
                    s.push(current-dm)
                    dm = 0
                else:
                    kill +=1
                    dm -= current
        print()
        print(f"deal {dmg} damage, killed {kill} enemy")
        print(s.list)

print()
if s.is_empty():
    print(">>>> Player Wins <<<<")