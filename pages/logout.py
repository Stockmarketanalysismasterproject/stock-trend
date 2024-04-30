import streamlit as st
from sqlalchemy import text


from utils import *

import sys
import os

# Add the parent directory of Folder1 to the Python path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)


from stock_trend import index
from stock_trend import login


st.success("Loged Out Successfully")

# Initialize SQL connection.
# Uses @st.cache_resource to run only once
@st.cache_resource
def init_conn():
    db_url = st.secrets["DATABASE_URL"]
    return st.connection("postgresql", type="sql", url=db_url)
conn = init_conn()

# Get the email of the user
email = login.email_fn()

# Update the user auth_status
with conn.session as session:
    query = text(f"UPDATE users SET auth_status = 'TRUE' WHERE email = '{email}';")
    session.execute(query)
    session.commit()

index.app()