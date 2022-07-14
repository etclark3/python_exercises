# help with 2b, 2c
# Q1: Conditional Basics
# Q1a: prompt the user for a day of the week, print out whether the day is Monday or not
from re import I


day_of_week = 'Monday'

if day_of_week == 'Monday':
    print('Today is ' + day_of_week)
else:
    print('It\'s not Monday')

# Q1b: prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend_day = ['Saturday', 'Sunday']
day = 'Wednesday'

if day in weekend_day:
    print('Today is weekend day')
elif day in weekday:
    print('Today is a weekday')

# Q1c: create variables and make up values for
# the number of hours worked in one week
# # the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hours_worked = 45
hourly_rate = 35
regular_paycheck = hourly_rate*hours_worked
overtime_paycheck = (hourly_rate*40) + ((hours_worked - 40) * (hourly_rate*1.5))

if hours_worked <= 40:
    print(f'This week I will make ${regular_paycheck}')
elif hours_worked > 40:
    print(f'This week I will make ${overtime_paycheck} with overtime')

# Q2: Loop Basics
    # 2a: While
        # Create an integer variable i with a value of 5.
i = 5

        # Create a while loop that runs so long as i is less than or equal to 15
while i <= 15:
    print(i)
    i += 1

        # Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
for i in range(0, 101, 2):
    print(i)
    print('line')

i=100
while i => -10:
    print(i)
    i -= -5

        # Alter your loop to count backwards by 5's from 100 to -10.
for i in range(100, -16, -5):
    print(i)

        # Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i=2

while i < 1000000:
    print(i)
    i = i**2

        # Write a loop that uses print to create the output shown below.
for i in reversed(range(5,105, 5)):
    x = i
    print(x)

for i in reversed(range(1,21)):
    x = i * 5
    print(x)

for i in range(100,0, -5):
    x = i
    print(x)

for i in range(100)

i = 100
while i >= 5:
    print(i)
    i -= 5

    # 2b: For Loops

        # Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
num = int(input("Enter your number"))
for x in range(1,11):
    print(num, 'x', x, '=', num*x)
        # Create a for loop that uses print to create the output shown below.
for x in range(1,10):
    print(x * str(x))

    # 2c: break and continue

        # Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
skip_num = int(input())

for i in range(1,50):
    if i % 2:
        print(f'Odd: {i}')
    f = skip_num
    elif f == i:
        print('not today')
    else:
        print(i)

for i in range(0,50):
    if i == 27:
        print('no no no, not today')
    elif i % 2:
        print(f'Odd Number: {i}')

        # (Hint: use the isdigit method on strings to determine this). 
        # Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
        # The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
while True:
    number = int(input('Enter a positive number''))
    if number.isdigit() == True:
        print('This is a numer')
        if number > 0:
            print('This is Positive')
            break

for x in range((number) + 1)):
    print(x)
        # Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# 3: Fizzbuzz
    # One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
    # Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
        # Write a program that prints the numbers from 1 to 100.
        # For multiples of three print "Fizz" instead of the number
        # For the multiples of five print "Buzz".
        # For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(0,101,3):
    print(i)

for i in range(1,101):
    q = i in range(0,101,3)
    else:
        print(i)

y = i in range(0,101,5)
g = i in range(0,101,3) and range(0,101,5)
    if q:
        print('Fizz')
    if g:
        print('FizzBuzz')
    if y:
        print('Buzz')
    else:
        print(i)

for i in range(1,101):
    q = i in range(0,101,3)
    y = i in range(0,101,5)
    g = i in range(0,101,15)
    if g:
        print('FizzBuzz')
    elif q:
        print('Fizz')
    elif y:
        print('Buzz')
    else:
        print(i)

for i in range(1,101):
    if x % 3 == 0:
        print('Fizz')
        continue
    print(x)

# 4: Display a table of powers.
    # Prompt the user to enter an integer.
    # Display a table of squares and cubes from 1 to the value entered.
    # Ask if the user wants to continue.
    # Assume that the user will enter valid data.
    # Only continue if the user agrees to.
integer = x

    print('Table:')