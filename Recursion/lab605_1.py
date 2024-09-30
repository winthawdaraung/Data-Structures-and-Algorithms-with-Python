def staircase(n, cur = 0):
    if n == 0:
        return "Not Draw!"
    if n == 1:
        return "_" * (n - 1) + "#" * (cur+1)
    if n == -1:
        return "_" * (cur) + "#" * (abs(n))
    if n > 0:
        return "_" * (n - 1) + "#" * (cur+1) + '\n' + staircase(n - 1, cur + 1)
    else:
        return "_" * (cur) + "#" * (abs(n)) + '\n' + staircase(n + 1, cur + 1)    
# print(" *** Stair case ***")
print(staircase(int(input("Enter Input : "))))
# print("===== End of program =====")