import streamlit as st
st.title("⭐ My FlashDeal Star")
st.write("Talk. Pay. Done.")
token = st.text_input("Security Token", type="password")
if st.button("Connect"):
    if token == "FLASH_2026":
        st.success("Connected!")
    else:
        st.error("Invalid")
