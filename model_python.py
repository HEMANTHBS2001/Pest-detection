# pip install opencv-python

import streamlit as st
import Orange
import pickle
import pandas as pd
import numpy as np
from pandas.api.types import SparseDtype


st.write('PEST DETECTION')
with open("model.pkcls","rb") as model:
    loaded_model = pickle.load(model)

