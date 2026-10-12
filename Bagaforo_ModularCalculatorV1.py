# Define Operations

def add(value1, value2):
    return value1 + value2
    
def subtract(value1, value2):
    return value1 - value2
    
def multiply(value1, value2):
    return value1 * value2
    
def divide(value1, value2):
    if value2 == 0:
        return "Error: Cannot divide by zero"
    return value1 / value2
    
# Input for two numbers

value1 = float(input("Enter first value: "))
value2 = float(input("Enter second value: "))

# Choosing of Operations

operation = input("Choose an operation (+, -, *, /): ")

# Call the correct function based off the operation

if operation == '+':
    result = add(value1, value2)
elif operation == '-':
    result = subtract(value1, value2)
elif operation == '*':
    result = multiply(value1, value2)
elif operation == '/':
    result = divide(value1, value2)
else:
    result = "Invalid Operation"
    
# Final result

print(f"The final result is: {result}")