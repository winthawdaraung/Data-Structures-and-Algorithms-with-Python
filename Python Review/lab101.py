# pi = 3.141592653589793
pi = 3.14159
r = input("r=")
try:
    r = float(r)
    a = pi * (r**2)
    print(f"Area={a}")
except:
    print("Not a number!")