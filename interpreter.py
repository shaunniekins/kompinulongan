class MiniLanguage:
    def __init__(self):
        self.variables = {}

    def execute(self, code):
        lines = code.split('\n')
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue
            command = parts[0]
            if command == 'print':
                self.print_expression(' '.join(parts[1:]))
            elif command == 'read':
                self.read_file(parts[1])
            else:
                self.perform_operation(parts)

    def print_expression(self, expression):
        try:
            value = eval(expression, self.variables)
            print(value)
        except (NameError, SyntaxError, TypeError):
            print(expression)

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    self.execute(line.strip())
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")

    def perform_operation(self, parts):
        if len(parts) != 4:
            print("Error: Invalid syntax.")
            return

        var = parts[1]
        operator = parts[2]
        value = parts[3]

        try:
            if operator == '+':
                self.variables[var] = self.get_value(var) + self.get_value(value)
            elif operator == '-':
                self.variables[var] = self.get_value(var) - self.get_value(value)
            elif operator == '*':
                self.variables[var] = self.get_value(var) * self.get_value(value)
            elif operator == '/':
                self.variables[var] = self.get_value(var) / self.get_value(value)
            elif operator == '%':
                self.variables[var] = self.get_value(var) % self.get_value(value)
            else:
                print("Error: Invalid operator.")
        except (ValueError, ZeroDivisionError):
            print("Error: Invalid operand.")

    def get_value(self, value):
        if value in self.variables:
            return self.variables[value]
        else:
            return float(value)