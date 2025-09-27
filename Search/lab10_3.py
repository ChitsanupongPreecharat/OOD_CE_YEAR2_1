class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,max_collision):
        self.size = size
        self.max_collision = max_collision
        self.table = [None] * size
        self.full_msg_shown = False
    
    def get_index(self,key):
        total = sum(ord(ch) for ch in key)
        return total % self.size
    
    def insert(self,data):
        if not self.full_msg_shown:
            if all(self.table):
                if not self.full_msg_shown:
                    print("This table is full !!!!!!")
                    self.full_msg_shown = True
                    return
            
            index = self.get_index(data.key)
            i = 0
            while i < self.max_collision:
                new_index = (index + i**2) % self.size
                if self.table[new_index] is None:
                    self.table[new_index] = data
                    return 
                else:
                    print(f"collision number {i+1} at {new_index}")
                    i += 1
            print("Max of collisionChain")

        
            
    
    def show_information(self):
        if not self.full_msg_shown:
            for i,item in enumerate(self.table):
                print(f"#{i+1}	{item}")
            print("---------------------------")
        


print(" ***** Fun with hashing *****")
infor,List = input("Enter Input : ").split('/')
size_table,max_cliiision = map(int,infor.split())
List = list(List.split(','))
H = hash(size_table,max_cliiision)

for l in List:
    key,value = l.split()
    H.insert(Data(key,value))
    H.show_information()
    