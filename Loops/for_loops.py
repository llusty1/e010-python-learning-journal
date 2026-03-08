# A for loop statement loops over each element in a container one at a time, 
# assigning a variable with the next element that can then be used in the loop body.
# for variable in container:
    # Loop body: Sub-statements to execute
    # for each item in the container
# Statements to execute after the for loop is complete

for name in ["Bill", "Nicole", "John"]:
    print(f"Hi {name}")

print()
# Let's print out the key value pairs in a dictionary using the following code:
channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for x in channels:
    print(f'{x} is on channel {channels[x]}')

print()

my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)
print()

# For loops = execute a block of code a fixed number of times. 
#             You can iterate over a range, string, sequence, etc.
for x in range(1,11):
    print(x)
print()

for x in range(1, 21):
    if x == 13:
        continue # This will cause the program to skip 13
    else:
        print(x)
print()

daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]
# For loop example: Calculating shop revenue.
total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print(f'Weekly revenue: ${total:.2f}')
print(f'Daily average revenue: ${average:.2f}')
print()

# For loop example: Looping over a sequence in reverse.
names = [
    'Biffle',
    'Bowyer', 
    'Busch',
    'Gordon',
    'Patrick'
]
print('\nPrinting forward:')
for name in names:
    print(name, '|', end=' ')

print('\nPrinting in reverse:')
for name in reversed(names):
    print(name, '|', end=' ')
print()
print()

# For loop accessing both key, value pairs:
my_dict = {
    "name": "Alice",
    "age" : 30,
    "city": "New York"
}

for key, value in my_dict.items():
    print(f"{key}: {value}")
