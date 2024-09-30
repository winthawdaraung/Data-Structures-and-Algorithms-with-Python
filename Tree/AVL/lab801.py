class AVLTree:

    class AVLNode:
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

    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = self._add(self.root, int(data))
    
    def _add(self, root, data):
        if not root:
            return self.AVLNode(data)
        
        if data < root.data: 
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)
        
        root.setHeight()
        bf = root.balanceValue()
        if bf < -1:
            if data < root.left.data:
                return self.rotateLeftChild(root)
            else:
                root.left = self.rotateRightChild(root.left)
                return self.rotateLeftChild(root)
        elif bf > 1:
            if data > root.right.data:
                return self.rotateRightChild(root)
            else:
                root.right = self.rotateLeftChild(root.right)
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

    def postOrder(self):
        root = self.root
        self._postOrder(root)
        print()

    def _postOrder(self, root):
        if root:
            self._postOrder(root.left)
            self._postOrder(root.right)
            print(root.data,end=' ')

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)
 

avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
        # avl1.printTree()

    elif i[:2] == "PR":
        avl1.printTree()

    elif i[:2] == "PO":
        print("AVLTree post-order : ",end='')
        avl1.postOrder()