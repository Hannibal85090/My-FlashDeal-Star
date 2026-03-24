import streamlit as st
import time

# --- 1. إعدادات المنصة ---
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. التصميم الجمالي المطور (التنسيق النهائي) ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #001a33 0%, #003366 100%);
    background-image: url("https://www.transparenttextures.com/patterns/pinetree.png");
    background-blend-mode: overlay;
}
/* العنوان المحاط بالنجوم الملتصقة */
.main-title {
    text-align: center;
    color: #ffffff;
    font-size: 3.2rem;
    font-weight: bold;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
    margin-bottom: 5px;
}
.side-star { color: gold; font-size: 2.5rem; vertical-align: middle; }

/* النجمة الكبرى المركزية */
.big-star {
    text-align: center;
    font-size: 80px;
    color: gold;
    text-shadow: 0 0 30px gold;
    margin: -10px 0;
}

/* الشعار تحت النجمة مباشرة */
.motto-box {
    text-align: center;
    color: #000000;
    font-size: 22px;
    font-weight: bold;
    background: rgba(255, 255, 255, 0.9);
    border: 2px solid gold;
    border-radius: 12px;
    padding: 10px 30px;
    width: fit-content;
    margin: 10px auto 30px auto;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}

/* التوقيت الأنيق */
.time-display {
    text-align: center;
    color: #00ffff;
    font-size: 18px;
    font-family: 'Courier New', monospace;
    font-weight: bold;
    margin-bottom: 20px;
}

/* بطاقة المنتج النظيفة */
.product-card {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.08);
    border: 1px solid gold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- 3. القاموس اللغوي ---
LANG_DICT = {
    'Arabic': {'motto': "تكلم ، ادفع ، تم .", 'agent': "🤝 الوكيل الذكي", 'prod': "نجمة فلاش ديل الذكية", 'price': "199.99 $"},
    'English': {'motto': "TALK , PAY , DONE .", 'agent': "🤝 Smart Agent", 'prod': "FlashDeal Smart Star", 'price': "$199.99"},
    'Italiano': {'motto': "PARLA , PAGA , FATTO .", 'agent': "🤝 Agente Intelligente", 'prod': "Stella Smart", 'price': "199.99 $"}
}

# --- 4. الواجهة الجانبية (Memory Log) ---
with st.sidebar:
    selected_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    with st.expander("📜 Memory Log", expanded=True):
        for item in reversed(st.session_state.history): st.write(item)

# --- 5. الهيكل البصري (التنفيذ بحذافيره) ---

# أ. العنوان والنجوم الملتصقة
st.markdown(f'<div class="main-title"><span class="side-star">✨</span>My FlashDeal Star<span class="side-star">✨</span></div>', unsafe_allow_html=True)

# ب. النجمة الأكبر تحت العنوان
st.markdown('<div class="big-star">★</div>', unsafe_allow_html=True)

# ج. الشعار تحت النجمة مباشرة
st.markdown(f'<div class="motto-box">{t["motto"]}</div>', unsafe_allow_html=True)

# د. التوقيت (تاريخ ووقت فقط)
st.markdown(f'<div class="time-display">{time.strftime("%d/%M/%Y - %H:%M:%S")}</div>', unsafe_allow_html=True)

# هـ. أزرار التحكم السريع (Face ID, Gesture, etc.)
c1, c2, c3, c4, c5 = st.columns(5)
with c1: st.button("👤 Face ID")
with c2: st.button("🔑 Key")
with c3: st.button("✋ Gesture")
with c4: st.button("🔒 Lock")
with c5: st.button("💎 Trans")

st.divider()

# --- 6. المحتوى الوظيفي (نظام سادن والتحكم) ---
col_sec, col_inf = st.columns(2)
with col_sec:
    st.subheader("🛡️ Saden Security Hub")
    st.camera_input("Verification", label_visibility="collapsed")
with col_inf:
    st.subheader("🏠 Infrastructure")
    st.button("🚗 Start Engine", use_container_width=True)
    st.button("🏠 Home Security", use_container_width=True)

st.divider()

# --- 7. الوكيل الذكي والمنتج (بدون أسعار دخيلة) ---
col_agent, col_prod = st.columns([1.5, 1])

with col_agent:
    st.subheader(t['agent'])
    st.text_input("Transaction Context", placeholder="Scrivi il tuo comando / اكتب أمرك...")
    if st.button("إبرام الصفقة 🚀", type="primary", use_container_width=True):
        st.balloons()
        add_to_memory("Deal Executed")

with col_prod:
    # تم تثبيت السعر ليكون بالدولار فقط وإزالة أي عملات أخرى دخيلة
    st.markdown(f"""
    <div class="product-card">
        <h3 style="color: gold;">💎 {t['prod']}</h3>
        <h2 style="color: #00ffcc;">{t['price']}</h2>
        <div style="font-size: 50px;">⭐</div>
        <p style="color: #aaa; font-size: 12px;">Innovation Team Edition 2026</p>
    </div>
    """, unsafe_allow_html=True)

# حقل الدردشة السفلي الخاص بـ Sony-Agent
st.chat_input("Sony-Agent: Pitch Day mode active...")
