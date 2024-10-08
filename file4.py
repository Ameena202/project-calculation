# Function to divide two numbers
def divide_numbers(num1, num2):
    return num1 / num2

# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Dividing the two numbers
result = divide_numbers(number1, number2)

# Displaying the result
print(f"The result of dividing {number1} by {number2} is {result}.")
