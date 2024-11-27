def quick_sort(arr, left, right, count):
    if left < right:
        p_ind = left
        pivot = arr[p_ind]
        i = left + 1
        j = right
        while i < j and arr[i] < pivot:
                count += 1
                i += 1
        while i <= j and arr[j] > pivot:
                j -= 1
                count += 1
        
        while arr[i] < arr[j]:
            swap(arr, i, j)
            i += 1
            j += 1
        swap(arr, p_ind, j)
        count = quick_sort(arr, left, j-1, count)
        count = quick_sort(arr, j+1, right, count)
    return count

def quick_sort_last(arr, left, right, count):
    if left < right:
        p_ind = right
        pivot = arr[p_ind]
        i = left
        j = right -1 
        while i <= j and arr[i] < pivot:
                count += 1
                i += 1
        while i < j and arr[j] > pivot:
                j -= 1
                count += 1
        while arr[i] < arr[j]:
            count += 1
            swap(arr, i, j)
            i += 1
            j += 1
        swap(arr, p_ind, i)
        count = quick_sort_last(arr, left, i-1, count)
        count = quick_sort_last(arr, i+1, right, count)
    return count + 1

def quick_sort_mid(arr, left, right, count):
    if left < right:
        mid = (right + left) // 2
        p_ind = mid
        pivot = arr[p_ind]
        for i in range(left, mid):
            if arr[i] < pivot:
                swap(arr, i, i -1)
                p_ind += 1
                count += 1
        swap(arr, p_ind, mid)
        mid = p_ind
        for i in range(right, mid, -1):
            if arr[i] > pivot:
                swap(arr, i, i + 1)
                p_ind -= 1
                count += 1
        swap(arr, p_ind, mid)
        quick_sort_last(arr, left, p_ind -1, count)
        quick_sort_last(arr, p_ind+1, right, count)
    return count

def swap(arr,i,j):
    arr[i],arr[j] = arr[j], arr[i]

print(" *** Quick sort ***")
inp = input("Enter a sequence of integers : ").strip().split()
inp = list(map(int, inp))
print()
inp2 = inp.copy()
inp3 = inp.copy()
print("Number of comparisons for each pivot strategy:")
print(f"First Pivot: {quick_sort(inp,0,len(inp)-1,0)} comparisons")
print(f"Last Pivot: {quick_sort_last(inp2,0,len(inp2)-1,0)} comparisons")
print(f"Middle Pivot: {quick_sort_mid(inp3,0,len(inp3)-1,0)} comparisons")
print("===== End of program =====")