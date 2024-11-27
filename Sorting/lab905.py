def partition(arr, low, high, pivot_func):
    pivot = pivot_func(low, high)
    pivot_value = arr[pivot]
    arr[pivot], arr[low] = arr[low], arr[pivot]
    i = low + 1
    comparisons = 0

    for j in range(low+1, high+1):
        comparisons += 1
        if arr[j] <= pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low] 
    return i - 1 , comparisons

def quicksort(arr, low, high, pivot_func):
    if low < high:
        pivot_index, count = partition(arr, low, high, pivot_func)
        left_count = quicksort(arr, low, pivot_index - 1, pivot_func)
        right_count = quicksort(arr, pivot_index + 1, high, pivot_func)
        return count + left_count + right_count
    return 0

def first_pivot(low, high):
    return low

def last_pivot(low, high):
    return high

def middle_pivot(low, high):
    return (low + high) // 2



print(" *** Quick sort ***")
input_str = input("Enter a sequence of integers : ")
arr = list(map(int, input_str.split()))

strategies = [
    ("First Pivot", first_pivot),
    ("Last Pivot", last_pivot),
    ("Middle Pivot", middle_pivot)
]

results = {}
for name, strategy in strategies:
    arr_copy = arr.copy()
    comparisons = quicksort(arr_copy, 0, len(arr_copy) - 1, strategy)
    results[name] = comparisons
print()
print("Number of comparisons for each pivot strategy:")
for strategy, comparisons in results.items():
    print(f"{strategy}: {comparisons} comparisons")

print("===== End of program =====")
