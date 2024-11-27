def bubble(l):
    step = 1
    for last in range(len(l)-1, 0, -1):
        swapped = False
        move = None
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                move = l[i+1]
                swapped = True
        if not swapped or step == len(l) - 1:
            break
        print(f"{step} step : {l} move[{move}]")
        step += 1
    print(f"last step : {l} move[{move}]")

inp = input("Enter Input : ").strip().split()
inp = list(map(int, inp))
bubble(inp) 