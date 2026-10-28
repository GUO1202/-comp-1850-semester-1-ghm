
def countdown(number): 

    print(number)#print the current number
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 
    if number > 0:

        countdown(number - 1)

number = int(input("Enter a positive integer: "))
countdown(number)