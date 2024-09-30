class translator:
    
    def deciToRoman(self, num):
        src_1 = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40,'X':10,'IX':9,'V':5,'IV':4, 'I':1}
        src_2 = {v:k for k,v in src_1.items()}
        res = ""
        l = len(str(num)) - 1
        for i in range(len(str(num))):
            n = int(str(num)[i]) * (10**l)
            l -= 1
            while n > 0:
                if n in src_2:
                    res += src_2[n]
                    n -= src_1[src_2[n]]
                else:
                    for k,v in src_1.items():
                        if v < n:
                            res += k
                            n -= v
                            break
        return res


    def romanToDeci(self, s):
        src_1 = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40,'X':10,'IX':9,'V':5,'IV':4, 'I':1}
        num = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in src_1:
                num += src_1[s[i:i+2]]
                i += 2
            else:
                num += src_1[s[i]]
                i += 1
        return num


print(" *** Decimal to Roman ***")
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))