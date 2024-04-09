import re

# DUGANG corresponds to 'ADDITION'
# KUHAAN corresponds to 'SUBTRACTION'
# PILOPILOON corresponds to 'MULTIPLICATION'
# BAHIN corresponds to 'DIVISION'
# SALIN corresponds to 'MODULUS'

OPERATIONS = r'(DUGANG|KUHAAN|PILOPILOON|BAHIN|SALIN)\((\d+), (\d+)\)'
PRINT = r'PRINTA\((.*?)\)'

def perform_arithmetic(expression):
    """Evaluate a Kompinulongan expression"""
    match = re.search(OPERATIONS, expression)
    if match:
        operator = match.group(1)
        a = int(match.group(2))
        b = int(match.group(3))
        try:
            if operator == 'DUGANG':
                return a + b
            elif operator == 'KUHAAN':
                return a - b
            elif operator == 'PILOPILOON':
                return a * b
            elif operator == 'BAHIN':
                return a / b
            elif operator == 'SALIN':
                return a % b
        except ZeroDivisionError:
            raise ValueError("Division or modulus by zero is not allowed")
    else:
        raise ValueError("Invalid expression")

def handle_print_operation(expression):
    """Print the value of a Kompinulongan print statement to the console"""
    match = re.search(PRINT, expression)
    if match:
        print(match.group(1))  # Change this to the correct group number
    else:
        raise ValueError("Invalid print statement")

def execute_program(code):
    """Interpret a Kompinulongan program"""
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('PRINTA('):
            handle_print_operation(line)
        elif re.search(OPERATIONS, line):  # Only evaluate lines that contain operations
            try:
                result = perform_arithmetic(line)
                print(result)
            except ValueError as e:  # Catch the ValueError raised by perform_arithmetic
                print(f"Error: {e}")

with open('data.txt', 'r') as file:
    program = file.read()

execute_program(program)