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
        self.height = 0

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
    
    def insert(self, root, data):
        if not root:
            root = Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return root
    
    def search_subtree(self, root, key):
        if root:
            if key == root.data:
                return root
            elif key < root.data:
                return self.search_subtree(root.left, key)
            else:
                return self.search_subtree(root.right, key)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def get_height(self, root):
        return root.height if root else 0

inp, num  = input("Enter Input : ").split('/')
inp = inp.split()
num = int(num)
bst = BST()
for i in inp:
    bst.root = bst.insert(bst.root, int(i))
bst.printTree(bst.root)
num_root = bst.search_subtree(bst.root, num)
print("--------------------------------------------------")
# print(len([i for i in inp if int(i) <= num]))
print(bst.get_height(num_root))

