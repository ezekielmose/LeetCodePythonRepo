def find_factorial (n):
    if n==0:
        return 1
    else:
        return n * find_factorial(n-1)
numb=6
result=find_factorial(numb)
print(f"the factorial of {numb} is : {result} ")
