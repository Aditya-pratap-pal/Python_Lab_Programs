#To show uses of the operators in Python.

# Function to perform arithmetic operations
def perform_arithmetic_operations(a, b):
    addition_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b
    division_result = a / b
    exponentiation_result = a ** b
    floor_division_result = a // b
    modulo_result = a % b

    # Displaying results
    print(f"Addition: {addition_result}")
    print(f"Subtraction: {subtraction_result}")
    print(f"Multiplication: {multiplication_result}")
    print(f"Division: {division_result}")
    print(f"Exponentiation: {exponentiation_result}")
    print(f"Floor Division: {floor_division_result}")
    print(f"Modulo: {modulo_result}")

# Function to perform relational operations
def perform_ralational_operations(a,b):
    greaterthan = a>b
    lessthan=a<b
    greaterThanAndEqual=a>=b
    lessThanAndEqual=a<=b
    equalTo=a==b
    notEqualTo=a!=b
    print("\n")

# Function to perform logical operations
def peform_logical_operations(a,b):
    andLogical=(a and b)
    orLogical=(a or b)
    notLogical=(not b)

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

perform_arithmetic_operations(num1, num2)
perform_ralational_operations(num1,num2)
peform_logical_operations(num1,num2)
