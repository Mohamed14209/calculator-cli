while True:
    try:
        The_first__number = int(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /, %, **): ")
        second__number = int(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if operator not in ['+', '-', '*', '/', '%', '**']:
        print("Please enter one of these operators: +  -  *  /  %  **")
        continue

    if operator == '+':
        result = The_first__number + second__number

    elif operator == '-':
        result = The_first__number - second__number

    elif operator == '*':
        result = The_first__number * second__number

    elif operator == '/':
        if second__number == 0:
            print("Cannot divide by zero!")
            continue
        result = The_first__number / second__number

    elif operator == '%':
        result = The_first__number % second__number

    elif operator == '**':
        result = The_first__number ** second__number

    print("The result is:", result)

    Question = input("Do you want to perform another calculation? (y/n): ")

    if Question.lower() == 'n':
        print("Goodbye!")
        break