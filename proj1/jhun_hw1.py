# @author jhunbaclaan
# d.o.c (date of creation): 01/21/2026
# objective -- create a program that takes user input and parses for a sentence with >= 25 chars
# from these chars, return the amount of letters & numbers
# symbols like !@#$%^&*() do not count

print("welcome to the program!")
print("this program will take your input and return the amount of letters and numbers in that input")
print("input must be 25 characters or longer. let's get started!")
# create a while loop until the user prompts quit
while True:
    user_input = input("enter text (otherwise, type quit to exit): ")
    # pre-condition: check if input = quit
    if user_input == 'quit':
        break
    # else, parse input into a char array
    input_asArray = list(user_input)
    if (len(input_asArray) < 25):
        print("input length is less than 25 characters!")
    else:
        letters = numbers = 0 # counters for letters & numbers, both are ints
        for char in input_asArray:
            if char.isalpha():
                letters += 1
            elif char.isnumeric():
                numbers += 1
            else:
                # if not letter or number, skip
                continue
        print("=-=-=-=- string analysis complete -=-=-=-=")
        print("letters: ", letters)
        print("numbers: ", numbers)
print("thank you for using the program!")