class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        newNode = Node(val)
        if self.root:
            cur = self.root
            self.rinsert(cur, newNode)
        else:
            self.root = newNode
        return self.root

    def rinsert(self, cur, node):
        if node.data < cur.data:
            if cur.left:
                self.rinsert(cur.left, node)
            else:
                cur.left = node
        else:
            if cur.right:
                self.rinsert(cur.right, node)
            else:
                cur.right = node

    # def delete(self, r, data):
    #     if r is None:
    #         print("Error! Not Found DATA")
    #         return None

    #     if data < r.data:
    #         r.left = self.delete(r.left, data)
    #     elif data > r.data:
    #         r.right = self.delete(r.right, data)
    #     else:
    #         if r.left is None:
    #             return r.right
    #         elif r.right is None:
    #             return r.left
    #         sus = self.get_successor(r)
    #         r.data = sus.data 
    #         r.right = self.delete(r.right, sus.data)  
    #     return r 

    def get_successor(self, cur):
        cur = cur.right
        while cur and cur.left:
            cur = cur.left
        return cur

    def delete(self, root, data):
        if not root:
            print("Not Found DATA")
            return None
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            sus = self.get_successor(root)
            root.data = sus.data
            root.right = self.delete(root.right, sus.data)
        return root

def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
root = None
for i in data:
    cmd, node = i.strip().split()
    if cmd == 'i':
        print(f"insert {node}")
        root = tree.insert(int(node))
        # print(f"insert {node}")
    elif cmd == 'd':
        print(f"delete {node}")
        root = tree.delete(root, int(node))
        tree.root = root
        
    else:
        print("Error!")
    printTree90(root)
