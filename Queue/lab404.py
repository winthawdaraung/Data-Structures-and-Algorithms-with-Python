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
    
dep, instr = input("Enter Input : ").strip().split('/')
staff_dict = {}
q_list = []
main_q = Queue()
for d in dep.split(','):
    # if d.split()[0] not in staff_dict.values():
    #     q_list.append([])
    staff_dict[d.split()[1]] = d.split()[0]
for i in instr.split(','):
    tmp_q = main_q.items
    if i[0] == 'D':
        if main_q.isEmpty():
            print('Empty')
        else:
            print(main_q.deQueue())
    elif i[0] == 'E':
        id = i.strip().split()[1]
        dep = staff_dict[id]
        # q_list[int(dep) - 1].append(id)
        # for j in range(len(q_list)):
        #     tmp_q += q_list[j]
        ind = -2
        # for j in tmp_q:
        #     if staff_dict[j] > dep:
        #         ind = tmp_q.index(j) - 1
        #         break
        for j in tmp_q:
            if staff_dict[j] == dep:
                ind = tmp_q.index(j) + 1
        if ind == -2:
            tmp_q.append(id)
        else:
            tmp_q.insert(ind, id)
        
        main_q = Queue(tmp_q)
    else:
        print("Error!")