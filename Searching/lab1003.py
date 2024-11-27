"""Write a Hashing program with the following operations:

Find the index of the Table from the sum of the ASCII values of the key, then mod it by the size of the Table.
If a collision occurs, shift the index using Quadratic Probing.
If collisions occur up to a defined limit, discard that Data immediately.
If the Table is full, display This table is full !!!!!!. If this message has already been shown, do not display it again (show it only once).
Explanation of Input:
The Data is divided into two parts using a "/".

The left side refers to the size of the Table and the MaxCollision limit, respectively.
The right side contains n sets of Data, where each set of Data is separated by a comma. In each set of Data, the key and value are provided in that order."""

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, max_size, max_col,):
        self.size = 0
        self.buckets = [None] * max_size
        self.max_col = max_col
        self.max_size = max_size
    
    def hasing_key(self, key):
        val = 0
        for i in key:
            val += ord(i)
        return val % self.max_size

    def qua_probing(self,key, col):
        return ((self.hasing_key(key) + (col ** 2)) % self.max_size)

    def insert(self, key, data):
        if self.size < self.max_size:
            col = 0
            ind = self.hasing_key(key)
            node = self.buckets[ind]
            if not node:
                self.buckets[ind] = Data(key, data)
                self.size += 1
                return
            while node and ind < self.max_size:
                col += 1
                print(f"collision number {col} at {ind}")
                if col >= self.max_col:
                    print("Max of collisionChain")
                    return
                ind = self.qua_probing(key, col)
                node = self.buckets[ind]
            if ind < self.max_size and col < self.max_col:
                self.buckets[ind] = Data(key, data)
                self.size += 1
        else:
            print("This table is full !!!!!!")

    
    def print_table(self):
        for i in range(self.max_size):
            print(f"#{i+1}	{self.buckets[i]}")
        print("---------------------------")
        

print(" ***** Fun with hashing *****")
t_info, data = input("Enter Input : ").split('/')
size, max_col = map(int,t_info.split())
table = hash(size, max_col)
for i in data.split(','):
    key, val = i.split()
    table.insert(key, val)
    table.print_table()
    if table.size >= size:
        print("This table is full !!!!!!")
        break
    
