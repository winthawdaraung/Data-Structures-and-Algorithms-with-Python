def insertion_sort(inp, arr):
    arr.append(inp)
    # for i in range(1, len(l)): #from index 1 to last index
    #     iEle = l[i] #insert element
    #     for j in range(i, -1, -1):
    #         if iEle<l[j-1] and j > 0:
    #             l[j] = l[j-1]
    #         else:
    #             l[j] = iEle
    #             break
    for ind,n in enumerate(arr):
        if n > i:
            arr[ind] = i
            break
    for j in range(ind + 1, len(arr)):
        n, arr[j] = arr[j], n
        

    return find_medium(arr)
    
def find_medium(arr):
    pos = len(arr) 
    if pos % 2 == 1:
        pos = pos // 2
        return float(arr[pos])
    else:
        pos = pos // 2
        return (arr[pos] + arr[pos-1]) / 2
    
l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    arr = []
    org = []
    for i in l:
        org.append(i)
        mediam = insertion_sort(i, arr)
        print(f"list = {org} : median = {mediam}")