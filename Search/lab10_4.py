def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while not is_prime(n):
        n += 1
    return n




class Hash:
    def __init__(self, size, max_collision, threshold):
        self.size = size
        self.max_collision = max_collision
        self.threshold = threshold
        self.table = [None] * size
        self.count = 0
        self.order = []   

    def is_over_threshold(self):
        return (self.count / self.size) * 100 >= self.threshold

    def rehash(self, data=None):
        
        old_order = list(self.order)
        if data is not None:
            old_order.append(data)

        new_size = next_prime(self.size * 2)
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0
        self.order = []  

        for item in old_order:
            self.add(item)   

    def add(self, data):
        index = data % self.size
        i = 0
        while i < self.max_collision:
            new_index = (index + i**2) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = data
                self.count += 1
                self.order.append(data)   
                if self.is_over_threshold():
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehash()
                return
            else:
                i += 1
                print(f"collision number {i} at {new_index}")
        print("****** Max collision - Rehash !!! ******")
        self.rehash(data)
        
         
    def show_information(self):
        
            for i,item in enumerate(self.table):
                print(f"#{i+1}	{item}")
            print("----------------------------------------")

print(" ***** Rehashing *****")
left,right = input("Enter Input : ").split('/')
size,collision,threshold = map(int,left.split())
right = list(map(int,right.split()))
H = Hash(size,collision,threshold)
print("Initial Table :")
H.show_information()
for d in right:
    print(f'Add : {d}')
    H.add(d)
    H.show_information()