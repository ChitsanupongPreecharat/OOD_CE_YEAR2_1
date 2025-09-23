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
s1 = Stack()
s2 = Stack()
print("******** Parking Lot ********")
parking_max,car_in_parking,action,car_action = input("Enter max of car,car in soi,operation : ").split()
car_in_parking = list(map(int,car_in_parking.split(',')))

for i in car_in_parking:
    if i > 0:    
        s1.push(i)

if action == 'arrive':
    if s1.size() < int(parking_max):
        if int(car_action) not in s1.item:
            s1.push(int(car_action))
            print(f"car {car_action} arrive! : Add Car {car_action}")
        else:
            print(f"car {car_action} already in soi")
    else:
        print(f"car {car_action} cannot arrive : Soi Full")
    print(s1.item)

elif action == 'depart':
    if not s1.isEmpty():
        if int(car_action) in s1.item:
            
            while s1.peek() != int(car_action):
                s2.push(s1.pop())
            s1.pop()
            while not s2.isEmpty():
                s1.push(s2.pop())
            print(f"car {car_action} depart ! : Car {car_action} was remove")
        else:
            print(f"car {car_action} cannot depart : Dont Have Car {car_action}")
    else:
        print(f"car {car_action} cannot depart : Soi Empty")
    print(s1.item)
    
