
import Orange
import pandas as pd

try:
    mc = pd.read_pickle("model.pkcls")
except FileNotFoundError:
    st.error("File not found. Please check the file path.")
except Exception as e:
    st.error(f"Error loading pickle file: {e}")

