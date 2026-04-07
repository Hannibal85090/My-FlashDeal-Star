import streamlit as st
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

st.set_page_config(page_title="My FlashDeal Star", layout="wide")

st.title("🌟 My FlashDeal Star")
st.write("Welcome to the demo app running on Streamlit Cloud with Python 3.14!")

# مثال بسيط: مصفوفة أرقام
arr = np.array([1, 2, 3, 4, 5])
st.write("Numpy array:", arr)

# مثال رسم بياني
fig, ax = plt.subplots()
ax.plot(arr, arr**2, label="x^2")
ax.legend()
st.pyplot(fig)

# إدخال نص من المستخدم مع إنجاز
user_input = st.text_input("Enter your name:")
if user_input:
    st.success(f"Hello, {user_input}! 🚀")
    st.balloons()
    st.info("🏅 Achievement unlocked: First interaction!")
