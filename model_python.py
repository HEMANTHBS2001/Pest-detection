


import streamlit as st
import Orange3
import pickle
import pandas as pd
import numpy as np



st.write('PEST DETECTION')
with open("model.pkcls","rb") as model:
    loaded_model = pickle.load(model)

