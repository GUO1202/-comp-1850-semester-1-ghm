
def func_1(lst_value): #define a function called func_1 that takes a list of values as input
    ''' 
    write your docstring to explain the function 
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
    sum = sum + value 
    return sum/num_of_value 