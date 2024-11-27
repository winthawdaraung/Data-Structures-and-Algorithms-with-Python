def FGV(arr, x):
    if arr:
        head, *tail = arr
        if head > x:
            return head
        else:
            return FGV(tail, x)
    return "No First Greater Value"

inp, val = input('Enter Input : ').split('/')
arr = list(map(int, inp.split()))
for k in val.split():
    print(FGV(sorted(arr), int(k)))