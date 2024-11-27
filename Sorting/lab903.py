# Receive a single integer input and display the result as follows:

# - If the input is in ascending order without any duplicate digits, display "Metadrome".

# - If the input is in ascending order with duplicate digits, display "Plaindrome".

# - If the input is in descending order without any duplicate digits, display "Katadrome".

# - If the input is in descending order with duplicate digits, display "Nialpdrome".

# - If all digits in the input are the same, display "Repdrome".

# - If none of the above conditions are met, display "Nondrome".

# ****** Do not use built-in sorting functions. Write your own sort function instead.

def check(arr):
    initEle = arr[0]
    state = False
    duplicate = False
    all_dup = True
    if arr[1]:
        if initEle > arr[1]:
            state = 'd' 
            for i in range(1, len(arr), 1):
                if arr[i] > initEle:
                    state = False
                    break
                if arr[i] == initEle:
                    duplicate = True
                else:
                    all_dup = False
                initEle = arr[i]
        else:
            state = 'a'
            for i in range(1, len(arr), 1):
                if arr[i]  < initEle:
                    state = False
                    break
                if arr[i] == initEle:
                    duplicate = True
                else:
                    all_dup = False
                initEle = arr[i]
    if state == 'a':
        if duplicate:
            if all_dup:
                return "Repdrome"
            return "Plaindrome"
        return "Metadrome"
    elif state == 'd':
        if duplicate:
            if all_dup:
                return "Repdrome"
            return "Nialpdrome"
        return "Katadrome"
    return "Nondrome"
    
inp = list(input("Enter Input : "))
inp = list(map(int, inp))
print(check(inp))