# Write a Python program that prints all even numbers between 1 and 20 using a
#for loop.
def print_even_numbers():
    for num in range(1, 21):# Loop through numbers from 1 to 20

        if num % 2 == 0:   # Check if the number is even
            print(num)

# Call the function
print_even_numbers()


#Use a while loop to ask the user to input a number until they provide a
#number greater than 10.

def prompt_for_number():
    number = int(input("Enter a number: "))
    
    while number <= 10:# checks until the number is greater than 10
        print("The number is 10 or less. Please Repeat.")
        number = int(input("Enter a number: "))

    print("You entered a number greater than 10.")

# Call the function
prompt_for_number()


# Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a
#for loop to find the sum of all odd numbers and print the result.

# List of integers
numbers = [4, 7, 2, 9, 12, 15]

# Initialize a variable to hold the sum of odd numbers
sum_of_odds = 0

# Loop through each number in the list
for num in numbers:
    # Check if the number is odd
    if num % 2 != 0:
        sum_of_odds += num  # Add the odd number to the sum

# Print the result
print("The sum of all odd numbers is:", sum_of_odds)



#Write a program that prints the multiplication table (from 1 to 10) for numbers
#from 1 to 5 using nested for loops

# Outer loop for numbers from 1 to 5
for i in range(1, 6):
    print(f"Multiplication Table for {i}:")
    
    # Inner loop for multiplying i by numbers from 1 to 10
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    
    print()  # Print a blank line after each table for readability




