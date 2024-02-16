from random import randint as generate_number
import utils.calculator as cl
from utils.person import Person
from termcolor import cprint
import emoji
from decouple import config

# alias

print(generate_number(2, 10))
print(cl.subtraction(9, 5))

my_friend = Person('Jim', 30)
print(my_friend)

cprint("Hello, World!", "green", "on_red")
print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
commented = config('COMMENTED', default=3, cast=int)
print(commented * 2)
# My comment