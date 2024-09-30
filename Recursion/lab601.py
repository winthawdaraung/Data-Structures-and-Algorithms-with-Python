def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

print(" *** Find fibonacci sequence ***")
n = int(input("Enter n : "))

print(f"fibo({n}) = {fibonacci(n)}")
print("===== End of program =====")