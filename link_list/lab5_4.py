class Node:
        def __init__(self,data,next=None):
            self.data = data
            self.next = next
class LinkedList:
    

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,data):
        p = Node(data)
        if self.head is None:
             self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1
    
    def addHead(self,data):
        p = Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def removeHead(self):
        if self.head == None:return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def removeTail(self):
        if self.head == None : return
        if self.head.next == None:
            p = self.head
            self.head = None
            return p.data
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1
    
    def insertAfter(self,i,data):
        p = Node(data)
        q = self.head
        count = 0
        while  q is not None:
            if count == i:
                p.next = q.next
                q.next = p 
                return
            q = q.next
            count += 1
    
    def deteteAll(self):
        self.head = None

        
    def deleteAfter(self,i):
        q = self.head
        count = 0
        while q != None and q.next != None:
            if count == i:
                p = q.next
                q.next = p.next
                p = None
                self.size -= 1
                return
            q = q.next
            count += 1
    
    def removeData(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return
        p = self.head
        while p.next is not None:
            if p.next.data == data:
                p.next = p.next.next
                return
            p = p.next
        

    def printList(self):
        result = []
        t = self.head
        while t is not None:
            result.append(str(t.data))
            t = t.next
        
        return ' '.join(result)
    def remove_worker_first(self):
        p = self.head
        while p:
            if "W" in p.data:
                result = p.data
                self.removeData(result)
                return result
            p = p.next
        if self.head is not None:
            result = self.head.data
            self.removeData(result)
            return result
        return None
    
    def remove_army_first(self):
        p = self.head
        while p:
            if "A" in p.data:
                result = p.data
                self.removeData(result)
                return result
            p = p.next
        if self.head is not None:
            result = self.head.data
            self.removeData(result)
            return result
        return None
    
    def get_worker(self):
        result = []
        p = self.head
        while p != None:
            if "W" in p.data:
                result.append(p.data)
            p = p.next
        
        return ' '.join(result)
    
    def get_army(self):
        result = []
        p = self.head
        while p != None:
            if "A" in p.data:
                result.append(p.data)
            p = p.next
        
        return ' '.join(result)    


l = LinkedList()
print("***This colony is our home***")
start,actions = input("Enter input : ").split('/')
work_ant,army_ant = start.split()
actions = actions.split(',')
i = 1
for w in range(0,int(work_ant),1):
    l.append(f"W{str(i)}")
    i += 1
j = 1
for a in range(0,int(army_ant),1):
    l.append(f"A{str(j)}")
    j += 1
current = l.printList()
print(f"Current Ant List: {current if current else 'Empty'}")  
print()
l_carry_food = LinkedList()
l_attack_mission = LinkedList()
Queen_angry = 0
for ac in actions:
    if ac.startswith('C'):
        _,food = ac.strip().split()
        food = int(food)
        l_carry_food.deteteAll()
        while food > 0:
            target = l.remove_worker_first()
            if target is None:
                
                break
            elif "W" in target:
                food -= 2
            elif "A" in target:
                food -= 5
            l_carry_food.append(target)
        print_food = l_carry_food.printList()
        print(f"Food carrying mission : {print_food if print_food else 'Empty'}")
        if target is None:
            Queen_angry += 1
            print("The food load is incomplete!")
            print("Queen is angry! ! !")
    
    elif ac.startswith('F'):
        _,blood = ac.split()
        blood = int(blood)
        l_attack_mission.deteteAll()
        while blood > 0 :
            target = l.remove_army_first()
            if target is None:
                break
            if "A" in target:
                blood -= 10
            elif "W" in target:
                blood -= 5
            l_attack_mission.append(target)
        print(f"Attack mission : {l_attack_mission.printList()}")
        if target is None:
            print("Ant nest has fallen!")
            break

    elif ac.startswith('S'):
        worker = l.get_worker()
        print(f"-> Remaining worker ants: {worker if worker else 'Empty'}")
        army = l.get_army()
        print(f"-> Remaining soldier ants: {army if army else 'Empty'}")

    elif ac.startswith('W'):
        _,num = ac.split()
        
        i = 1
        for n in range(int(num)):
            l.append(f"W{i}")
            i += 1

    elif ac.startswith('A'):
        _,num = ac.split()
       
        i = 1
        for n in range(int(num)):
            l.append(f"A{i}")
            i += 1

if Queen_angry >= 3:
    print("**The queen is furious! The ant colony has been destroyed**")



