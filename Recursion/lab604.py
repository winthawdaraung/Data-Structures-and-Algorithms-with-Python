#towerOfHanoi
# def move(n, A, B, C,rows):
#     if n == 1:
#         print(f"move 1 from  {A[0]} to {C[0]}")
#         C.append(A.pop())
#         print_tower(rows, A, B, C, rows)
#     else:
#         move(n-1, A, C, B,rows)
#         print(f"move {n} from  {A[0]} to {C[0]}")
#         C.append(A.pop())
#         print_tower(rows, A, B, C, rows)
#         move(n - 1, B, A, C,rows)

def move(n, A, B, C,rows):
    if n == 1:
        print(f"move 1 from  {A[0]} to {C[0]}")
        C.append(A.pop())
        print_tower(rows, A, B, C, rows)
    else:
        move(n-1, A, B, C,rows)
        print(f"move {n} from  {A[0]} to {C[0]}")
        C.append(A.pop())
        print_tower(rows, A, B, C, rows)
        move(n - 1, B, C, A,rows)

def print_tower(n, A, B, C, maxrow):        
    if A[0] != "A" or B[0] != "B" or C[0] != "C": 
        a,b,c = A, B, C
        if A[0] != "A":
            A = ["A"] + list(b[1:] if b[0] == "A" else c[1:])
        if B[0] != "B":
            B = ["B"] + list(a[1:] if a[0] == "B" else c[1:])
        if C[0] != "C":
            C = ["C"] + list(a[1:] if a[0] == "C" else b[1:])
    if n == maxrow:
        print("|  |  |")
    if n > 0:
        print_row(n, A, B, C)
        print_tower(n - 1, A, B, C, maxrow)


def print_row(row, A,B, C):
    print(str(A[row])+' ' if len(A) > row else "| "
        , ' '+str(B[row])+' ' if len(B) > row else " | "  
        , ' '+str(C[row])+' ' if len(C) > row else " | " ,sep = '')

n = int(input("Enter Input : "))
A = ["A"]+ list(range(n, 0, -1))
B = ["B"]
C = ["C"]
print_tower(n,A,B,C,n)
move(n,A,B,C,n)

