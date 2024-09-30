print(" *** Wind classification ***")
speed = input("Enter wind speed (km/h) : ")
try:
    speed = float(speed)
    if speed >= 0 and speed <= 51.99:
        cat = "Breeze"
    elif speed >= 52 and speed <= 55.99:
        cat = "Depression"
    elif speed >= 56 and speed <= 101.99:
        cat = "Tropical Storm"
    elif speed >= 102 and speed <= 208.99:
        cat = "Typhoon"
    elif speed >= 209:
        cat = "Super Typhoon"
    print(f"Wind classification is {cat}.")
except:
    print("Speed must be a number!")