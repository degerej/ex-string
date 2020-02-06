# Joe Degere
# String Lab
# 2/6/2020

my_name = "Joe, Jeff, Ben, Nick"

print("The length of this string is:", len(my_name))
print("The first letter in the string is:", my_name[0][:1])
print("The last name in my string is:", my_name[15:])
print(my_name.__str__().upper())
print(my_name.__str__().title())

# The true or false then split methods
print("Is this string alphabetic?")
print(my_name.__str__().isalpha())
print(my_name.__str__().split())

# My method of choice is lowercase

print("My string will now be lowercase:", my_name.__str__().casefold())
