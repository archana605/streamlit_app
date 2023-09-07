import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pydeck as pdk
import scipy
import altair as alt
import matplotlib.pyplot as plt
import time
from streamlit_extras.switch_page_button import switch_page
from snowflake.snowpark.context import get_active_session
