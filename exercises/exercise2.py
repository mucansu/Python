# Conditional Statements (max_num function):


# Task: Write a function that takes three numbers as arguments and returns the smallest among them.
# def min_num(num1, num2, num3):
#     if num1 <= num2 and num1 <= num3:
#         return num1
#     elif num2 <= num1 and num2 <= num3:
#         return num2
#     else:
#         return num3


# print(min_num(3, 5, 6))

# Task: Modify the max_num function to handle any number of arguments, not just three.


# def max_num(numbers):
#     return max(numbers)


# numbers = [
#     4,
#     5,
#     76,
#     8,
#     9,
#     6,
#     4,
#     3,
# ]

# print(max_num(numbers))


# # Dictionaries (monthConversions and numberMonthConversions):

# # Task: Add more key-value pairs to the dictionaries.

monthConverstions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
numberMonthConversions = {1: "Januay", 2: "Februay", 3: "March", 4: "April"}

# # Task: Write a function that swaps keys and values in a dictionary.


# def swap_keys_and_values(dictionary):
#     # Create a new dictionary with swapped keys and values
#     swapped_dict = {value: key for key, value in dictionary.items()}
#     return swapped_dict


# # for student, grade in students.item():
# #     grade_to_students[grade] = [student]

# monthConversions = {"Jan": "January", "Feb": "February", "Mar": "March"}

# print(swap_keys_and_values(monthConversions))

# Extra Task: Create a function that receives a dictionary of students and their grades as input. The function should return a new dictionary where the keys are the original grades and the values are lists of students who received that grade. If multiple students received the same grade, their names should appear in the list for that grade.


# def group_by_grade(students):
#     grade_to_students = {}  # Empty dictionary to store the result
#     for student, grade in students.items():
#         if (
#             grade in grade_to_students
#         ):  # If the grade is already a key in the dictionary
#             grade_to_students[grade].append(student)
#         else:
#             grade_to_students[grade] = [
#                 student
#             ]  # Create a new list for that grade with the current student
#     return grade_to_students


# print(group_by_grade({"Alice": 90, "Bob": 85, "Charlie": 90, "David": 78, "Eve": 85}))

# Task: Write a function that merges two dictionaries.


# def merge_dictionaries(first, second):
#     merged_dictionary = first.copy()  # Start with a copy of the first dictionary
#     merged_dictionary.update(second)  # Merge the second dictionary into it
#     return merged_dictionary


# print(merge_dictionaries(monthConverstions, numberMonthConversions))

# While Loops (number guessing game):

# Task: Modify the guessing game to give hints like "Guess higher" or "Guess lower".
import random

secret_number = random.randint(1, 100)
guess_limit = 7
out_of_guesses = False

guess = int(input("Guess my number: "))
guess_count = 1
while guess != secret_number and not (out_of_guesses):
    if guess_count < guess_limit:
        if guess < secret_number:
            guess = int(input("Guess higher: "))
        elif guess > secret_number:
            guess = int(input("Guess lower: "))
        guess_count += 1
    else:
        out_of_guesses = True
        print("You have reached max guess. Number is " + str(secret_number))
if guess == secret_number:
    print("Well done! Number is : " + str(secret_number))

# Task: Implement a countdown timer, where the user has only a certain amount of time to guess.
# For Loops (looping over strings, lists, and ranges):

# Task: Write a program that prints the reverse of a string, character by character.
# Task: Using a for loop, find the sum of all numbers in a list.
# Task: Print only the even numbers from a given range.
# Nested Loops (2D list traversal with number_grid):

# Task: Write a program that transposes a 2D matrix.
# Task: Create a pattern of stars using nested loops. For instance, a pyramid.
# Exception Handling (try-except block):

# Task: Handle more types of exceptions, like handling the case when a file doesn't exist.
# Task: Write a calculator program that catches exceptions when the user tries to divide by zero or enters invalid input.
# File Operations (employee_file operations):

# Task: Write a program that counts the number of lines, words, and characters in a file.
# Task: Implement a basic CSV reader that reads data from a CSV file and stores it in a list of dictionaries.
# Task: Write a program that reads a file and prints out only the lines that contain a specific keyword.
# File Modes:

# Task: Create a log file where every time a user performs an action, it gets appended to the log with a timestamp.
# Task: Write a program that backs up a given file by creating a copy with a different name.
