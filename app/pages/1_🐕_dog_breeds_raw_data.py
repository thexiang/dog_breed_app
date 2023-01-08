import page_content
import sql_query
import streamlit as st
import utils

st.set_page_config(page_title="Dog List", page_icon="🐕")

utils.inject_css()

conn = utils.DBConnector.init_connection()

raw_dog_page = page_content.RawDogPage(conn=conn)

with st.expander("SQL Query"):
    st.code(sql_query.RAW_DOG_QUERY, language="sql")

st.write("# Dog List ")
st.table(raw_dog_page.get_transformed_data())

