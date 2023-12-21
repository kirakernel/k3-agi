# Functions
string = 'I had strings but I\'m free.'
print(type(string))
print(len(string))
print(string)

print(string.lower())
print(string.upper())
print(string.capitalize())
print(string.casefold())

letters = 'abcccdeee'
for l in 'abcde':
	print(l, letters.count(l))

print('A'.islower()) # False
print('a'.islower()) # True

print(letters.find('a'))

name01 = 'Laura'
name02 = 'Amy'

print('{} is mad.'.format(name01))
print('{} and {} are mad.'.format(name01, name02))



print(string.split())
print(string.split(' ', 2))
print('real.name.text.png'.split('.'))