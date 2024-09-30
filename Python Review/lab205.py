class funString():
    def __init__(self,string = ""):
        self.string = string
        

    def __str__(self):

        return self.string

    def size(self) :
        count = 0
        for i in self.string:
            count += 1
        return count
    def changeSize(self):
        res = ''
        for i in self.string:
            if ord(i) >= 97 and ord(i) <= 122:
               res += chr(ord(i) - 32)
            else:
                res += chr(ord(i) + 32)
        return res

    def reverse(self):
        s = self.string[::-1]
        return s

    def deleteSame(self):
        res = ''
        s = self.string
        for i in s:
           if i not in res:
               res += i
        return res



str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())
elif str2 == "2":  print(res.changeSize())
elif str2 == "3" : print(res.reverse())
elif str2 == "4" : print(res.deleteSame())