import streamlit as st

# Pymongo import for MongoDB connection
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.set_page_config(
    page_title = "ChatBot App"
)

st.title("Home Page")

st.sidebar.success("Select a page")

st.text("Hello World")

# streamlit_app.py
#import mysql.connector as sql_conn

st.header("SQL Table")
st.text("Doc Source: https://docs.streamlit.io/knowledge-base/tutorials/databases/mysql")
# Initialize connection.
sqlconn = st.connection('mysql', type='sql')

# Perform query.
df = sqlconn.query('SELECT * from mytable;', ttl=600)

# print query table as dataframe
st.dataframe(df)


st.header("MongoDB Table")
st.text("Doc Source: https://docs.streamlit.io/knowledge-base/tutorials/databases/mongodb")

# OpenID Connect (OIDC) Docs: https://www.microsoft.com/en-us/security/business/security-101/what-is-openid-connect-oidc#:~:text=OpenID%20Connect%20(OIDC)%20is%20an,who%20they%20say%20they%20are.
url = ""

# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Initialized database and collection variables for testing
db = client.pets
coll = db.petdata

# count variable to limit inserts
count = 1

@st.cache_data(ttl=600)
def insert_data():
    docs = [{"name" : "Mary", "pet": "dog"}, 
        {"name" : "John", "pet": "cat"}, 
        {"name" : "Robert", "pet": "bird"}]

    coll.insert_many(docs)

def get_data():
    items = coll.find()
    items = list(items)  # make hashable for st.cache_data
    return items

if count <= 0:
    insert_data() # - uncomment when running initially or set count to 0

items = get_data()

# Print database items
st.dataframe(items)

client.close()

