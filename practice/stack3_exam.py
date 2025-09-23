class Stack:
    def __init__(self,list=None):
        if list is not None :   
            self.list = list
        else:
            self.list = []

    def push(self,i):
        self.list.append(i)

    def pop(self):
        if not self.isEmpty():    
            return self.list.pop()

    def peek(self):
        return self.list[-1]

    def isEmpty(self):
        return self.list == []
    
    def size(self):
        return len(self.list) 
    
    def search(self,data):
        return data in self.list
    
print("******** Parking Lot ********")    
max_car,car_slot,action,car_action = input("Enter max of car,car in soi,operation : ").split()
car_slot = list(car_slot.split(','))
s1 = Stack()
s2 = Stack()
for i in car_slot:
    if int(i) > 0:    
        s1.push(int(i))

max_car = int(max_car)
car_action = int(car_action)
if action == 'arrive':
    if s1.size() < max_car:
        if not s1.search(car_action):
            s1.push(car_action)
            print(f"car {car_action} arrive! : Add Car {car_action}")
        else:
            print(f"car {car_action} already in soi")
    else:
        print(f"car {car_action} cannot arrive : Soi Full")

elif action == 'depart':
    if not s1.isEmpty():
        if s1.search(car_action):
            while int(s1.peek()) != car_action:
                s2.push(s1.pop())
            s1.pop()
            while not s2.isEmpty():
                s1.push(s2.pop())
            print(f"car {car_action} depart ! : Car {car_action} was remove")
        else:
            print(f"car {car_action} cannot depart : Dont Have Car {car_action}")
    else:
        print(f"car {car_action} cannot depart : Soi Empty")

print(s1.list)