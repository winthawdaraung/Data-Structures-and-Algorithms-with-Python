class TreeNode(object): 
    def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()        

    def __str__(self):
        return str(self.data)

    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height            

    def getHeight(self, node):
        return -1 if node == None else node.height
        
    def balanceValue(self):    
        return self.getHeight(self.right) - self.getHeight(self.left)
  
class AVL_Tree(object): 
    def __init__(self, root = None):
        self.root = None if root is None else root

    def insert(self, data):
        self.root = self._insert(self.root, int(data))
    
    def _insert(self, root, data):
        if not root:
            return TreeNode(data)
        
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        
        root.setHeight()
        root = self.rebalance(root)
        return root
    
    def rebalance(self, root):
        bf = root.balanceValue()
        if bf < -1: #left heavy
            if root.left.balanceValue() > 0:
                root.left = self.rotateRightChild(root.left)
            return self.rotateLeftChild(root)
        elif bf > 1: #right heavy
            if root.right.balanceValue() < 0:
                root.right = self.rotateLeftChild(root.right)
            return self.rotateRightChild(root)
        return root
    
    def rotateLeftChild(self, z):
        if z.left:
            y = z.left
            z.left = y.right
            y.right = z
            z.setHeight()
            y.setHeight()
        return y
    
    def rotateRightChild(self, z):
        if z.right:
            y = z.right
            z.right = y.left
            y.left = z
            z.setHeight()
            y.setHeight()
            return y
        return z 
    
    def delete(self, r, data):
        if r is None:
            print("Error! Not Found DATA")
            return None

        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                return r.right
            elif r.right is None:
                return r.left
            sus = self.get_successor(r)
            r.data = sus.data 
            r.right = self.delete(r.right, sus.data)
        r.setHeight()
        r = self.rebalance(r)
        return r 

    def get_successor(self, cur):
        cur = cur.right
        while cur and cur.left:
            cur = cur.left
        return cur
    
    def get_biggest(self):
        if self.root:
            cur = self.root
            data = cur.data
            while cur and cur.right:
                cur = cur.right
                data = cur.data
            return data
        
        
    def level_order(self):
        if self.root is None:
            return
        queue = []
        queue.append([self.root, 0])
        max_level = self.root.getHeight(self.root) + 1
        level_before = 0
        space = [0] * (max_level)
        for i in range(max_level):
            space[i] = (2 ** (max_level - i)) * 4
        while len(queue) > 0:
            node, level = queue.pop(0)
            if node.left is not None:
                queue.append([node.left, level + 1])
            else:
                if level + 1 < max_level:
                    queue.append([TreeNode(' '), level + 1])
            if node.right is not None:
                queue.append([node.right, level + 1])
            else:
                if level + 1 < max_level:
                    queue.append([TreeNode(' '), level + 1])
            if level_before != level:
                print()
                level_before = level
            print(f'{node.data:^{space[level]}}', end='')

        print()
        print()
        print('-' * 30)


myTree = AVL_Tree() 
root = None

data = input("Enter numbers to insert: ").split()
print("AVL Tree (Level Order):")
for e in data:
    root = myTree.insert(e)
myTree.level_order()

while(myTree.get_biggest()):
    myTree.root = myTree.delete(myTree.root, myTree.get_biggest())
    myTree.level_order()
    
# while(myTree.root):
#     myTree.root = myTree.delete(myTree.root, myTree.root.data)
#     # printTree(myTree.root)
#     myTree.level_order()
#     # print("------------------------------")