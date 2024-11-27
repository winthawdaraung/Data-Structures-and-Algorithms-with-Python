#rehashing

def is_prime(n):
    if n % 2 == 1:
        for i in range(3, n//2):
            if n % i == 0:
                return False
        return True
    else:
        return False

def get_next_prime(n):
    while not is_prime(n):
        n += 1
    return n

class hash:
    def __init__(self, max_size, max_col, th):
        self.size = 0
        self.buckets = [None] * max_size
        self.max_col = max_col
        self.max_size = max_size
        self.th = th
        self.data_lst = []
    
    def hasing_key(self, key):
        return key % self.max_size

    def qua_probing(self,key, col):
        return ((self.hasing_key(key) + (col ** 2)) % self.max_size)

    def check_threshold(self):
        count = 0
        for i in self.buckets:
            if i != None:
                count += 1
        threshold = ((count + 1) /self.max_size) * 100
        if threshold > self.th:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()

    def insert(self, key):
        self.check_threshold()
        if self.size < self.max_size:
            col = 0
            ind = self.hasing_key(key)
            node = self.buckets[ind]
            if not node:
                self.buckets[ind] = key
                self.size += 1
                return
            while node and ind < self.max_size:
                col += 1
                print(f"collision number {col} at {ind}")
                if col >= self.max_col:
                    print("****** Max collision - Rehash !!! ******")
                    self.rehash()
                    self.insert(key)
                    break
                ind = self.qua_probing(key, col)
                node = self.buckets[ind]
            if ind < self.max_size and col < self.max_col:
                self.buckets[ind] = key
                self.size += 1
        else:
            print("This table is full !!!!!!")

    def rehash(self):
        new_size = get_next_prime(self.max_size * 2)
        self.buckets = self.buckets + ([None] * (new_size - self.max_size))
        self.max_size = new_size
        for i in range(self.max_size):
            if self.buckets[i] != None:
                self.buckets[i] = None
        self.size = 0
        for j in self.data_lst:
            self.insert(j)
        
    
    def print_table(self):
        for i in range(self.max_size):
            print(f"#{i+1}	{self.buckets[i]}")
        print("----------------------------------------")
        

print(" ***** Rehashing *****")
t_info, data = input("Enter Input : ").split('/')
size, max_col, th = map(int,t_info.split())
table = hash(size, max_col, th)
print("Initial Table :")
table.print_table()
for key in data.split():
    print(f"Add : {key}")
    table.insert(int(key))
    table.data_lst.append(int(key))
    table.print_table()
    if table.size >= size:
        print("This table is full !!!!!!")
        break