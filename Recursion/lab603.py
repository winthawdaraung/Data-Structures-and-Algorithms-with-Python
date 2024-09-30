def gcd(n,d):
    n = abs(n)
    d = abs(d)
    if d == 0:
        return n
    if n % d == 0:
        return d
    return gcd(d, n%d)

n1, n2 = input("Enter Input : ").strip().split()
n1 = int(n1)
n2 = int(n2)
n = max(n1,n2)
d = min(n1,n2)
if d == 0 and n == 0:
    print("Error! must be not all zero.")
else:
    print(f"The gcd of {n} and {d} is : {gcd(n,d)}")