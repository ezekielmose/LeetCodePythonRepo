def find_largest(number):
    largest = number[0]
    for num in number:
        if num>largest:
            largest=num
    return largest
nums= [10, 88, 43,7,9,18]
largest_n= find_largest(nums)
print("the largest number is: ", largest_n)