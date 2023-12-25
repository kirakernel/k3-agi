names = ['Yor', 'Daki', 'Nene', 'Aia', 'Nerissa']

print(names)
print(names[0])
print(names[1])
print(names[-1])
print(names[len(names) - 1])


print(names[1:4])
print(names[1:])
print(names[:3])


print('Yor' in names)
print('Nerissa' in names)

print('Amy' not in names)
print('Laura' not in names)


names[0] = 'Elira'
print(names)