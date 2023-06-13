class LengthString:
    def lengthLastStr(self, s:str)->str:
        stLength=len(s)-1

        while stLength >=0 and s[stLength] ==' ':
            stLength -= 1
        lastIdex= stLength
        while lastIdex >=0 and s[lastIdex] != ' ':
            lastIdex -=1

        return  stLength-lastIdex

if __name__ == '__main__':
    c=LengthString()
    print(c.lengthLastStr('Hello Mr Jaohnson'))

