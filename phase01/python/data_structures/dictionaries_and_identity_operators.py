girlfriend = { 'name': 'Daki', 'is_cute': True }

print(girlfriend)
print(girlfriend['name'])
print(girlfriend['is_cute'])

print('name' in girlfriend)
print('is_hot' in girlfriend)
print(girlfriend.get('age') is not None)
print(girlfriend.get('age') is None)
print(girlfriend.get('name'))