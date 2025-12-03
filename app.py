import streamlit as st

# -----------------------------
# AI Knowledge Base (Rule-Based)
# -----------------------------

dish_data = {
    "maggi": {"time": "5 minutes", "ingredients": ["maggi", "water", "salt", "masala"],
              "steps": "1. Boil water.\n2. Add maggi & masala.\n3. Cook 2 minutes."},

    "pasta": {"time": "12 minutes", "ingredients": ["pasta", "salt", "water"],
              "steps": "1. Boil pasta.\n2. Add salt.\n3. Drain and add sauce if available."},

    "omelette": {"time": "7 minutes", "ingredients": ["egg", "salt", "oil"],
                 "steps": "1. Beat eggs.\n2. Heat oil.\n3. Cook both sides."},

    "tea": {"time": "6 minutes", "ingredients": ["water", "tea", "milk", "sugar"],
            "steps": "1. Boil water.\n2. Add tea.\n3. Add milk & sugar.\n4. Strain."}
}

# -------------------------------------
# AI Logic Functions
# -------------------------------------

def suggest_dish(available):
    available = [i.lower().strip() for i in available]

    for dish, info in dish_data.items():
        if all(item in available for item in info["ingredients"]):
            return f"You can cook **{dish.capitalize()}**!"
    return "Sorry! No matching dish found with available ingredients."

def get_cooking_time(dish):
    dish = dish.lower()
    return dish_data.get(dish, {}).get("time", "Sorry, I don't know this dish.")

def get_steps(dish):
    dish = dish.lower()
    return dish_data.get(dish, {}).get("steps", "I don't have steps for this dish.")


# -------------------------------------
# STREAMLIT UI
# -------------------------------------

st.set_page_config(page_title="AI Cooking Chatbot", page_icon="🍳", layout="centered")

st.title("🍳 AI Cooking Chatbot")
st.write("Ask me anything related to cooking!")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    user_input_lower = user_input.lower()

    if "time" in user_input_lower:
        dish = user_input_lower.replace("time for", "").strip()
        response = get_cooking_time(dish)

    elif "ingredients" in user_input_lower or "available" in user_input_lower:
        items = user_input_lower.replace("ingredients", "").replace("available", "").strip().split(',')
        response = suggest_dish(items)

    elif "how to make" in user_input_lower or "recipe" in user_input_lower:
        dish = user_input_lower.replace("how to make", "").replace("recipe", "").strip()
        response = get_steps(dish)

    else:
        response = "I can:\n• Suggest dishes\n• Tell cooking time\n• Give recipe steps"

    st.write("### 🤖 Bot Response:")
    st.success(response)
