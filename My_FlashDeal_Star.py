import streamlit as st
import time

# --- العنوان مع الشعار والنجمة ---
current_time = time.strftime("%d/%m/%Y - %H:%M:%S")

# العنوان الرئيسي
st.markdown(
    "<h1 style='text-align:center;color:#000000;text-shadow:0 0 10px #444444;'>🌟 My FlashDeal Star 🌟</h1>",
    unsafe_allow_html=True
)

# الشعار بالإنجليزية
st.markdown(
    "<p style='text-align:center;color:gold;font-size:22px;'>TALK , PAY , DONE .</p>",
    unsafe_allow_html=True
)

# الشعار بالعربية
st.markdown(
    "<p style='text-align:center;color:gold;font-size:22px;'>تكلم ، ادفع ، تم .</p>",
    unsafe_allow_html=True
)

# النجمة الكبيرة
st.markdown('<div style="text-align:center;font-size:60px;color:gold;">★</div>', unsafe_allow_html=True)

# التوقيت أسفل النجمة
st.markdown(
    f"<p style='text-align:center;color:#4facfe;'>🕒 Current Time: {current_time}</p>",
    unsafe_allow_html=True
)
