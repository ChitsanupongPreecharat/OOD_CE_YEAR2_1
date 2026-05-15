class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}, {self.value})"


class HashTable:
    def __init__(self, size, max_collision):
        self.size = size
        self.max_collision = max_collision
        self.table = [None] * size
        self.full_msg_shown = False

    def get_index(self, key):
        total = sum(ord(ch) for ch in key)
        return total % self.size

    def is_full(self):
        return all(item is not None for item in self.table)

    def insert(self, data):
        if self.full_msg_shown:
            return

        if self.is_full():
            print("This table is full !!!!!!")
            self.full_msg_shown = True
            return

        index = self.get_index(data.key)

        for i in range(self.max_collision):
            new_index = (index + i**2) % self.size

            if self.table[new_index] is None:
                self.table[new_index] = data
                return

            print(f"collision number {i + 1} at {new_index}")

        print("Max of collisionChain")

    def show_information(self):
        if not self.full_msg_shown:
            for i, item in enumerate(self.table):
                print(f"#{i+1}	{item}")
            print("---------------------------")


print(" ***** Fun with hashing *****")
info, data_list = input("Enter Input : ").split("/")
size_table, max_collision = map(int, info.split())
data_list = data_list.split(",")
H = HashTable(size_table, max_collision)

for item in data_list:
    key, value = item.split()
    H.insert(Data(key, value))
    H.show_information()
