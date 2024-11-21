#Create a dictionary with three key-value pairs representing a student's
#information: name, age, and grade. Print each key-value pair on a new line

student_info = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}


for key, value in student_info.items():   #each key-value pair on a new line
    print(f"{key}: {value}")


#Write a function that takes a dictionary of people's names and their ages,
#{'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of
#people who are 21 or older.
    
def find_adults(people):    # Creates a list of names of people who are 21 or older

    return [name for name, age in people.items() if age >= 21]

people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}

adults = find_adults(people)  # Calls the function and prints the result
print(adults)


#Given a dictionary representing items in a store with their prices,
#{'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes
#a list of items bought, ['apple', 'orange', 'banana', 'banana'], and
#calculates the total cost.

def calculate_total_cost(items_bought, price_list):
    total_cost = 0
    # Loop through each item bought and add the corresponding price
    for item in items_bought:
        if item in price_list:
            total_cost += price_list[item]
    return total_cost

price_list = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}

items_bought = ['apple', 'orange', 'banana', 'banana']

# Call the function and print the result
total_cost = calculate_total_cost(items_bought, price_list)
print(f"Total cost: ${total_cost:.2f}")


#Write a program that counts the occurrences of each word in a given
#sentence. Example: for the sentence "hello world hello," the output should be
#{'hello': 2, 'world': 1}.

def count_word_occurrences(sentence):
    # Split the sentence into words since they are already in lowercase)
    words = sentence.split()
    
    word_count = {}      # Create a dictionary to store word counts

    # Loop through each word and update the count in the dictionary
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

sentence = "hello world hello"

# Call the function and print the result
word_counts = count_word_occurrences(sentence)
print(word_counts)




