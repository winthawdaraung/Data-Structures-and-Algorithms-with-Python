def length(txt):     
    def recursive(s, l = 0, sym = "*"):
        if not s:
            return f"\n{l}"
        return s[0] + sym + recursive(s[1:], l+1, "~" if sym=="*" else "*")
    return recursive(txt)
print("",length(input("Enter Input : ")),sep="")
