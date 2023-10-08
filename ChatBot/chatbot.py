""" ChatBot project """
# Name & birth year
bot_name = "ChatBot"
birth_year = 2023
print("Hello! My name is" + " " + str(bot_name))
print("I was created in" + " " + str(birth_year))

# User name
print("Please, remind me your name.")
your_name = str(input())
print("What a great name you have," + " " + your_name + "!")

# Questions
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is" + " " + str(age) + ";" + " " + "that's a good time to start programming!")

# Count numbers
print("Now I will prove to you that I can count to any number you want.")
number_input = int(input())
for i in range (number_input + 1):
    print(i, "!")
# Programming test
print("Let's test your programming knowledge")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
while True:
    answer_key = int(input())
    if answer_key == 2:
        print("Completed, have a nice day!")
        break
    print("Please, try again")
print("Congratulations, have a nice day!")
