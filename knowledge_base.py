# Knowledge base for common Indian dishes
knowledge_base = {
    "idli": {
        "time": "15-20 minutes",
        "recipe": "Steam the batter in idli molds for 15-20 minutes."
    },
    "dosa": {
        "time": "10-15 minutes",
        "recipe": "Pour the batter on a hot tawa, cook until golden, then flip and cook."
    },
    "poha": {
        "time": "10 minutes",
        "recipe": "Soak poha, sauté with onions, green chilies, turmeric, and peanuts."
    },
    "upma": {
        "time": "10-12 minutes",
        "recipe": "Roast semolina, then cook with water, vegetables, and spices."
    },
    "paneer butter masala": {
        "time": "25-30 minutes",
        "recipe": "Cook paneer cubes in tomato gravy with butter, cream, and spices."
    },
    "chole": {
        "time": "40-45 minutes",
        "recipe": "Cook chickpeas with onion, tomato, ginger-garlic paste, and spices."
    },
    "dal tadka": {
        "time": "20-25 minutes",
        "recipe": "Cook lentils and temper with ghee, garlic, cumin, and chili."
    },
    "biryani": {
        "time": "50-60 minutes",
        "recipe": "Layer marinated meat/vegetables with rice and cook with spices."
    },
    "aloo gobi": {
        "time": "20-25 minutes",
        "recipe": "Cook potatoes and cauliflower with tomato, onion, and spices."
    },
    "samosa": {
        "time": "30-35 minutes",
        "recipe": "Prepare dough, fill with spiced potato mix, and deep fry."
    },
    "pav bhaji": {
        "time": "25-30 minutes",
        "recipe": "Cook mashed vegetables with butter and spices, serve with pav."
    },
    "idiyappam": {
        "time": "15 minutes",
        "recipe": "Steam rice flour noodles and serve with curry or coconut milk."
    },
    "rajma": {
        "time": "35-40 minutes",
        "recipe": "Cook kidney beans with onion, tomato, and spices."
    },
    "masala dosa": {
        "time": "15-20 minutes",
        "recipe": "Prepare dosa batter, cook on tawa, and fill with potato masala."
    },
    "vada": {
        "time": "15-20 minutes",
        "recipe": "Shape lentil batter into rounds and deep fry until golden."
    },
    "gulab jamun": {
        "time": "30 minutes",
        "recipe": "Fry dough balls and soak in sugar syrup."
    },
    "rasgulla": {
        "time": "25-30 minutes",
        "recipe": "Boil cottage cheese balls in sugar syrup until soft."
    }
}

# Example function to fetch info
def get_dish_info(dish_name, info_type="time"):
    dish_name = dish_name.lower()
    if dish_name in knowledge_base:
        return knowledge_base[dish_name][info_type]
    else:
        return "Sorry, I don't know about that dish."

# Example usage
print(get_dish_info("Biryani", "time"))
print(get_dish_info("Chole", "recipe"))
