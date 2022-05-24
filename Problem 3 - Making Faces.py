# https://cs50.harvard.edu/python/2022/psets/0/faces/

from dataclasses import replace


user_input = input("Type a sentence that includes :) ir :(: ")

user_input = user_input.replace(":)", "🙂")
user_input = user_input.replace(":(", "🙁")

print(user_input)