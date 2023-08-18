from pywebio.input import input as pw_input
from pywebio.input import NUMBER, PASSWORD, TEXT, DATETIME, COLOR
from pywebio.output import put_success, put_warning, put_code, popup, put_markdown, toast

user_pet = pw_input('Enter your favorite pet', type=TEXT, required=True)

nickname_of_user_pet = pw_input('Enter nickname of your pet', type=TEXT, required=True)

cat_emoji = '\U0001F408'
dog_emoji = '\U0001F415'
hamster_emoji = '\U0001F439'
fish_emoji = '\U0001F41F'
turtle_emoji = '\U0001F422'

can_pet_swim = pw_input('Can your pet swim?', type=TEXT, required=True)

if user_pet == 'fish':
    put_success('We have to buy aqurium')
if user_pet == 'turtle':
    put_success('We have to buy aqurium')

if user_pet == 'dog':
    put_success(f'I am very scarred barking of dogs and dog by nickname {nickname_of_user_pet}')
elif user_pet == 'cat':
    put_success('Cats catching mice')
else:
    put_success("I don`t know this pet")
if user_pet == 'hamster':
    put_success('Hamsters are small')
elif user_pet == 'fish':
    put_success('Don`t fry fish')
if user_pet == 'turtle':
    put_success('Turtles have strong carapace')
