def RANGE(*args):
    res = tuple()
    if len(args) >= 1 and len(args) <=3:
        start = 0
        step = 1
        stop = args[0]
        if len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
        while start < stop:
            res = res + (float(f"{start:.3f}"),)
            start += step
    return res

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    k = RANGE(n[0])
    print(RANGE(n[0]))
elif len(n) == 2:
    print(RANGE(n[0], n[1]))
elif len(n) == 3:
    print(RANGE(n[0], n[1], n[2]))
