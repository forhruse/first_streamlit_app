import streamlit as st
import pandas as pd
import requests

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
fruits_to_show = st.multiselect("Pick some fruits:", options=list(my_fruit_list.index), default=["Avocado", "Banana"])

# Filter the dataframe based on the selected fruits
filtered_fruit_list = my_fruit_list.loc[fruits_to_show]

# Display the filtered fruit data
st.dataframe(filtered_fruit_list)

# New session to display Fruityvice API response
st.header("Fruityvice Fruit Advice!")

# Call the Fruityvice API from our Streamlit App and display the advice
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# st.text(fruityvice_response.json())
# take json verson of the data and normalize it 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output as a table
st.dataframe(fruityvice_normalized)








