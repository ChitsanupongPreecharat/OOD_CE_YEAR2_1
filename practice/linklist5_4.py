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

    def printList(self):
        if self.head is None: return 'Empty'
        result = []
        t = self.head
        while t is not None:
            result.append(str(t.data))
            t = t.next
        return ' '.join(result)
    def deleter_data(self,data):
        if self.head is None: return None
        if self.head.data == data: 
            self.head = self.head.next
        cur = self.head
        while cur and cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                return
            cur =  cur.next

    def get_worker_first(self):
        if self.head is None : return None
        cur = self.head
        while cur :
            if 'W' in cur.data:
                result = cur.data
                self.deleter_data(cur.data)
                return result
            cur = cur.next
        if self.head :    
            p = self.head
            self.deleter_data(self.head.data)
            return p.data
        return None
    
    def get_army_first(self):
        if self.head is None : return None
        cur = self.head
        while cur :
            if 'A' in cur.data:
                result = cur.data
                self.deleter_data(cur.data)
                return result
            cur = cur.next
        if self.head :    
            p = self.head
            self.deleter_data(self.head.data)
            return p.data
        return None
    
    def show_woker(self):
        cur = self.head
        result = []
        while cur :
            if 'W' in cur.data:
                result.append(cur.data)
            cur = cur.next
        if result:
            return ' '.join(result)
        return 'Empty'
    
    def show_army(self):
        cur = self.head
        result = []
        while cur :
            if 'A' in cur.data:
                result.append(cur.data)
            cur = cur.next
        if result:
            return ' '.join(result)
        return 'Empty'     
print("***This colony is our home***")
l_main = LinkedList()
start_ant,action = input("Enter input : ").split('/')
worker_ant,army_ant = start_ant.split()
if int(worker_ant) > 0:  
    for i in range(int(worker_ant)):
        l_main.append(f'W{i+1}')
            
if int(army_ant) >0 :
    for i in range(int(army_ant)):
        l_main.append(f'A{i+1}')

print(f"Current Ant List: {l_main.printList()}")
print()
action = action.split(',')
Queen_angry = 0
for ac in action:
    if 'C' in ac:
        _,num=ac.split()
        food = int(num)
        l_food = LinkedList()
        while food > 0:
            target = l_main.get_worker_first()
            if target is None:
                break
            elif 'W' in target:
                food -= 2
            elif 'A' in target:
                food -= 5
            l_food.append(target)
        print(f"Food carrying mission : {l_food.printList()}")
        if target is None:
            Queen_angry += 1
            print("The food load is incomplete!")
            print("Queen is angry! ! !")
    elif 'F' in ac:
        _,num = ac.split()
        hp = int(num)
        l_army = LinkedList()
        while hp > 0:
            target = l_main.get_army_first()
            if target is None:
                break
            elif 'A' in target:
                hp -= 10
            elif 'W' in target:
                hp -= 5
            l_army.append(target)
        print(f"Attack mission : {l_army.printList()}")
        if target is None:
            print("Ant nest has fallen!")
            break
    elif 'S' in ac:
        print(f"-> Remaining worker ants: {l_main.show_woker()}")
        print(f"-> Remaining soldier ants: {l_main.show_army()}")
    
    elif 'W' in ac:
        _,num = ac.split()
        num = int(num)
        if num > 0:   
            for i in range(num):
                l_main.append(f'W{i+1}')

    elif 'A' in ac:
        _,num = ac.split()
        num = int(num)
        if num > 0:   
            for i in range(num):
                l_main.append(f'A{i+1}')

if Queen_angry >= 3:
    print("**The queen is furious! The ant colony has been destroyed**")