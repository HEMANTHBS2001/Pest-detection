


import streamlit as st
import Orange3
import pickle
import pandas as pd
import numpy as np

 
pickle_out = open("model.pkcls", mode = "rb") 
pickle.dump(model, pickle_out) 
pickle_out.close()

