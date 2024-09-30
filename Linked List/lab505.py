#raddit sort
class Node():
    def __init__(self, data = None, previous = None, next = None):
        self.data = data
        self.next = next
        self.previous = previous
class LinkedList():
    def __init__(self, lst = None):
        self.head = None

    def __str__(self) -> str:
        s = ''
        cur = self.head  
        while cur:
            s += str(cur.data)
            if cur.next:
                s += ' -> '
            cur = cur.next
        return s

    def append(self, data):
        newNode = Node(data)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode

    def add_before(self,data):
        newNode = Node(data)
        if self.head:
            cur = self.head
            newNode.next = cur
            cur.previous = newNode
            self.head = newNode
        else:
            self.head = newNode
       
def raddit_sort(num):

    # positives = [n for n in num if n > 0]
    # negatives = [-n for n in num if n < 0]

    
    max_num = max(map(abs,num))
    rounds = 0
    exp = 1
    while max_num // exp > 0:
        rounds += 1
        print("------------------------------------------------------------")
        print(f"Round : {rounds}")
        sorting_place = [LinkedList() for _ in range(10)]
        for n in num:
            index = (abs(n) // exp) % 10
            if sorting_place[index].head:
                if sorting_place[index].head.data < 0 and n > 0:
                    sorting_place[index].add_before(n)
                else:
                    sorting_place[index].append(n)
            else:
                sorting_place[index].append(n)
        
        for i in range(10):
            if sorting_place[i].head:
                s = ''
                h = sorting_place[i].head
                while h:
                    s += str(h.data) + ' '
                    h = h.next
                print(f"{i} : {s}")
            else:
                print(f"{i} : ")
        
        num = []
        for i in range(9, -1, -1):
            cur = sorting_place[i].head
            while cur:
                if cur.data >= 0:
                    num.append(cur.data)
                cur = cur.next
        for j in range(10):
            cur = sorting_place[j].head
            while cur:
                if cur.data < 0:
                    num.append(cur.data)
                cur = cur.next
        exp *= 10
    return num, rounds
        

inp = input("Enter Input : ").strip().split()
num = list(map(int, inp))

initial_list = LinkedList()
for n in num:
    initial_list.append(n)

sorted_lst,rounds = raddit_sort(num)

final_list = LinkedList()
for num in sorted_lst:
    final_list.append(num)
    
print("------------------------------------------------------------")
print(f"{rounds} Time(s)")
print(f"Before Radix Sort : {initial_list}")
print(f"After  Radix Sort : {final_list}")