# Dictionary = A collection of {key: value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals)

players = {
    "Lionel Messi": 10,
    "Cristiano Ronaldo": 7
}
print(players)

caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639
}

print(caffeine_content_mg)

prices = {"apples": 1.99, "oranges": 1.49}

print(f"The price of apples is {prices['apples']}")
# This is how you add a {key}:{value} pair into an existing dictonary.
prices["bananas"] = 1.49
print(f"The price of oranges is {prices['oranges']}")
print(f"The price of bananas is {prices['bananas']}")