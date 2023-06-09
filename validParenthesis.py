#create a function
def validParenthesis(s:str)->bool:
    #declare left sysmbol as an empty array
    leftSymbol=[]
    #loop through the string
    for c in s:
        if c in ['(', '{', '[']:
            leftSymbol.append(c)
        elif c =='(' and len(leftSymbol) !=0 and leftSymbol==')':
            leftSymbol.pop()
        elif c=='{' and len(leftSymbol)!=0 and leftSymbol=='}':
            leftSymbol.pop()
        elif c== '[' and len(leftSymbol) !=0 and leftSymbol ==']':
            leftSymbol.pop()
        else:
            return  False
    return leftSymbol ==[]
if __name__=='__main__':
    print(validParenthesis("[]"))
    print(validParenthesis("{}"))
    print(validParenthesis("([}"))
    print(validParenthesis("[()"))
    print(validParenthesis("()[]{}"))
    print(validParenthesis("(]"))
    print(validParenthesis("([)]"))
    print(validParenthesis("{[]}"))

