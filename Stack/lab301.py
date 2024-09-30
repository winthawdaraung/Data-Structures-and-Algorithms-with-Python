class Stack():
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = list(lst)
    def push(self,ch):
        self.items.append(ch)
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None
    def seek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None
    def size(self):
        return len(self.items)

def paramatch(s):
    param = Stack()
    param_cl = Stack()
    op = '(['
    cl = ')]'
    for i in s:
        if i in op:
            param.push(i)
        elif i in cl:
            if match(param.seek(),i):
                param.pop()
            else:
                param_cl.push(i)
    return param_cl.size() + param.size()

def match(a, b):
    return (a == '(' and b ==')') or (a == '[' and b ==']')

inp = input("Enter Input : ")
count = paramatch(inp)
print(count)
if count == 0 and len(inp) > 0:
    print("Perfect ! ! !")