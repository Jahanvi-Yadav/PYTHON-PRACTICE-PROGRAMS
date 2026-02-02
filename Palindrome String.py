#WAP TO CHECK WHETHER ENTERED STRING IS PALINDROME OR NOT.
string = str(input("Enter a String Here: "))
string = string.lower()
reversed_string = string[::-1]

# Check if the string is equal to its reverse
if string == reversed_string:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
