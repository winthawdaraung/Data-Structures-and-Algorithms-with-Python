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

def get_order(ch):
    if ch == '^':
        return 3
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    else:
        return -1
def compare(inp, res = '', op = Stack()):
    open = '({['
    close = ')}]'
    flag = 0
    pemdas = "^*/+-"
    for i in range(len(inp)):
        ch = inp[i]
        if ch in open:
            op.push(ch)
            flag += 1
        elif ch in close:
            if flag > 0:
                while not match(op.seek(),ch):
                    res += op.pop()
                op.pop()
                flag -= 1
            else:
                return "Unmatched Bracket!!!"
        elif ch in pemdas:
            if (op.size() > 0):
                while (op.seek() not in open) and (op.seek() not in close) and (get_order(ch) <= get_order(op.seek())):
                    res += op.pop()
                    if op.size() == 0:
                        break
                op.push(ch)
            else: 
                op.push(ch)
        else:
            res += ch
    while op.size() > 0:
        res += op.pop()
    return res

def match(a, b):
    return (a == '(' and b ==')') or (a == '[' and b ==']') or (a == '{' and b =='}')


inp = input("Enter Infix : ")
s = compare(inp)
print(f"Postfix : {s}")