# This program is a simple program that implements raw_input
# and string formatting. The user gets asked a series of questions
# and then a formatted sentence is generated based on their response.
#
# There is also a try-except-else to catch whether the user types in
# a non-number for the number of pets that they have.

first_name = raw_input("Tell us your first name: ")
last_name = raw_input("Tell us your last name: ")
favorite_color = raw_input("Tell us your favorite color: ")
number_of_pets = ""
while True:
    try:
      number_of_pets = int(raw_input("Tell us how many pets you have: "))
      if number_of_pets < 0:
        print "That's a negative number!"
        continue
    except (ValueError):
      print "That's not a number, dawg!, try again."
    else: # no ValueError problems
      break

# format the print statement section
message = "Great! So your name is %s %s, \nyour favorite color is %s and you have %d pets. \
\nNice to meet you!" % (first_name, last_name, favorite_color, number_of_pets)

print message
