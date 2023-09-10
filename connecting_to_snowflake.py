import streamlit as st
import pandas as pd
import numpy as np


import os

# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])


# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
