# In Python iterating over a dictionary means looping
# through its elements (key,values) one by one using 
# a for loop or similar interation mechanism

my_dict = {"a": 1, "b": 2, "c": 3}
# 1. Iterate over keys in my_dict (Default behavior)
for key in my_dict:
    print(key)

# 2. Iterate over values in my_dict using .values()
for value in my_dict.values():
    print(value)

# 3. Iterate over both keys and values (most common)
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Summary of Methods
# for key in my_dict: It will yield Keys
# for key in my_dict.keys(): Yields Keys
# for value in my_dict.values(): Yields Values
# for key, value in my_dict.items(): Yields Tuples (key, value pairs)