# Simple while loop:
value = 1
while value < 10: # If you want to include the number 10 when printing the value
                  # you have to include the = sign. So it would look like 
                  # while value <= 10
    print(value)
    if value == 5: # Here we will nest an if statement into the body of the while loop. 
        break
    value += 1

# Simple for loop
# names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)
    
# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# Range function in a for loop
for x in range(0,101,5):
    print(x)
else:
    print("Glad that's over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for action in actions:
    for name in names:
        print(name + " " + action + ".")