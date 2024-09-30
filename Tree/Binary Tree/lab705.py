# Write a Python program to accept an input, then show it in expression tree.

#   - input is in postfix format

#   - only 4 types of operators +-*/

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 

class Stack():
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = list(lst)
    def push(self,ch):
        self.items.append(ch)
    def pop(self):
        return self.items.pop()
    def seek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0

def printTree90(node, level=0):
    if node is not None:
        printTree90(node.right, level + 1)
        print('     ' * level, node.data)
        printTree90(node.left, level + 1)

def inorder(root,s = ''):
    if root:
        if root.left or root.right:
            s += "("
        s = inorder(root.left,s)
        s += str(root.data)
        s = inorder(root.right,s)
        if root.left or root.right:
            s += ")"
    return s

def preorder(root,s = ''):
    if root:
        s += str(root.data)
        s = preorder(root.left,s)
        s = preorder(root.right,s)
    return s

inp = input("Enter Postfix : ")
stack = Stack()
for i in inp:
    if i in "+-*/":
        node = Node(i)
        node.right = stack.pop()
        node.left = stack.pop()
        stack.push(node)
    else:
        stack.push(Node(i))
root = stack.pop()
print("Tree :")
printTree90(root)
print("--------------------------------------------------")
print(f"Infix : {inorder(root)}")
print(f"Prefix : {preorder(root)}")