


import streamlit as st
# import Orange3
import pickle
import pandas as pd
import numpy as np

 
pickle_in = open('model.pkcls', 'rb') 
classifier = pickle.load(pickle_in)

