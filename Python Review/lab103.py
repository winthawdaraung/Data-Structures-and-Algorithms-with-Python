print(" *** Summation of each digit ***")
number = input("Enter a positive number : ")
total = 0
for i in number:
    total += int(i)
print(f"Summation of each digit =  {total}")