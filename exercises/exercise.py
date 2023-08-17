# Scenario 1 - The Student Grading System: Create a Python script that grades a student based on their score. The score should be a number between 0 and 100. If the score is above 90, print "A". If it's between 80 and 90, print "B". If it's between 70 and 80, print "C". If it's between 60 and 70, print "D". Otherwise, print "F".

score = 30

if score >= 90:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")

# Scenario 2 - The Movie Ticket Pricing: A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a Python script that asks for the age and determines the cost of the movie ticket.
age = input("How old are you?\n")
ticket = 0

if 3 < int(age) < 12:
    ticket = 10
elif int(age) > 12:
    ticket = 15

print("Your ticker price is : " + str(ticket))

# Scenario 3 - The Driving Eligibility Check: In some countries, you must be at least 18 years old and have a valid driving license to drive a car. Write a Python script that asks for the age and whether the person has a driving license (yes/no). Then, using if-elif-else statements, determine whether the person is eligible to drive or not.

hasDriverLicence = False

age2 = int(input("How old are you ?\n"))


if age2 >= 18:
    licence_input = input("Do you have a driver's licence? (yes/no)\n")
    if licence_input.lower() == "yes":
        hasDriverLicence = True
        print("Yeey! you can drive!")
    else:
        print("You are old enough but need a driver's licence")
else:
    ageDiff = 18 - age2
    print("Oh sorry, you need to wait for another " + str(ageDiff) + " years")

# Scenario 4 - The Restaurant Order: A restaurant has different meal options based on the time of day. In the morning they serve breakfast, in the afternoon they serve lunch, and in the evening they serve dinner. Write a Python script that asks for the current time (in 24-hour format) and prints out what meal is being served right now.

current_time = int(input("What time is it?\n"))

if 7 < current_time < 11:
    print("Breakfast time")
elif 11 < current_time < 15:
    print("Lunch time")
elif 16 < current_time < 19:
    print("Dinner time")
else:
    print("Not a meal time")


# Scenario 5 - The Leap Year Checker: A year is a leap year if it is divisible by 4, but not by 100 unless it is also divisible by 400. Write a Python script that asks for a year and checks if it's a leap year or not.

year = int(input("Give me a year"))

if year % 400 == 0:
    print("It is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("It is a leap year")
else:
    print("It is not a leap year")
