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

class Queue:
    def __init__(self, lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst
    def enQueue(self, new):
        self.items.append(new)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        if len(self.items) > 0:
            return False
        return True
    def size(self):
        return len(self.items)

    

def explode(inp,explosion_count, exploded_bomb = None):
    stack = Stack()
    if exploded_bomb == None:
        exploded_bomb = Queue()
    count = 0
    for i in inp:
        if stack.size() > 0:
            if i != stack.seek():
                count = 0
        stack.push(i)
        count += 1
        if count == 3:
            stack.pop()
            stack.pop()
            exploded_bomb.enQueue(stack.pop())
            count = 0
            explosion_count += 1
    remaining = ''.join(stack.items)
    if check_explodable(remaining):
        remaining,explosion_count,exploded_bomb,_ = explode(remaining,explosion_count,exploded_bomb)
    interrupt_items = ''.join(exploded_bomb.items)
    return remaining,explosion_count,exploded_bomb, interrupt_items
    
def add_blocks(inp, blocks = None):
    stack = Stack()
    if blocks == None:
        blocks = Queue()
    count = 0
    for i in inp:
        if stack.size() > 0:
            if i != stack.seek():
                count = 0
        stack.push(i)
        count += 1
        if count == 3:
            if not blocks.isEmpty():
                tmp = stack.pop()
                stack.push(blocks.deQueue())
                stack.push(tmp)
            count = 0
    return ''.join(stack.items)

def check_explodable(inp):
    stack = Stack()
    count = 0
    for i in inp:
        if stack.size() > 0:
            if i != stack.seek():
                count = 0
        stack.push(i)
        count += 1
        if count == 3:
            return True
    return False

    
            
normal, mirror = input("Enter Input (Normal, Mirror) : ").strip().split()
mirror_remaining,mirror_count,mirror_exploded,interrupt_items = explode(mirror[::-1],0)
normal_blocks = add_blocks(normal, mirror_exploded)
normal_remaining,normal_count,normal_exploded,_ = explode(normal_blocks,0)
no_remaining,no_count,no_exploded,_ = explode(normal,0)
print("NORMAL :")
print(len(normal_remaining))

if len(normal_remaining) > 0:
    print(normal_remaining[::-1])
else:
    print("Empty")


should = no_count - len(interrupt_items)
if should < 0:
    should = 0
if normal_count > should:
    interruptFailed = normal_count - no_count
    if interruptFailed == 0:
        interruptFailed = normal_count - should
    # interruptFailed = len(interrupt_items)
    # for k in interrupt_items:
    #     if k in normal_remaining:
    #         interruptFailed -= 1
    print(f"{normal_count - interruptFailed} Explosive(s) ! ! ! (NORMAL)")
    if interruptFailed > 0:
        print(f"Failed Interrupted {interruptFailed} Bomb(s)")
else:
    print(f"{normal_count} Explosive(s) ! ! ! (NORMAL)")

print("------------MIRROR------------")

print("MIRROR :"[::-1])
print(len(mirror_remaining))

if len(mirror_remaining) > 0:
    print(mirror_remaining[::-1])
else:
    print("Empty"[::-1])

print(f"(RORRIM) ! ! ! (s)evisolpxE {mirror_count}")

