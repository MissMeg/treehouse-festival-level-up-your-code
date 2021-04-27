# What does it do?
# map() applies a function to an iterable

flowers = ['sunflower', 'daisy', 'rose', 'peony']

# regular loop
plural = []
for flower in flowers:
    if flower[-1] == 'y':
        plural.append(flower + 'ies')
    else:
        plural.append(flower + 's')
print(plural)


# map()
def pluralize(word):
    if word[-1] == 'y':
        return word + 'ies'
    else:
        return word + 's'


plural = map(pluralize, flowers)
print(list(plural))

# other built-in functions
length = list(map(len, flowers))

# lambda functions
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda num: num * 2, nums))