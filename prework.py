# # QUESTION 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
    """Display a greeting to the user"""
    print("Hello " + user_name)
hello_name('USERNAME')

# #QUESTION 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

current_number = 0
def first_odds(current_number):
    """Print a list of odd numbers 1-100"""
    while current_number <= 99:
        current_number += 1
        if current_number % 2 == 0:
            continue
        else:
            print(current_number)

first_odds(current_number)

# #QUESTION 3  Please write a Python function, max_num_in_list to return the max number of a given list. 
# # The first line of the code has been defined as below. 
 
a_list = [30,70,90,20,80]

def max_num_in_a_list(a_list):
    """Return the max number from the list of numbers"""
    for max_num_in_a_list in a_list:
        max(a_list)

print(max(a_list))
max_num_in_a_list(a_list)

# # QUESTION 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# # but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

a_year = int(input('Enter the year you would like to check. '))
def is_leap_year(a_year):
    """Identify if given year is a leap year by providing True/False response."""
    leap_year = False
    
    if a_year % 400 == 0:
        leap_year = True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        leap_year = True
    return leap_year

print(is_leap_year(a_year))

# # QUESTION 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] 
# # are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be Boolean Type.

a_list = [1,2,4,5]


def is_consecutive(a_list):
    consecutive = False
  
    x = a_list[0]
    last = a_list[-1]
    if x + len(a_list) - 1 == last:
       consecutive = True
    return consecutive 

print(is_consecutive(a_list))

