def safe_divide(numerator, deminator):
    try:
        numerator = float(numerator)
        deminator = float(deminator)
    except ValueError:
        return 'Error: Please enter numeric values only.'
    
    try:
        result = numerator/deminator
        return f'The result of the division is {result}'
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    