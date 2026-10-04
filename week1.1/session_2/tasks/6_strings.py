# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}")
# converts the letters in the string to lowercase
print(f"Modified String 2: {user_string.upper()}")
# converts the letters in the string to uppercas
print(f"Modified String 3: {user_string.strip()}")
# removes the spaces at the beginning and end of the string
print(f"Modified String 4: {user_string.replace('a', '@')}")
#replaces all 'a' with '@' in the string
print(f"Modified String 5: {user_string.capitalize()}")
# capitalizes the first letter of the string
print(f"Modified String 6: {user_string[::-1]}")
#  reverses the string
print(f"Modified String 7: {user_string.title()}")
# capitalizes the first letter of each word in the string
print(f"Modified String 8: {len(user_string)}")
# print the length of the string
print(f"Modified String 9: {user_string.find('a')}")
# find the first occurence of 'a' in the string
print(f"Modified String 10: {user_string.count('a')}")
# count the number of letters 'a' in the string
print(f"Modified String 11: {user_string.startswith('Hello')}")
# checks the string starts with 'Hello', returns True or False
print(f"Modified String 12: {user_string.endswith('!')}")
# checks the string ends with '!', returns True or False
print(f"Modified String 13: {user_string.isalnum()}")
# checks is the string only consists oof letters and numbers, returns True or False
print(f"Modified String 14: {user_string.isalpha()}")
# checks if the string only consists of letters, returns True or False
print(f"Modified String 15: {user_string.isdigit()}")
# checks if the string only consists of numbers, returns True or False



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!