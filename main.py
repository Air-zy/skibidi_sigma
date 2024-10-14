def get_input(prompt, num=True):
    while True:
        value = input(prompt)
        if (num and value.isnumeric()) or (not num and value in '*+-/'):
            return float(value) if num else value
        print('invalid input.')

total = 0

# infinite loop to keep taking inputs and performing operations until the user decides to quit.
while True:
    first_number = total if total else get_input('enter first number: ')
    second_number = get_input('enter second number: ')
    operation = get_input('choose operation (*, /, +, -): ', num=False)

    # If 'total' is 0 (i.e., no existing calculation), prompt the user for the first number.
    # result of the operation is stored back into 'total', allowing subsequent operations to build upon it.
    total = (first_number * second_number if operation == '*' else 
             first_number / second_number if operation == '/' and second_number != 0 else 
             'error: Cannot divide by zero' if operation == '/' else 
             first_number + second_number if operation == '+' else 
             first_number - second_number)

    print(total)
    
    # there was a division by zero or the user dont want to continue, break out of the loop.
    if total == 'error: Cannot divide by zero' or input('Another operation? (yes/no): ').lower() != 'yes':
        break

    if input('use existing calculation or start a new one? (Exist or New): ').lower() == 'new':
        total = 0 # reset
