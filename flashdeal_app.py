import streamlit as st
import time

# --- 1. إعدادات المنصة ---
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. التصميم الجمالي النهائي (تناسق النجوم والشعار) ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #001a33 0%, #003366 100%);
    background-image: url("https://www.transparenttextures.com/patterns/pinetree.png");
    background-blend-mode: overlay;
}
/* العنوان والنجوم الملتصقة */
.header-box { text-align: center; margin-top: -40px; }
.main-title {
    display: inline-block;
    color: #ffffff;
    font-size: 3.5rem;
    font-weight: bold;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.4);
}
.attached-star { color: gold; font-size: 3rem; vertical-align: middle; }

/* النجمة الكبرى تحت العنوان */
.center-star {
    text-align: center;
    font-size: 90px;
    color: gold;
    text-shadow: 0 0 30px gold;
    margin: -15px 0;
}

/* الشعار تحت النجمة مباشرة */
.motto-bar {
    text-align: center;
    color: #000000;
    font-size: 24px;
    font-weight: bold;
    background: rgba(255, 255, 255, 0.9);
    border: 2px solid gold;
    border-radius: 15px;
    padding: 10px 40px;
    width: fit-content;
    margin: 10px auto 25px auto;
}

.time-text {
    text-align: center;
    color: #00ffff;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}

.product-card {
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.1);
    border: 2px solid #00ffcc;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- 3. القاموس اللغوي ---
LANG_DICT = {
    'Arabic': {'motto': "تكلم ، ادفع ، تم .", 'prod': "سماعات كوفيه ستار", 'price': "99.99 $"},
    'English': {'motto': "TALK , PAY , DONE .", 'prod': "Cuffie Star Headphones", 'price': "$99.99"},
    'Italiano': {'motto': "PARLA , PAGA , FATTO .", 'prod': "Cuffie Star", 'price': "99.99 $"}
}

# --- 4. الشريط الجانبي ---
with st.sidebar:
    selected_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    with st.expander("📜 Memory Log", expanded=True):
        for item in reversed(st.session_state.history): st.write(item)

# --- 5. الهيكل البصري (التنفيذ الحرفي لأوامرك) ---

# أ. العنوان بالنجوم الملتصقة ✨My FlashDeal Star✨
st.markdown(f'<div class="header-box"><span class="attached-star">✨</span><span class="main-title">My FlashDeal Star</span><span class="attached-star">✨</span></div>', unsafe_allow_html=True)

# ب. النجمة الكبرى
st.markdown('<div class="center-star">★</div>', unsafe_allow_html=True)

# ج. الشعار تحت النجمة مباشرة
st.markdown(f'<div class="motto-bar">{t["motto"]}</div>', unsafe_allow_html=True)

# د. التوقيت (تاريخ ووقت فقط)
st.markdown(f'<div class="time-text">{time.strftime("%d/%m/%Y - %H:%M:%S")}</div>', unsafe_allow_html=True)

# هـ. أزرار المهام السريعة
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.button("👤 Face ID")
with c2: st.button("🔑 Key")
with c3: st.button("✋ Gesture")
with c4: st.button("🔒 Lock")
with c5: st.button("💎 Trans")

st.divider()

# --- 6. الأمان والتحكم ---
col_sec, col_inf = st.columns(2)
with col_sec:
    st.subheader("🛡️ Saden Security")
    st.camera_input("Verify", label_visibility="collapsed")
with col_inf:
    st.subheader("🏠 Control")
    st.button("🚗 Start Engine", use_container_width=True)
    st.button("🏠 Security", use_container_width=True)

st.divider()

# --- 7. التفاعل والمنتج (الإبقاء على سماعات 99.99 فقط) ---
col_agent, col_prod = st.columns([1.5, 1])

with col_agent:
    st.subheader("🤝 Smart Agent")
    st.text_input("Deal Description", placeholder="Scrivi il tuo comando / اكتب أمرك...")
    if st.button("Execute Deal 🚀", type="primary", use_container_width=True):
        st.balloons()
        add_to_memory("Deal Confirmed")

with col_prod:
    # تم حذف الـ 199.99 تماماً والإبقاء على بضاعة الصورة 2
    st.markdown(f"""
    <div class="product-card">
        <h3 style="color: #00ffcc;">🎧 {t['prod']}</h3>
        <h2 style="color: #ffffff;">{t['price']}</h2>
        <div style="font-size: 60px;">🎧</div>
        <p style="color: #aaa; font-size: 12px; margin-top:10px;">Innovation Team Edition 2026</p>
    </div>
    """, unsafe_allow_html=True)

st.chat_input("Sony-Agent: Pitch mode ready...")
