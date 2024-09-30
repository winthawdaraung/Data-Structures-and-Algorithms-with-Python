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

# def explode(inp,start, n = 3):
#     inp = list(inp)
#     prev = inp[0]
#     explosion_count = 0
#     count = 1
#     start = 0
#     exploded_bomb = []
#     for i in inp[1:]:
#         if i == prev:
#             count += 1
#         else:
#             start = inp.index(i)
#             count = 0
#         if count == 3:
#             exploded_bomb.append(i)
#             inp.pop(start)
#             inp.pop(start + 1)
#             inp.remove(i)
#             explosion_count += 1
#         prev = i
#     remaining = ''.join(inp)
#     return remaining,explosion_count,exploded_bomb

def explode(inp):
    inp = list(inp)
    explosion_count = 0
    exploded_bomb = Queue()
    if len(inp) >= 3:
        for i in range(len(inp) - 2):
            if check_explode(inp[i:i+3]):
                exploded_bomb.enQueue(inp[i])
                new = inp[:i] + inp[i+3:]
                explosion_count += 1
    remaining = ''.join(inp)
    return remaining,explosion_count,exploded_bomb

def check_explode(window):
    return all(i == window[0] for i in window)
    
def add_blocks(inp:str, blocks: Queue):
    inp = list(inp)
    if len(inp) >= 3 and not blocks.isEmpty():
        for j in range(len(inp) - 2):
            if check_explode(inp[j:j+3]):
                if not blocks.isEmpty():
                    inp.insert(j + 1, blocks.deQueue())
    return ''.join(inp)

normal, mirror = input("Enter Input (Normal, Mirror) : ").strip().split()
mirror_remaining,mirror_count,mirror_exploded = explode(mirror[::-1])
normal_blocks = add_blocks(normal, mirror_exploded)
normal_remaining,normal_count,normal_exploded = explode(normal)
print("NORMAL :")
print(len(normal_remaining))
print(normal_remaining)
print(normal_count)
print("------------MIRROR------------")
print("MIRROR :"[::-1])
print(len(normal_remaining))
print(normal_remaining[::-1])
print(normal_count)