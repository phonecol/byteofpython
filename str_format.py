age = 20
name = 'Swaroop'

print('{name} was {age} years old when he wrote this book'.format(name=name ,age=age))
print('Why is {name} playing with that python'.format(name=name))

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^20}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

print('a',end = ' ')

print('b',end = '\n')

print(R'This is the first sentence. This is the second sentence.')
print(r'weeew')