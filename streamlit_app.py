import streamlit as st

st.title("My Mom's New Healthy Diner")
st.header(' Breakfast Favorites')
st.text('🥣 Omega 3 and Blueberry Oatmeal')
st.text('🥗 Kale, Spinich & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-range Egge')
st.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
selected_fruits = st.multiselect("Pick some fruits:", options=list(my_fruit_list.index), default=["Avocado", "Strawberries"])

# Filter the dataframe based on the selected fruits
filtered_fruit_list = my_fruit_list.loc[selected_fruits]

# Display the table on the page.
st.dataframe(my_fruit_list)







