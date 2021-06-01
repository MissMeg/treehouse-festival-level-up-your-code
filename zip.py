# What does it do?
# 'combines' two or more iterables

flowers = ['sunflower', 'daisy', 'rose', 'peony']
trees = ['oak', 'birch', 'cedar', 'pear']


# zip()
plants = zip(flowers, trees)
print(plants)
print(list(plants))

# Loop
for plant in zip(flowers, trees):
    print(plant)

# Unequal length
cats = ['Big Unit', 'FuzzFace', 'Lumberjack']
dogs = ['Jethro', 'Harley', 'Pyrros', 'Jordi']
treehouse_pets = zip(cats, dogs)
print(list(treehouse_pets))


# double trouble loops
for cat, dog in zip(cats, dogs):
    print(f'A cat named {cat}')
    print(f'A dog named {dog}')