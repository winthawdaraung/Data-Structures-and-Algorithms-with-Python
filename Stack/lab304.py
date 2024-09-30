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

class calculator():
    
    def __init__(self, stack = Stack()) -> None:
        self.instinst = ['+','-','*','/','DUP','POP','PSH']
        self.stack = stack
        
    def run(self, instructions, num = None):
        for instruction in instructions:
            if instruction.isnumeric():
                self.stack.push(int(instruction))
            elif instruction == '+':
                if self.stack.size() >= 2:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    self.stack.push(a+b)
            elif instruction == '-':
                if self.stack.size() >= 2:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    self.stack.push(a-b)
            elif instruction == '*':
                if self.stack.size() >= 2:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    self.stack.push(a*b)
            elif instruction == '/':
                if self.stack.size() >= 2:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    self.stack.push(a/b)
            elif instruction == 'DUP':
                if self.stack.size() >= 1:
                    self.stack.push(self.stack.seek())
            elif instruction == 'POP':
                if self.stack.size() >= 1:
                    self.stack.pop()
            elif instruction == 'PSH':
                if num != None:
                    self.stack.push(num)
                else:
                    return "Put a number to push onto stack!"
            else:
                return f"Invalid instruction: {instruction}"
        if self.stack.size() == 0:
            return 0
        try:
            return int(self.stack.pop())
        except:
            return self.stack.pop()


print("* Stack Calculator *")
inp = input("Enter arguments : ").split()
cal = calculator()
print(cal.run(inp))