import streamlit
import pandas
streamlit.title('My parents new healthy dinner') 
streamlit.header('Breakfast menu')
streamlit.text(' 🥣  Omega 3 and blueberry & oat meal')
streamlit.text(' 🥗 Kale, spinach smoothie')
streamlit.text(' 🐔 Hard boiled egg')
streamlit.text('🥑🍞 Avacodo Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)
               
               
