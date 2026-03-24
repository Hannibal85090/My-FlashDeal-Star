import streamlit as st
import time

# --- 1. إعداد الصفحة الأساسي ---
st.set_page_config(page_title="FlashDeal Star Celebration", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history=[]

def add_to_memory(action):
    timestamp=time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. التنسيق الجمالي (أوراق الصنوبر الزرقاء والاحتفالية) ---
st.markdown("""
<style>
/* خلفية أوراق الصنوبر الزرقاء */
.stApp {
    background: linear-gradient(135deg, #001a33 0%, #003366 100%);
    background-image: url("https://www.transparenttextures.com/patterns/pinetree.png");
    background-blend-mode: overlay;
}
.main-title {text-align:center; color:#000000; text-shadow:0 0 10px #ffffff; font-size:3rem; font-weight:bold; margin-bottom:0px;}
.motto-black {text-align:center; color:#000000; font-size:24px; font-weight:bold; background:rgba(255,255,255,0.8); border-radius:15px; padding:10px; border: 2px solid #ffd700; margin: 10px auto; width: 60%;}
.star {font-size:110px; color:gold; text-shadow:0 0 30px gold; text-align:center; margin:10px 0;}
.glass-card {padding:25px; border-radius:20px; background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); backdrop-filter:blur(15px); margin-bottom:20px;}
</style>
""", unsafe_allow_html=True)

# --- 3. القاموس الكامل (4 لغات) ---
LANG_DICT = {
    'English': {'motto': "TALK , PAY , DONE .", 'saden': "Saden Security Token", 'home_car': "Smart Control 🏠🚗", 'agent': "🤝 Smart Agent", 'trans': "🔐 Transparency"},
    'Arabic': {'motto': "تكلم ، ادفع ، تم .", 'saden': "أمان سادن: التوكن المتبادل", 'home_car': "التحكم الذكي 🏠🚗", 'agent': "🤝 الوكيل الذكي", 'trans': "🔐 الشفافية والأمان"},
    'Français': {'motto': "PARLE , PAIE , TERMINÉ .", 'saden': "Token Mutuel Saden", 'home
