class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root:
            self.ninsert(self.root,data)
        else:
            self.root = newNode
        return self.root

    def ninsert(self,cur, data):
        if data < cur.data:
            if cur.left == None:
                cur.left = Node(data)
            else:
                self.ninsert(cur.left,data)
        else:
            if cur.right == None:
                cur.right = Node(data)
            else:
                self.ninsert(cur.right,data)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)