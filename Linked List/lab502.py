"""
Write a class for a Doubly Linked List which includes the following methods:

def __init__(self): Initializes the linked list.

def __str__(self): Returns a string representing the values in the linked list.

def str_reverse(self): Returns a string representing the values in the linked list from back to front.

def isEmpty(self): Returns whether the list is empty.

def append(self, data): Adds a node with the given data to the end of the linked list.

def insert(self, index, data): Inserts data at the specified index.

def remove(self, data): Removes and returns the node with the given data.

When inserting, the new data replaces the position of the old data, and the old data is moved to follow the new data.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        s = ""
        if not self.isEmpty():
            h = self.head
            s += str(self.head.data)
            while h.next != None:
                s += "->" + str(h.next.data)
                h = h.next
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def str_reverse(self):
        s = str(self)
        lst = s.split("->")[::-1]
        return "->".join(lst)
    
    def append(self, data):
        newNode = Node(data)
        if not self.isEmpty():
            h = self.head
            while h.next != None:
                h = h.next
            newNode.previous = h
            h.next = newNode
        else:
            self.head = newNode
        self.tail = newNode
    
    def addBefore(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head:
            self.head.previous = newNode
        self.head = newNode
        if not self.tail:
            self.tail = newNode

    def insert(self, index, data):
        if index < 0 or index > self.size():
            print("Data cannot be added")
        else:
            newNode = Node(data)
            if index == 0:
                newNode.next = self.head
                if self.head:
                    self.head.previous = newNode
                self.head = newNode
                if not self.tail:
                    self.tail = newNode
            elif index == self.size():
                self.tail.next = newNode
                newNode.previous = self.tail
                self.tail = newNode
            else:
                cur = self.head
                for _ in range(index - 1):
                    cur = cur.next
                newNode.next = cur.next
                newNode.previous = cur
                cur.next = newNode
            print(f"index = {index} and data = {data}")

    def remove(self, data):
        if not self.isEmpty():
            index = 0
            cur = self.head
            while cur:
                if cur.data == data:
                    if cur.previous:
                        cur.previous.next = cur.next
                    else:
                        self.head = cur.next
                    if cur.next:
                        cur.next.previous = cur.previous
                    else:
                        self.tail = cur.previous
                    print(f"removed : {data} from index : {index}")
                    return index, data
                cur = cur.next
                index += 1
        print("Not Found!")
        return -1,data
    
    def size(self):
        count = 0
        if not self.isEmpty():
            h = self.head
            while h.next != None:
                count += 1
                h = h.next
            count += 1
        return count
    
DLL = DoubleLinkedList()
error = 0
inp = input("Enter Input : ").split(',')
for i in inp:
    if i.strip().split()[0] == 'A': #Append
        data = i.strip().split()[-1]
        DLL.append(data)
    elif i.strip().split()[0] == 'Ab': #AddBefore
        data = i.strip().split()[-1]
        DLL.addBefore(data)
    elif i.strip().split()[0] == 'I': #Insert
        data = i.strip().split()[-1].split(':')[-1]
        index = int(i.strip().split()[-1].split(':')[0])
        DLL.insert(index,data)
        
    elif i.strip().split()[0] == 'R': #Remove
        data = i.strip().split()[-1]
        index, data = DLL.remove(data)
           
    print(f"linked list : {DLL}")
    print(f"reverse : {DLL.str_reverse()}")
    error = 0
