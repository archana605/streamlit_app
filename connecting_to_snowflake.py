#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
from snowflake.snowpark import Session

st.set_page_config(page_title='Experimental Connection', page_icon=':wave:')
# Initialize connection.
session = st.experimental_connection('snowpark').session

temp = session.table('book_author_publisher')
temp
