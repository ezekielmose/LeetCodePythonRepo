def is_prime (n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n %2==0:
            return False
    return  True
nums=20
if is_prime(nums):
    print(f"{nums} is a prime number")
else:
    print(f"{nums} is not a prime number")
