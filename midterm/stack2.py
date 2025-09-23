class Stack:
    def __init__(self):
        self.item = []

    def push(self,i):
        self.item.append(i)

    def pop(self):
        if not self.is_empty():
            return self.item.pop(-1)
    
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
    
    def is_empty(sefl):
        return len(sefl.item) == 0
    
    def size(sefl):
        return len(sefl.item)

def fine_plate(weight):
    result = []
    plate = [25,20,15,10,5,2.5,1.25]
    for p in plate:
        while sum(result) + p <= weight and len(result) < 5:
            result.append(p)
    return sorted(result,reverse=True) if sum(result) == weight else None

def actions_plate(old,new):
    action = []
    misstake = 0 
    for i in range(min(len(old),len(new))):
        if old[i] != new[i]:
            break
        misstake += 1
    
    for i  in range(len(old)-1,misstake-1,-1):
        remove = s.pop()
        action.append(f'PO:{remove}')
    
    for i in range(misstake,len(new)):
        s.push(new[i])
        action.append(f'PU:{new[i]}')

    return ' '.join(action)

def print_bar(new_plate,actions,b):
    dashes = '-' * (5-len(new_plate))
    plates = ''.join(f"[{i}]" for i in new_plate) 
    reversed_plates = ''.join(f"[{i}]" for i in reversed(new_plate))
    bar = f"{dashes}{plates}|======|{reversed_plates}{dashes}"
    has_float = any(isinstance(i,float) for i in new_plate)
    if actions == '':
        if has_float:
            print(f"{bar} => {b} KG.")
        else:
            print(f"{bar} => {int(b)} KG.")
    else:
        if has_float:
            print(f"{actions} => {bar} => {b} KG.")
        else:
            print(f"{actions} => {bar} => {int(b)} KG.")

bar = list(map(float,input("Enter needed weight(s): ").split()))
s = Stack()
for b in bar:
    weight = (b-20)/2
    new_plate = fine_plate(weight)
    if new_plate is None:
        print(f"It's impossible to achieve the weight you want({b}).")
        break
    else:
        actions = actions_plate(s.item,new_plate)
        print_bar(new_plate,actions,b)