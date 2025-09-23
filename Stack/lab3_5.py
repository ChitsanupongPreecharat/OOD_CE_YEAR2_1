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
    
print("******** Parking Lot ********")
slot,list_car,action,num_car = input("Enter max of car,car in soi,operation : ").split()
list_car = list_car.split(",")
s = Stack()
s2 = Stack()
for i in list_car:
    if int(i) > 0:
        s.push(int(i))

if action == 'arrive':
    if s.size() < int(slot):
        if num_car in list_car:
            print(f"car {num_car} already in soi")
        else:
            s.push(int(num_car))
            print(f"car {num_car} arrive! : Add Car {num_car}")
    else:
        print(f"car {num_car} cannot arrive : Soi Full")
    print(s.item)

elif action == 'depart':
    if s.isEmpty():
        print(f"car {num_car} cannot depart : Soi Empty")
    elif num_car not in list_car:
        print(f"car {num_car} cannot depart : Dont Have Car {num_car}")    
    else:
        while s.peek() != int(num_car):
            s2.push(s.pop())
        s.pop()

        while not s2.isEmpty():
            s.push(s2.pop())

        print(f"car {num_car} depart ! : Car {num_car} was remove")    



    print(s.item)    

        
         

    

