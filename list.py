#Create a list of 5 fruits and print each fruit on a new line using a for loop


fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]

for fruit in fruits:      # prints each fruit in the list using a for loop

    print(fruit)


#Write a function that takes a list of numbers and returns a new list with
#each number squared. Example: [1, 2, 3] should become [1, 4, 9].
    
def square_numbers(numbers):

    squared_numbers = [num ** 2 for num in numbers]     #  squares each number in the list using a list comprehension

    return squared_numbers

numbers = [1, 2, 3]
print(square_numbers(numbers))  


#Write a Python program that takes two lists, list1 = [1, 2, 3] and
#list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2,5, 3, 6].

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = []    # Initialize an empty list tat takes in combined result


#using a for loop combine the lists
for i in range(len(list1)):
    combined.append(list1[i])
    combined.append(list2[i])

print("Combined list:", combined)  


#Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find
#and print the two largest numbers in the list without using the max() function.

numbers = [3, 1, 4, 1, 5, 9, 2]

# Initialize two variables that takes in two largest numbers
largest = float('-inf')  
second_largest = float('-inf')

# Loop through each number in the list
for num in numbers:
    if num > largest:
        # Update second largest before updating largest
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest: #used to ensure that the second largest number is different from the largest number. 
    
        second_largest = num

print("The two largest numbers are:", largest, "and", second_largest)





