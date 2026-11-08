# Week 1.3, Session 2: Write User Information to a File

name = input("Enter your name: ")
age = input("Enter your age: ")
colour = input("Enter your favourite colour: ")
with open('user_info.txt', 'w') as f:
    f.write(name + '\n')
    f.write(age + '\n')
    f.write(colour + '\n')
