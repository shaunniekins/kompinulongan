import re

# DUGANG corresponds to 'ADDITION'
# KUHAAN corresponds to 'SUBTRACTION'
# PILOPILOON corresponds to 'MULTIPLICATION'
# BAHIN corresponds to 'DIVISION'
# SALIN corresponds to 'MODULUS'

OPERATIONS = r'(DUGANG|KUHAAN|PILOPILOON|BAHIN|SALIN)\(([\d, ]+)\)'
PRINT = r'PRINTA\((.*?)\)'

def perform_arithmetic(expression):
    match = re.search(OPERATIONS, expression)
    if match:
        operator = match.group(1)
        numbers = list(map(int, match.group(2).split(',')))
        try:
            if operator == 'DUGANG':
                return sum(numbers)
            elif operator == 'KUHAAN':
                return numbers[0] - sum(numbers[1:])
            elif operator == 'PILOPILOON':
                result = 1
                for number in numbers:
                    result *= number
                return result
            elif operator == 'BAHIN':
                result = numbers[0]
                for number in numbers[1:]:
                    result /= number
                return result
            elif operator == 'SALIN':
                result = numbers[0]
                for number in numbers[1:]:
                    result %= number
                return result
        except ZeroDivisionError:
            raise ValueError("Division or modulus by zero is not allowed")
    else:
        raise ValueError("Invalid expression")

def handle_print_operation(expression):
    match = re.search(PRINT, expression)
    if match:
        print(match.group(1)) 
    else:
        raise ValueError("Invalid print statement")

def execute_program(code):
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('PRINTA('):
            handle_print_operation(line)
        elif re.search(OPERATIONS, line):
            try:
                result = perform_arithmetic(line)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

with open('data.txt', 'r') as file:
    program = file.read()

execute_program(program)