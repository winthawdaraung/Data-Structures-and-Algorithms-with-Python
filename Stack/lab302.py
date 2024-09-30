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
    op = '([{'
    cl = ')]}'
    for i in s:
        if i in op:
            param.push(i)
        elif i in cl:
            if param.size() > 0:
                if match(param.seek(),i):
                    param.pop()
                else:
                    return "Unmatch open-close"
            else:
                param_cl.push(i)
    if len(s) > 0:
        if param_cl.size() + param.size() == 0:
            return "MATCH"
        elif param.size() > 0:
            return f"open paren excess   {param.size()} : {''.join(param.items)}"
        else:
            return "close paren excess"

def match(a, b):
    return (a == '(' and b ==')') or (a == '[' and b ==']') or (a == '{' and b =='}')

inp = input("Enter expresion : ")
status = paramatch(inp)
if len(inp) > 0:
    print(f"{inp} {status}")