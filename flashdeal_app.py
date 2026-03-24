import streamlit as st
import time

# --- أ. إعدادات المنصة والهوية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- ب. الهندسة الجمالية (CSS) ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #001a33 0%, #003366 100%);
}
/* العنوان المحاط بالنجوم الملتصقة */
.title-container { text-align: center; padding-top: 20px; }
.main-header {
    display: inline-block;
    color: white;
    font-size: 3.8rem;
    font-weight: bold;
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
}
.star-attached { color: gold; font-size: 3.2rem; vertical-align: middle; }

/* النجمة الكبرى المركزية */
.mega-star {
    text-align: center;
    font-size: 100px;
    color: gold;
    text-shadow: 0 0 40px gold;
    margin: -20px 0;
}

/* الشعار المعتمد */
.motto-box {
    text-align: center;
    color: #111;
    font-size: 26px;
    font-weight: bold;
    background: #fff;
    border: 3px solid gold;
    border-radius: 20px;
    padding: 12px 50px;
    width: fit-content;
    margin: 15px auto;
}

/* التوقيت الحي باللون السيان */
.live-clock {
    text-align: center;
    color: #00ffff;
    font-size: 22px;
    font-weight: bold;
    font-family: 'Courier New', monospace;
    margin-bottom: 30px;
}

/* بطاقة السماعات المعتمدة (صورة 2) */
.product-frame {
    padding: 30px;
    border-radius: 25px;
    background: rgba(255,255,255,0.05);
    border: 2px solid #00ffcc;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- ج. القاموس واللغات ---
LANG_DICT = {
    'Arabic': {'motto': "تكلم ، ادفع ، تم .", 'prod': "سماعات كوفيه ستار", 'price': "99.99 $"},
    'English': {'motto': "TALK , PAY , DONE .", 'prod': "Cuffie Star Headphones", 'price': "$99.99"},
    'Italiano': {'motto': "PARLA , PAGA , FATTO .", 'prod': "Cuffie Star", 'price': "99.99 $"}
}

# --- د. شريط التحكم الجانبي ---
with st.sidebar:
    selected_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    with st.expander("📜 Memory Log", expanded=True):
        for item in reversed(st.session_state.history): st.write(item)

# --- هـ. تنفيذ الواجهة الإبداعية (بالترتيب المطلوب) ---

# 1. العنوان ✨My FlashDeal Star✨
st.markdown(f'<div class="title-container"><span class="star-attached">✨</span><span class="main-header">My FlashDeal Star</span><span class="star-attached">✨</span></div>', unsafe_allow_html=True)

# 2. النجمة الكبرى تحت العنوان مباشرة
st.markdown('<div class="mega-star">★</div>', unsafe_allow_html=True)

# 3. الشعار تحت النجمة
st.markdown(f'<div class="motto-box">{t["motto"]}</div>', unsafe_allow_html=True)

# 4. التوقيت والتاريخ الحي
current_time = time.strftime("%d/%m/%Y - %H:%M:%S")
st.markdown(f'<div class="live-clock">{current_time}</div>', unsafe_allow_html=True)

# 5. أزرار التحكم الفوري
cols = st.columns(5)
with cols[0]: st.button("👤 Face ID")
with cols[1]: st.button("🔑 Smart Key")
with cols[2]: st.button("✋ Gesture")
with cols[3]: st.button("🔒 Lock/Sync")
with cols[4]: st.button("💎 Trans")

st.divider()

# --- و. قلب النظام (سادن والتحكم بالأصول) ---
col_saden, col_infra = st.columns(2)
with col_saden:
    st.subheader("🛡️ Saden Security Hub")
    st.camera_input("Biometric Scan", label_visibility="collapsed")
with col_infra:
    st.subheader("🏠 Infrastructure Control")
    st.button("🚗 Start Car Engine", use_container_width=True)
    st.button("🏠 Home Security", use_container_width=True)

st.divider()

# --- ز. الوكيل والمنتج النهائي (بدون أي دخلاء) ---
col_agent, col_prod = st.columns([1.5, 1])

with col_agent:
    st.subheader("🤝 Smart Agent")
    st.text_input("Deal Description", placeholder="اكتب تفاصيل الصفقة...")
    if st.button("إبرام الصفقة 🚀", type="primary", use_container_width=True):
        st.balloons()
        add_to_memory(f"Deal for {t['prod']} Executed")

with col_prod:
    # تم تثبيت سماعات كوفيه ستار فقط (صورة 2) وحذف الـ 199.99 تماماً
    st.markdown(f"""
    <div class="product-frame">
        <h3 style="color: #00ffcc;">🎧 {t['prod']}</h3>
        <h2 style="color: #ffffff;">{t['price']}</h2>
        <div style="font-size: 80px;">🎧</div>
        <p style="color: #888; font-size: 14px; margin-top:15px;">Innovation Team Edition 2026</p>
    </div>
    """, unsafe_allow_html=True)

st.chat_input("Sony-Agent: Pitch mode ready...")
