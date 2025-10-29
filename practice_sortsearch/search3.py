class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,max_collision):
        self.size = size
        self.max_colision = max_collision
        self.table = [None] * size
        self.full = False
    
    def get_index(self,key):
        return sum(ord(ch) for ch in key ) % self.size 
    def insert(self,data):
        if not all(self.table):
            index = self.get_index(data.key)
            i = 0
            while i < self.max_colision:
                new_index = (index + i**2) % self.size
                if self.table[new_index] is None:
                    self.table[new_index] = data
                    return 
                else:
                    print(f"collision number {i+1} at {new_index}")
                    i+=1
            print("Max of collisionChain")
        else:
            print("This table is full !!!!!!")
            self.full = True
            return 
    
    def show_information(self):
        if not self.full:
            for i,item in enumerate(self.table):
                print(f'#{i+1}	{item}')
            print('---------------------------')

num,data = input('Enter Input : ').split('/')
size,collision = num.split()
h = hash(int(size),int(collision))
data = list(data.split(','))
for d in data:
    key,value = d.split()
    if not h.full:
        h.insert(Data(key,value))
    h.show_information()