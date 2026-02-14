# Create a set using the set function. A set function = set()
nums1 = set([1, 2, 3, 4, "cretins wanna hop some more."])

# Create a set using a set literal. A set literal uses curly braces {}
nums2 = {4, 5, 6, 7, "all the cretins go to heaven."}

# Print the contents of the sets:

print(nums1)
print(nums2)

# Initial list contains some duplicate values
first_names = [ 'Alba', 'Hema', 'Ron', 'Alba', 'Musa', 'Ron', 'Ron' ]

# Creating a set removes any duplicate values
names_set = set(first_names)

print(names_set)