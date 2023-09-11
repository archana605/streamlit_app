#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title='Experimental Connection', page_icon=':wave:')
# Initialize connection.
session = st.experimental_connection('snowpark').session

temp = session.table('department')
temp
