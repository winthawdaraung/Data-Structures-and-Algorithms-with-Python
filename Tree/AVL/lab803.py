class TreeNode(object): 
    def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = 0#self.setHeight()        

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
        bf = root.balanceValue()
        if bf < -1:
            if data < root.left.data:
                print("Right Right Rotation")
                return self.rotateLeftChild(root)
            else:
                root.left = self.rotateRightChild(root.left)
                print("Left Right Rotation")
                return self.rotateLeftChild(root)
        elif bf > 1:
            
            if data > root.right.data:
                print("Left Left Rotation")
                return self.rotateRightChild(root)
            else:
                root.right = self.rotateLeftChild(root.right)
                print("Right Left Rotation")
                return self.rotateRightChild(root)
        return root
    
    def rotateLeftChild(self, a):
        if a.left:
            tmp = a.left
            tmp2 = tmp.right
            tmp.right = a
            a.left = tmp2
            a.setHeight()
            tmp.setHeight()
            return tmp
        return a
    
    def rotateRightChild(self, a):
        if a.right:
            tmp = a.right
            tmp2 = tmp.left
            tmp.left = a
            a.right = tmp2
            a.setHeight()
            tmp.setHeight()
            return tmp
        return a 

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None
print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.insert(e)
    printTree90(myTree.root)
    print("====================")