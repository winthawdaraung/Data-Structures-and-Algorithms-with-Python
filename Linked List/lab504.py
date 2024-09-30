class Node():
    def __init__(self, data = None, previous = None, next = None):
        self.data = data
        self.next = next
        self.previous = previous
    
class textEditor():
    def __init__(self, head = None):
        self.cursor = Node('|')
        if head == None:
            self.head = self.cursor
        else:
            self.head = head
            self.cursor.previous = head
            self.head.next = self.cursor
    
    def __str__(self):
        if self.head == None:
            return
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s
    
    def insert(self, word):
        newWord = Node(word)
        nxt = self.cursor.next
        newWord.next = nxt
        newWord.previous = self.cursor
        self.cursor.next = newWord
        self.right()
        
        
    def left(self):
        if self.cursor.previous:
            prev = self.cursor.previous
            self.cursor.previous = prev.previous
            if prev.previous:
                prev.previous.next = self.cursor
            else:
                self.head = self.cursor
            prev.next = self.cursor.next
            if self.cursor.next:
                self.cursor.next.previous = prev
            self.cursor.next = prev
            prev.previous = self.cursor

    def right(self):
        if self.cursor.next:
            next = self.cursor.next
            self.cursor.next = next.next
            if next.next:
                next.next.previous = self.cursor
            next.previous = self.cursor.previous
            if self.cursor.previous:
                self.cursor.previous.next = next
            else:
                self.head = next
            self.cursor.previous = next
            next.next = self.cursor

    def backspace(self):
        prev = self.cursor.previous
        if prev:
            self.cursor.previous = prev.previous
            if prev.previous:
                prev.previous.next = self.cursor

    def delete(self):
        nxt = self.cursor.next
        if nxt:
            self.cursor.next = nxt.next
            if nxt.next:
                nxt.next.previous = self.cursor

text = textEditor()
inp = input("Enter Input : ").strip().split(',')
for i in inp:
    if i.split()[0] == 'I':
        text.insert(i.split()[-1])
    elif i.split()[0] == 'L':
        text.left()
    elif i.split()[0] == 'R':
        text.right()
    elif i.split()[0] == 'B':
        text.backspace()
    elif i.split()[0] == 'D':
        text.delete()
print(text)