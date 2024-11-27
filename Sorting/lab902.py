def pos_sort(l):
    for last in range(len(l)-1,0,-1):
        swapped = False
        for i in range(last):
            nxt = i+1
            if l[i] >= 0:
                while nxt+1 < len(l) and l[nxt] < 0:
                    nxt += 1
                if l[i] > l[nxt] and l[nxt] >= 0:
                    l[i], l[nxt] = l[nxt], l[i]
                    swapped = True
        if not swapped:
            break
    l = list(map(str, l))
    print(' '.join(l))
inp = input("Enter Input : ").strip().split()
inp = list(map(int, inp))
pos_sort(inp)