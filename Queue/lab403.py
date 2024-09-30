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
    
def errorCheck(inp, inp_error, dq_error, last, queue = Queue()):
    instrc = inp[0]
    action = ''
    try:
        count = int(inp[1:])
        if instrc == 'E':
            for i in range(1,count+1):
                last += 1
                queue.enQueue(f'*{last}')
        elif instrc == 'D':
            for i in range(1,count+1): 
                if queue.size() > 0:
                    queue.deQueue()
                else:
                    dq_error += 1    
        else:
            inp_error += 1
    except:
        inp_error += 1
    if instrc == 'E':
        action = 'Enqueue : '
    if instrc == 'D':
        action = 'Dequeue : '
    return inp_error, dq_error, queue, last, action

inp = input("input : ").strip().split(',')
inp_error,dq_error = 0,0
queue = Queue()
last = -1
for j in inp:
    inp_error, dq_error, queue, last, action = errorCheck(j,inp_error, dq_error, last, queue)
    print(f"Step : {j}")
    print(f"{action}{queue.items}")
    print(f"Error Dequeue : {dq_error}")
    print(f"Error input : {inp_error}")
    print("--------------------")