import streamlit as st
import time

# --- [1. إعدادات النظام وتفعيل محرك اللغات] ---
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟", layout="wide")

if 'lang' not in st.session_state:
    st.session_state.lang = "Arabic"

# قاموس اللغات الشامل لجميع الأجزاء (17)
translations = {
    "Arabic": {
        "motto": ". تكلم ، ادفع ، تم .", "saden": "🛡️ أمان سادن", "assets": "🏠 التحكم في الأصول",
        "car": "🚗 تشغيل السيارة", "home": "🏠 أمن المنزل", "deal": "🤝 إبرام الصفقة",
        "sony": "🤝 الوكيل صوني", "log": "سجل الذاكرة", "ready": "النظام جاهز للسيادة",
        "token": "مستطيل التوكن", "mutual": "التوكن المتبادل 👁️", "cert": "📜 شهادة إتمام الصفقة"
    },
    "English": {
        "motto": ". Speak , Pay , Done .", "saden": "🛡️ Saden Security", "assets": "🏠 Asset Control",
        "car": "🚗 Start Engine", "home": "🏠 Home Security", "deal": "🤝 Finalize Deal",
        "sony": "🤝 Sony Agent", "log": "Memory Log", "ready": "System Sovereign Ready",
        "token": "Token Box", "mutual": "Mutual Token 👁️", "cert": "📜 Deal Certificate"
    },
    "Italiano": {
        "motto": ". Parla , Paga , Fatto .", "saden": "🛡️ Sicurezza Saden", "assets": "🏠 Controllo Asset",
        "car": "🚗 Avvia Motore", "home": "🏠 Sicurezza Casa", "deal": "🤝 Concludi Affare",
        "sony": "🤝 Agente Sony", "log": "Registro", "ready": "Sistema Pronto",
        "token": "Riquadro Token", "mutual": "Token Mutuo 👁️", "cert": "📜 Certificato Affare"
    }
}

# --- [2. الهندسة البصرية المصفاة - CSS] ---
st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #001a33 0%, #003366 100%); color: white; }
    .header-box { text-align: center; margin-top: -60px; }
    .main-title { color: white; font-size: 50px; font-weight: bold; text-shadow: 0 0 20px #fff; display: inline-block; vertical-align: middle; }
    .star-side { color: gold; font-size: 40px; margin: 0 15px; vertical-align: middle; }
    .star-mega { text-align: center; font-size: 80px; color: gold; text-shadow: 0 0 35px gold; margin-top: -25px; }
    .motto-bar { background: white; color: black; font-size: 24px; font-weight: bold; padding: 10px 40px; border-radius: 12px; border: 3px solid gold; width: fit-content; margin: 10px auto; }
    .white-card { background: white; border-radius: 12px; padding: 12px; border: 2px solid gold; margin-bottom: 10px; }
    .black-text { color: black !important; font-weight: 900; font-size: 20px; border-bottom: 2px solid #333; }
</style>
""", unsafe_allow_html=True)

# --- [3. الشريط الجانبي - 17, 18, 20] ---
with st.sidebar:
    st.session_state.lang = st.selectbox("🌐 Languages / اللغات", ["Arabic", "English", "Italiano"], index=0)
    t = translations[st.session_state.lang] # استخراج الترجمة الحية
    st.divider()
    # 18. خيار Master Alpha
    st.radio("System Mode", ["Standard", "Master Alpha 🔓"], index=1)
    st.divider()
    # 20. سجل الذاكرة
    with st.expander(f"📜 {t['log']}", expanded=True):
        st.write(f"[{time.strftime('%H:%M')}] {t['ready']}")

# --- [4. العرض الرئيسي - 1-5] ---
st.markdown(f'<div class="header-box"><span class="star-side">✨</span><div class="main-title">My FlashDeal Star</div><span class="star-side">✨</span></div>', unsafe_allow_html=True)
st.markdown('<div class="star-mega">★</div>', unsafe_allow_html=True)
st.markdown(f'<div class="motto-bar">{t["motto"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="text-align:center; color:#00ffff; font-family:monospace;">{time.strftime("%d/%m/%Y - %H:%M:%S")}</div>', unsafe_allow_html=True)

# --- [6. الأزرار الخماسية - وجه، مفتاح، يد، قفل، جوهرة] ---
st.write("")
cols = st.columns(5)
icons = ["👤 Face ID", "🔑 Key", "✋ Hand", "🔒 Lock", "💎 Jewel"]
for i, col in enumerate(cols): col.button(icons[i], use_container_width=True, key=f"btn_{i}")

st.divider()

# --- [7-11. أمان سادن والأصول والكاميرا والتوكن] ---
col_l, col_r = st.columns(2)
with col_l:
    st.markdown(f'<div class="white-card"><div class="black-text">{t["saden"]}</div></div>', unsafe_allow_html=True)
    st.camera_input("Scan", key="cam_1", label_visibility="collapsed") # 9
    st.text_input(t["token"], type="password", key="tk_1") # 10
    st.text_input(t["mutual"], type="password", key="tk_2") # 11

with col_r:
    st.markdown(f'<div class="white-card"><div class="black-text">{t["assets"]}</div></div>', unsafe_allow_html=True)
    st.button(t["car"], use_container_width=True) # 8
    st.button(t["home"], use_container_width=True) # 8
    st.info("Sovereign Control Active")

st.divider()

# --- [12-16. الوكيل صوني، التصافح، والصفقة] ---
col_sony, col_prod = st.columns([2, 1])
with col_sony:
    st.subheader(t["sony"]) # 16
    st.text_area("⌨️ Interaction", placeholder="Write to Sony...", key="sony_m", label_visibility="collapsed") # 13
    
    if st.button(t["deal"], type="primary", use_container_width=True): # 12
        st.balloons() # 13
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # 13
        st.markdown(f'<div style="border:4px double gold; padding:20px; text-align:center; border-radius:12px; background:rgba(0,0,0,0.5);"><h3>{t["cert"]}</h3><p>Verified by <b>Master Alpha</b></p></div>', unsafe_allow_html=True) # 14

with col_prod:
    # 15. المنتج والثمن
    st.markdown('<div style="border:2px solid #00ffcc; border-radius:15px; padding:15px; text-align:center; background:rgba(255,255,255,0.05);"><h4>سماعات كوفيه ستار</h4><h2>99.99 $</h2><div style="font-size:55px;">🎧</div></div>', unsafe_allow_html=True)

# 13. التفاعل السفلي
st.chat_input(f"Sony Agent: {st.session_state.lang} Active...")
