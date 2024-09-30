# class node:
#     def __init__(self, data, next = None) -> None:
#         self.data = data
#         self.next = None
#     def __str__(self) -> str:
#         return str(self.data)
#     def getData(self):
#         return self.data
#     def getNext(self):
#         return self.next
#     def setData(self, data):
#         self.data = data
#     def setNext(self, next):
#         self.next = next

# class List:
#     def __init__(self) -> None:
#         pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = newNode

    def addHead(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def search(self, item):
        if not self.isEmpty():
            h = self.head
            while h.next != None:
                if h.value == item or h.next.value == item:
                    return 'Found'
                h = h.next
            if h.value == item:
                return 'Found'
        return 'Not Found'

    def index(self, item):
        ind = 0
        if not self.isEmpty():
            h = self.head
            while h.next != None:
                if h.value == item:
                    return ind
                elif h.next.value == item:
                    return ind + 1
                ind += 1
                h = h.next
            if h.value == item:
                return ind
        return -1

    def size(self):
        count = 0
        if not self.isEmpty():
            h = self.head
            while h.next != None:
                count += 1
                h = h.next
            count += 1
        return count

    def pop(self, pos):
        if pos >= 0 and pos < self.size():
            ind = 0
            h = self.head
            if pos == 0:
                self.head = h.next    
                return 'Success'
            while h.next != None:
                if ind + 1 == pos:
                    h.next = h.next.next
                    return 'Success'
                ind += 1
                h = h.next
        return 'Out of Range'
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print(f"{L.search(i[3:])} {i[3:]} in {L}")
    elif i[:2] == "SI":
        print(f"Linked List size = {L.size()} : {L}")
    elif i[:2] == "ID":
        print(f"Index ({i[3:]}) = {L.index(i[3:])} : {L}")
    elif i[:2] == "PO":
        before = f"{L}"
        k = L.pop(int(i[3:]))
        if k == "Success":
            print(f"{k} | {before}-> {L}")
        else:
            # print(f"{k} | {L}")before = f"{L}"
            print(f"{k} | {before}")

print("Linked List :", L)
# print("===== End of program =====")