# Function to calculate the total cost of a recipe based on the ingredients' prices and amounts.
# The optional ingredients' costs are not included in the total price.
def get_recipe_price(prices, optionals=None, **kwargs):
    # Initialize the total cost of the recipe.
    total = 0

    # Set the default value for the optionals list if not provided.
    if optionals is None:
        optionals = []

    # Iterate through the ingredients and their amounts passed as keyword arguments.
    for ingredient, amount in kwargs.items():
        # Check if the ingredient is not an optional item.
        if ingredient not in optionals:
            # Get the price per unit of the ingredient from the prices dictionary.
            price_per_unit = prices.get(ingredient)
            # If the price is available, add the cost of the ingredient to the total.
            if price_per_unit is not None:
                total += (prices[ingredient] * amount / 100)

    # Return the total cost of the recipe.
    return total


# Test the get_recipe_price function with required ingredients.
print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))  # Output: 44

# Test the get_recipe_price function with an optional ingredient.
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))  # Output: 54

# Test the get_recipe_price function with no ingredient prices provided.
print(get_recipe_price({}))  # Output: 0
