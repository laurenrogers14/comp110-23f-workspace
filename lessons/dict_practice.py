"""Practice with dictionaries."""

# Constructung a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5, "mint": 10}
print("Made my dictionary")
print(ice_cream)

# Adding a key, value pair to a dictionary
ice_cream: ["mint"] = 3
print("After adding mint:")
print(ice_cream)

# Removing a key, value pair from a dictionary
ice_cream.pop("mint")
print("After removing mint")
print(ice_cream)

# Adjusting a value
ice_cream["vanilla"] = 10
print("After adjusting amount of vanilla")
print(ice_cream)

# Print out the length of ice_cream
print(f"the number of key value pairs: {(len(ice_cream))}")

# Check if key is in dictionary
if "mint" in ice_cream:
    print(f"Number of orders {ice_cream['mint']}")
else:
    print("No orders of mint.")

# For loops with dictionaries
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")
