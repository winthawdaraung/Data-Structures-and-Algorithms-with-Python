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
    
inp = list(input("Enter people : ").strip())

main_q = Queue(inp)
cashier1 = Queue()
cashier2 = Queue()
time1 = 0
time2 = 0
for i in range(len(inp)):
    if time1 > 0 and time1 % 3 == 0:
        cashier1.deQueue()
    if time2 > 0 and time2 % 2 == 0:
        cashier2.deQueue()
    
    if cashier1.size() < 5:
        cashier1.enQueue(main_q.deQueue())
    else:
        cashier2.enQueue(main_q.deQueue())
    
    if cashier1.size() > 0:
        time1 += 1
    if cashier2.size() > 0:
        time2 += 1
    print(f"{i+1} {main_q.items} {cashier1.items} {cashier2.items}")