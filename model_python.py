import streamlit as st
import pickle
import cv2
import numpy as np
model = pickle.load(open('model.pkcls', 'rb'))
user_input = st.text_input("ENTER FILE PATH")



image = cv2.imread(user_input)

# # Convert BGR image to RGB (if needed)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Convert the image to a NumPy array
# numpy_array = np.array(image_rgb)
prediction = model.predict(image)

