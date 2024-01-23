# PRACTICE QUESTION:

# Create a list of your favorite fruits. Add a new fruit to the end of the list.

favorite_fruits = ["Pomogranate", "Mango", "Orange"]
favorite_fruits.append("Guava")
print(favorite_fruits)

# Remove the third fruit from the list.

fruit_to_remove = "Mango"
favorite_fruits.remove(fruit_to_remove)
print(favorite_fruits)

# Create two lists of numbers and concatenate them.

listA = [0, 1, 2]
listB = [3, 4, 5]
concatenated_list = listA + listB
print(concatenated_list)

# Multiply each element in the list by 2.

numbers = [3, 5, 7, 9]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

# Create a tuple with the days of the week.

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(days_of_week)

# Access and print the third day of the week.

third_day = days_of_week[2]
print(third_day)

# Create a list of tuples, where each tuple represents a (name, age) pair.

people_info = [('Agha', 25), ('Basit', 30), ('Irtat', 22)]
print(people_info)
