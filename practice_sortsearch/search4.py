class hash:
    def __init__(self,size,colision,threshold):
        self.size = size
        self.colision = colision
        self.threshold = threshold
        self.table = [None] * self.size
        self.count = 0
        self.data = []

    def rehashing(self):
        def fine_near_prime(n):
            def is_prime(x):
                if x < 2:
                    return False
                for i in range(2,(int(x**0.5))+1):
                    if x % i==0:
                        return False
                return True
            n = n*2
            while not is_prime(n):
                n+=1
            return n
                
        self.old_data = self.data.copy()
        self.size = fine_near_prime(self.size)
        self.table = [None] * self.size
        self.count = 0
        self.data = []
        for d in self.old_data:
            self.add(d)
    
    def add(self,data):
        
        index  = data % self.size
        i = 0 
        while i < self.colision:
            new_index = (index+i**2) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = data
                self.count += 1
                self.data.append(data)
                if ((self.count/self.size) *100) >=self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehashing()
                return
            else:
                i+=1
                print(f"collision number {i} at {new_index}")
        print("****** Max collision - Rehash !!! ******")
        self.data.append(data)
        self.rehashing()
    
    def show_information(self):
        for i,item in enumerate(self.table):
            print(f'#{i+1}	{item}')
        print('----------------------------------------')

infor_hash,data = input('Enter Input : ').split('/')
size,colision,threshold = map(int,infor_hash.split())
data = list(map(int,data.split()))
h = hash(size,colision,threshold)
h.show_information()
for d in data:
    print(f'Add : {d}')
    h.add(d)
    h.show_information()

        