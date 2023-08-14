import streamlit as st
import pandas as pd

# Title and header for the page
st.title("My Mom's New Healthy Diner")
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 and Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-range Egg')
st.text('🥑🍞 Avocado Toast')

# Header for the smoothie section
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Load and process data
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let users pick the fruits for their smoothie
fruits_to_show = st.multiselect("Pick some fruits:", options=list(my_fruit_list.index), default=["Avocado", "Strawberries"])

# Filter the dataframe based on the selected fruits
filtered_fruit_list = my_fruit_list.loc[fruits_to_show]

# Display the filtered fruit data
st.dataframe(filtered_fruit_list)


# new session to display Fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

# Let's Call the Fruityvice API from Our Streamlit App!
# We need to bring in another Python package library. This one is called requests.
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())







