import streamlit as st
import pandas as pd
import requests
import snowflake.connector 
from urllib.error import URLError

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
  # st.header("Fruityvice Fruit Advice!")

  # fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
  # st.write('The user entered ', fruit_choice)

  # Call the Fruityvice API from our Streamlit App and display the advice
     # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
  #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # take json verson of the data and normalize it 
  #fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  # output as a table
  #st.dataframe(fruityvice_normalized)

# Second New session with Try and Except to display Fruityvice API response
# st.header("Fruityvice Fruit Advice!")
# try: 
    # fruit_choice = st.text_input('What fruit would you like information about?')
    #if not fruit_choice:
       # st.error("Please selecct a fruit to get information.")
    # else:
        # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        # ruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        # st.dataframe(fruityvice_normalized)
# except URLError as e:
       # st.error();


# Third New session with FUNCTION to display Fruityvice API response
# Create function to fetch data from Fruityvice API
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# Streamlit app
st.header("Fruityvice Fruit Advice!")

try: 
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruitvice_data(fruit_choice)
        st.dataframe(back_from_function)
except requests.exceptions.RequestException as e:
    st.error("An error occurred while fetching data from the Fruityvice API.")


# first time - Add Snowflake Connection Info to Our Streamlit Secrets File,
             # then qurrey snowflake data from streamlit
# my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
# my_cur = my_cnx.cursor()
  # my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
  # my_data_row = my_cur.fetchone()
# my_data_rows = my_cur.fetchall()
  # st.text("Hello from Snowflake:")
# st.header("The fruit load list contains:")
  # st.text(my_data_row)
# st.dataframe(my_data_rows)

# second time - Move the Fruit Load List Query and Load into a Button Action
st.header("The fruit load list contains:")
def get_fruit_load_list():
        with  my_cnx.cursor() as my_cur: 
              my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
# add a button to load data
if st.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.dataframe(my_data_rows)

# put a stop for trouble shooting - streamlit.stop
st.stop()

# allow user to add a fruit to the list
add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('Thanks for adding ', add_my_fruit)

# this will not work correclty, but just go with it for now
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit' )")



