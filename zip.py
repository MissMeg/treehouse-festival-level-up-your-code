# What does it do?
# 'combines' two or more iterables

flowers = ['sunflower', 'daisy', 'rose', 'peony']
trees = ['oak', 'birch', 'cedar', 'pear']


# zip()
plants = zip(flowers, trees)
print(plants)
print(list(plants))

# Unequal length
cats = ['Big Unit', 'FuzzFace', 'Lumberjack']
dogs = ['Jethro', 'Harley', 'Pyrros', 'Jordi']
treehouse_pets = zip(cats, dogs)


# double trouble loops
for dog, cat in treehouse_pets:
    print(f'A cat named {cat}')
    print(f'A dog named {dog}')