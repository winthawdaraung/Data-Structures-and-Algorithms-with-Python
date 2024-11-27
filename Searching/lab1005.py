def box_used(weights, n, capacity):
    cur = 0
    box = 1
    for i in weights:
        if cur + i <= capacity:
            cur += i
        else:
            box += 1
            cur = i
    return box  

def min_capacity(weights, n):
    low = max(weights)
    high = sum(weights)

    while low < high:
        mid = (low + high) // 2
        if box_used(weights, n, mid)  <= n:
            high = mid
        else:
            low = mid + 1
    return low
    
            


weights, nbox = input("Enter Input : ").split('/')
weights = list(map(int, weights.split()))
print(f"Minimum weigth for {nbox} box(es) = {min_capacity(weights, int(nbox))}")