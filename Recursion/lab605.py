def staircase(n):
    s = ''
    def recursion(d,h,s, sym):
        if d < 0:
            return s
        return s + sym[0] * d + sym[1] * h + recursion( d-1, h + 1, '\n' if d > 0 else '',sym)
    if n > 0:
        return recursion(n-1, 1,s,"_#")
    else:
        return recursion(abs(n), 0,s,"#_")
# print(" *** Stair case ***")
print(staircase(int(input("Enter Input : "))))
# print("===== End of program =====")