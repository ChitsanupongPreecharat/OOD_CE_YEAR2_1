class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            q = self.head
            while q.next:
                q=q.next
            q.next = p
    
    def printlist(self):
        if self.head is None: return 'Empty'
        result = ''
        p = self.head
        while p:
            result += str(p.data)
            result += ' '
            p = p.next
        return result if result != '' else 'Empty'
    
    def removeHead(self):
        if self.head is None: return 
        if self.head.next is None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        return p.data
    
    def removedata(self,data):
        if self.head is None :return 
        if self.head.data == data:
            self.head = self.head.next
            return 
        p = self.head
        while p.next :
            if p.next.data == data:
                p.next = p.next.next
                return 
            p = p.next
    
    def get_worker_first(self):
        if self.head is None : return 
        else:
            p = self.head
            while p:
                if 'W' in p.data:
                    cur = p.data
                    self.removedata(p.data)
                    return cur
                p = p.next
            return self.removeHead()
    
    def get_army_first(self):
        if self.head is None : return 
        else:
            p = self.head
            while p:
                if 'A' in p.data:
                    cur = p.data
                    self.removedata(p.data)
                    return cur
                p = p.next
            return self.removeHead()

    def get_worker(self):
        result = ''
        p = self.head
        while p:
            if "W" in p.data:
                result += p.data
                result += ' '
            p = p.next
        return result if result != '' else 'Empty'
    
    def get_army(self):
        result = ''
        p = self.head
        while p:
            if "A" in p.data:
                result += p.data
                result += ' '
            p = p.next
        return result if result != '' else 'Empty'

L = LinkList()
print("***This colony is our home***")
ant_start,action = input("Enter input : ").split('/')
work_start,army_start = map(int,ant_start.split())
if work_start > 0:
    for w in range(work_start):
        L.append(f'W{w+1}')
if army_start >0 :
    for a in range(army_start):
        L.append(f'A{a+1}')
print(f"Current Ant List: {L.printlist()}")
print()
Queen_argry = 0
for ac in action.split(','):
    if ac.startswith("C"):
        ant_carry_food = []
        _,num = ac.split()
        num = int(num)
        L_carry_food = LinkList()
        while num>0:
            cur_ant = L.get_worker_first()
            if cur_ant is None:
                Queen_argry += 1
                break
            L_carry_food.append(cur_ant)
            if 'W' in cur_ant:
                num -= 2
            elif 'A' in cur_ant:
                num -= 5
        
        print(f"Food carrying mission : {L_carry_food.printlist()}")
        if cur_ant is None:
            print("The food load is incomplete!") 
            print("Queen is angry! ! !")           
    elif ac.startswith("F"):
        _,hp = ac.split()
        hp = int(hp)
        L_army_ant = LinkList()
        while hp > 0:
            cur_ant = L.get_army_first()
            if cur_ant is None :
                
                break
            L_army_ant.append(cur_ant)
            if "W" in cur_ant:
                hp -= 5
            if "A" in  cur_ant:
                hp -= 10
        print(f"Attack mission : {L_army_ant.printlist()}")
        if cur_ant is None:
            print("Ant nest has fallen!")
            break
    elif ac == 'S':
        print(f'-> Remaining worker ants: {L.get_worker()}')
        print(f"-> Remaining soldier ants: {L.get_army()}")

    elif ac.startswith('W'):
        _,num = ac.split()
        num = int(num)
        
        if num > 0:
            for i in range(num):
                L.append(f'W{i+1}')
    
    elif ac.startswith("A"):
        _,num = ac.split()
        num = int(num)
        
        if num > 0:
            for i in range(num):
                L.append(f'A{i+1}')

if Queen_argry >= 3:
    print("**The queen is furious! The ant colony has been destroyed**")