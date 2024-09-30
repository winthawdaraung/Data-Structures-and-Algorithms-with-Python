
class Stack():
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = list(lst)
    
    def push(self, ch):
        self.items.append(ch)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None
    
    def seek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)

def parking_lot_test(input_str):
    max_car, cars, op = input_str.strip().split('/')
    op, cur_car = op.strip().split()
    max_car = int(max_car)

    cars = list(map(int, cars.strip().split(',')))
    cur_car = int(cur_car)

    cars_stack = Stack(cars)
    if op.strip() == 'arrive':
        if cars_stack.size() < max_car:
            if cur_car not in cars_stack.items:
                cars_stack.push(cur_car)
                print(f"car {cur_car} arrive! : Add Car {cur_car}")
            else:
                print(f"car {cur_car} already in soi")
        else:
            print(f"car {cur_car} cannot arrive : Soi Full")
    elif op.strip() == 'depart':
        if cur_car in cars_stack.items:
            temp = Stack()
            while cars_stack.size() > 0:
                if cars_stack.seek() != cur_car:
                    temp.push(cars_stack.pop())
                else:
                    cars_stack.pop()
                    break
            while temp.size() > 0:
                cars_stack.push(temp.pop())
            print(f"car {cur_car} depart ! : Car {cur_car} was remove")
        else:
            print(f"car {cur_car} cannot depart : Dont Have Car {cur_car}")
    else:
        print("Invalid Operation")

    print(cars_stack.items)
    print()

print("******** Parking Lot ********")
inp = input("Enter max of car / car in soi / operation : ")
parking_lot_test(inp)