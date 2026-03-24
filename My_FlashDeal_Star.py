import streamlit as st
import time

# --- 1. إعداد الصفحة ---
st.set_page_config(page_title="FlashDeal Star | Premium Edition", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history=[]

def add_to_memory(action):
    timestamp=time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. التنسيق الجمالي (خلفية الصنوبر الزرقاء والاحتفالية) ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #001a33 0%, #003366 100%);
    background-image: url("https://www.transparenttextures.com/patterns/pinetree.png");
    background-blend-mode: overlay;
}
.main-title {text-align:center; color:#000000; text-shadow:0 0 10px #ffffff; font-size:3.5rem; font-weight:bold; margin-top: -50px;}
.motto-black {text-align:center; color:#000000; font-size:24px; font-weight:bold; background:rgba(255,255,255,0.8); border-radius:15px; padding:10px; border: 2px solid #ffd700; margin: 10px auto; width: 50%;}
.star {font-size:100px; color:gold; text-shadow:0 0 30px gold; text-align:center; margin:5px 0;}
.product-card {padding:20px; border-radius:20px; background:rgba(0,0,0,0.4); border:2px solid #1E88E5; text-align:center; color:white;}
.price-tag {font-size:30px; color:#00ffcc; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# --- 3. القاموس الكامل (4 لغات) ---
LANG_DICT = {
    'English': {'motto': "TALK , PAY , DONE .", 'saden': "Saden Security Token", 'prod_name': "FlashDeal Smart Star", 'price': "$199.99"},
    'Arabic': {'motto': "تكلم ، ادفع ، تم .", 'saden': "أمان سادن: التوكن المتبادل", 'prod_name': "نجمة فلاش ديل الذكية", 'price': "199.99 دولار"},
    'Français': {'motto': "PARLE , PAIE , TERMINÉ .", 'saden': "Token Saden", 'prod_name': "Étoile Intelligente", 'price': "199.99 €"},
    'Italiano': {'motto': "PARLA , PAGA , FATTO .", 'saden': "Token Saden", 'prod_name': "Stella Intelligente", 'price': "199.99 €"}
}

# --- 4. الشريط الجانبي (Master Alpha) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    acc = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])
    if acc == "Master Alpha 🔓": st.success("Master Alpha Active")
    st.divider()
    if st.button("🎉 اطلق الاحتفالية / Celebrate"):
        st.balloons()
        st.snow()
        st.success("Celebration Mode Active! 🎶")

# --- 5. الهيكل الجديد (ترتيبك المقترح: عنوان -> شعار -> أزرار) ---

# أولاً: العنوان
st.markdown("<h1 class='main-title'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

# ثانياً: الشعار الأسود تحت العنوان مباشرة
st.markdown(f"<p class='motto-black'>{t['motto']}</p>", unsafe_allow_html=True)

# النجمة الكبرى
st.markdown('<div class="star">★</div>', unsafe_allow_html=True)

# ثالثاً: أزرار التحكم (تحت الشعار)
cols = st.columns(4)
if cols[0].button("✋ Sign"): add_to_memory("Sign Activated")
if cols[1].button("🔒 Lock"): add_to_memory("System Locked")
if cols[2].button("👤 Face"): add_to_memory("Face Scan Active")
if cols[3].button("🔑 Key"): add_to_memory("Key Engaged")

st.divider()

# --- 6. عرض المنتج (إضافة اختيارية رائعة) ---
col_prod, col_space = st.columns([1, 1])
with col_prod:
    st.markdown(f"""
    <div class="product-card">
        <h3>💎 {t['prod_name']}</h3>
        <p>Advanced AI Control & Financial Security</p>
        <div class="price-tag">{t['price']}</div>
    </div>
    """, unsafe_allow_html=True)
    # صورة المنتج (أيقونة تعبيرية كبديل لصورة برمجية)
    st.image("https://img.icons8.com/fluency/240/000000/star-burst.png", caption="The Future of FinTech")

# --- 7. سادن والكاميرا والوكيل ---
tab_cam, tab_agent = st.tabs(["📸 Camera Verification", "🤝 Smart Agent & Saden"])
with tab_cam:
    st.camera_input("Verify Access")
with tab_agent:
    st.markdown(f"### 🔒 {t['saden']}")
    st.text_input("Token ID", type="password")
    if st.button("Sync Now 🛡️"): st.success("Synced!")

st.chat_input("Sony-Agent: How can I assist you today?")
