import streamlit
import pandas
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
streamlit.title('My parents new healthy dinner') 
streamlit.header('Breakfast menu')
streamlit.text(' 🥣  Omega 3 and blueberry & oat meal')
streamlit.text(' 🥗 Kale, spinach smoothie')
streamlit.text(' 🐔 Hard boiled egg')
streamlit.text('🥑🍞 Avacodo Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)
               
               
