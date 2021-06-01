# What does it do?
# enumerate() adds a counter

flowers = ['sunflower', 'daisy', 'rose', 'peony']

# for loop
for flower in flowers:
    print(flower)

# counter loop
count = 0
for flower in flowers:
    print(count, flower)
    count += 1

# enter enumerate()
for count, flower in enumerate(flowers):
    print(count, flower)

# can't access
enumerate(flowers)[0]

# choose starting point
for count, flower in enumerate(flowers, start=1):
    print(count, flower)