#Palindrome

word = input("Enter a string:")
if word == (word [::-1]):
    print(f"The word, {word} is palindrome")
else:
    print("It is not palindrome")