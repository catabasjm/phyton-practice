import random

x = random.randint(1, 10)
y = random.random()

my_list = ['rock', 'paper', 'scissor']
z = random.choice(my_list)

cards = [1,2,3,4,5,6,7,8,9,'J', 'Q', 'K']
random.shuffle(cards)

print(cards)