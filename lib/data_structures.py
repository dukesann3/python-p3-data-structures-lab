spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_names = []
    for food in spicy_foods:
        food_name = food.get("name")
        spicy_foods_names.append(food_name)
    
    return spicy_foods_names

def get_spiciest_foods(spicy_foods):
    foods_that_are_spicy = []
    for food in spicy_foods:
        spicy_level = food.get("heat_level")
        if spicy_level > 5:
            foods_that_are_spicy.append(food)

    return foods_that_are_spicy


def heat_level_converter(spicy_foods_level):
    chili_string = "🌶"
    converted_spicy_level = chili_string * spicy_foods_level
    return converted_spicy_level


def print_spicy_foods(spicy_foods):


    for food in spicy_foods:
        food_name = food.get("name")
        food_type = food.get("cuisine")
        food_spicy_level = food.get("heat_level")
        converted_food_spicy_level = heat_level_converter(food_spicy_level)

        print(f"{food_name} ({food_type}) | Heat Level: {converted_food_spicy_level}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    for food in spicy_foods:
        cuisine_type = food.get("cuisine")
        if cuisine_type == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        food_name = food.get("name")
        food_cuisine = food.get("cuisine")
        food_spicy_level = food.get("heat_level")
        converted_spicy_level = heat_level_converter(food_spicy_level)

        print(f"{food_name} ({food_cuisine}) | Heat Level: {converted_spicy_level}")


def get_average_heat_level(spicy_foods):
    sum_of_spicy_levels = 0
    length_of_spicy_foods_list = len(spicy_foods)

    for food in spicy_foods:
        food_spicy_level = food.get("heat_level")
        sum_of_spicy_levels += food_spicy_level
    
    average_spicy_level = sum_of_spicy_levels / length_of_spicy_foods_list
    return average_spicy_level


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
