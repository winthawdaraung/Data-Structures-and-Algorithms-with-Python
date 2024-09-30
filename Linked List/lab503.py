class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = node(l[0], l[1])
    cur = head
    for i in range(1, len(l)):
        if i + 1 < len(l):
            cur.next = node(l[i],l[i+1])
        else:
            cur.next = node(l[i],None)
        cur = cur.next
    return head
    

def printList(H):
    s = ""
    while H != None:
        s += str(H.data) + " "
        H = H.next
    print(s)

def mergeOrderesList(p,q):
    lst = []
    while p or q:
        if p and q:
            if p.data <= q.data:
                lst.append(p.data)
                p = p.next
            else:
                lst.append(q.data)
                q = q.next
        else:
            if q == None:
                lst.append(p.data)
                p = p.next
            else:
                lst.append(q.data)
                q = q.next
    return createList(lst)

L1,L2 = input("Enter 2 Lists : ").strip().split()
L1 = list(map(int, L1.split(',')))
L2 = list(map(int, L2.split(',')))

#################### FIX comand ####################   
# input only a number save in L1,L2
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)