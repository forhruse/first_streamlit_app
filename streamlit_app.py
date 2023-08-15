import streamlit as st
import pandas as pd
import requests
import snowflake.connector 

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

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

# Call the Fruityvice API from our Streamlit App and display the advice
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# take json verson of the data and normalize it 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output as a table
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
# st.text("Hello from Snowflake:")
st.header("The fruit load list contains:")
# st.text(my_data_row)
st.dataframe(my_data_rows)

# allow user to add a fruit to the list
add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('Thanks for adding ', add_my_fruit)



