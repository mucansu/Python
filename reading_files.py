"""
- "r" means read
- "w" means write, you can change the content
- "a" means append, you can only add new info
- "r+" means read and write
"""
employee_file = open("employees.txt", "r")
print(employee_file.readable())  # this is gonna return if the file is readable or not
print(employee_file.read())  # read all the content
print(employee_file.readline())  # read the first line
print(employee_file.readline())  # read the next line
print(employee_file.readlines())  # read the lines in a list
print(employee_file.readlines([3]))  # read the fourth line in the list

for employee in employee_file.readlines():
    print(employee)

# when we are done with the file, it is good to close it
employee_file.close()
