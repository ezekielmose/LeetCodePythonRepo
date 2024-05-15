def is_palindrome (string):
    reverseing_string= string [::-1]
    return string ==reverseing_string
words="madam"
if is_palindrome(words):
    print(f"{words} is a palindrome")
else:
    print(f" {words} is not a palindrome")