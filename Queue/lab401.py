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

def add_delete(inp,queue = Queue()):
    for i in inp:
        instr = i.strip().split()[0]
        if instr.upper() == 'E':
            new = i.strip().split()[1]
            queue.enQueue(new)
            print(f"Add {new} index is {queue.size()-1}")
        elif instr.upper() == 'D':
            if queue.size() > 0:
                print(f"Pop {queue.deQueue()} size in queue is {queue.size()}")
            else:
                print("-1")
    if queue.size() > 0:
        print(f"Number in Queue is :  {queue.items}")
    else:
        print('Empty')

inp = input("Enter Input : ").strip().split(',')
add_delete(inp)
