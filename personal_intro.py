name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What is your favorite hobby? ")
city = input("Which city do you live in? ")
foods_input = input("What are your favorite foods? (separate by commas) ")

# Process the foods into a list
favorite_foods = [food.strip() for food in foods_input.split(',')]

print(f"🎉 Welcome {name}! 🎉")
print(f"You are {age} years old and love {hobby}.")
print(f"You live in {city} and enjoy eating: {', '.join(favorite_foods)}.")