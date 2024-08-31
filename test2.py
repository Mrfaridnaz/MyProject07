# Get input from the user as a comma-separated string of numbers
numbers = input("Enter a list of numbers separated by commas: ")

# Convert the string into a list of integers
numbers_list = [int(num.strip()) for num in numbers.split(",")]

# Calculate the sum of the numbers in the list
total_sum = sum(numbers_list)

# Print the result
print(f"The sum of the numbers in the list is: {total_sum}")
