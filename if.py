number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    print('Congratulations, you guessed it.')
    print('(But you do not win any prizes!)')
elif guess < number:
# Another block
    print('No, it is a little higher than that')
# You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
# you must have guessed > number to reach here
print('Done')