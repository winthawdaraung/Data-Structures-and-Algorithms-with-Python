class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        
    # def insert(self, data):
    #     newNode = Node(data)
    #     if self.root:
    #         self.ninsert(self.root,data)
    #     else:
    #         self.root = newNode
    #     return self.root

    # def ninsert(self,cur, data, level = 0):
    #     if cur.right == None and cur.left == None:
    #         if level >= self.height:
    #             self.height += 1
    #     if data < cur.data:
    #         if cur.left == None:
    #             cur.left = Node(data)
    #         else:
    #             self.ninsert(cur.left,data, level+1)
    #     else:
    #         if cur.right == None:
    #             cur.right = Node(data)
    #         else:
    #             self.ninsert(cur.right,data, level+1)

    def insert(self, data, root = None):
        if not root:
            root =  Node(data)
        elif data < root.data:
            root.left = self.insert(data, root.left)
        else:
            root.right = self.insert(data, root.right)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return root

    def get_height(self, root):
        if root:
            return root.height
        return 0
        
    # def printTree(self, node, level = 0):
    #     if node != None:
    #         self.printTree(node.right, level + 1)
    #         print('     ' * level, node)
    #         self.printTree(node.left, level + 1)

inp = input("Enter Input : ").split()
bst = BST()
for i in inp:
    bst.root = bst.insert(int(i), bst.root)
    # print(f"Height of this tree is : {bst.get_height(bst.root)}")
print(f"Height of this tree is : {bst.get_height(bst.root) - 1}")