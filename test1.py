# Function to check if a number is odd
def is_odd(number):
    return number % 2 != 0

# Get input from the user
num1 = int(input("Enter the first odd number: "))
num2 = int(input("Enter the second odd number: "))

# Check if both numbers are odd
if is_odd(num1) and is_odd(num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
else:
    print("Both numbers must be odd. Please try again.")
