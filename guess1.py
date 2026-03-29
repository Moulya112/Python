import random
number=random.randint(1,100)
while True:
    guess=int(input())
    if guess<number:
        print('Very low')
    elif guess>number:
        print('Very high')
    else:
        print('Your guess is correct')
        break
