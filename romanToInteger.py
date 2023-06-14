class RomInt:
    def romansToIntegers(self, st: str)->int:
        dictiom= {'I': 1, 'V':5 , 'X' : 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}

        strLeng= len(st)

        #variable to store string

        storStr= dictiom[st[strLeng-1]]

        #looping from right to left

        for i in range (strLeng-2, -1, -1):
            if dictiom[st[i]]>=dictiom[st[i+1]]:
                storStr += dictiom[st[i]]
            else:
                storStr -= dictiom[st[i]]
        return storStr
if __name__ == '__main':
    c=RomInt()
    print(c.romansToIntegers('III'))
    print(c.romansToIntegers('IV'))
    print(c.romansToIntegers('L'))




