import streamlit as st
import time

# --- 1. إعدادات الصفحة والذاكرة الموحدة ---
st.set_page_config(page_title="FlashDeal Star | Final Pitch", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
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
/* العنوان الرئيسي */
.main-title {text-align:center; color:#000000; text-shadow:0 0 12px #ffffff; font-size:3.5rem; font-weight:bold; margin-top: -40px;}
/* الشعار الأسود (Motto) */
.motto-black {text-align:center; color:#000000; font-size:24px; font-weight:bold; background:rgba(255,255,255,0.85); border-radius:15px; padding:12px; border: 2px solid #ffd700; margin: 10px auto; width: 60%; box-shadow: 0 4px 15px rgba(0,0,0,0.3);}
/* النجمة الكبرى */
.star {font-size:100px; color:gold; text-shadow:0 0 35px gold; text-align:center; margin:5px 0;}
/* بطاقة الشهادة */
.cert-card {border: 3px double gold; padding: 25px; border-radius: 15px; background: rgba(0,0,0,0.8); text-align: center; color: white; margin-top: 20px;}
/* بطاقة المنتج */
.glass-product {padding:20px; border-radius:20px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); backdrop-filter:blur(10px); text-align:center;}
</style>
""", unsafe_allow_html=True)

# --- 3. القاموس اللغوي (4 لغات) ---
LANG_DICT = {
    'English': {'motto': "TALK , PAY , DONE .", 'saden': "Saden Security Token", 'agent': "🤝 Smart Agent", 'exec': "Execute Deal 🚀", 'cert': "OFFICIAL DEAL CERTIFICATE", 'price': "$199.99", 'prod': "FlashDeal Smart Star"},
    'Arabic': {'motto': "تكلم ، ادفع ، تم .", 'saden': "أمان سادن: التوكن المتبادل", 'agent': "🤝 الوكيل الذكي", 'exec': "إبرام الصفقة 🚀", 'cert': "شهادة الصفقة الرسمية", 'price': "199.99 $", 'prod': "نجمة فلاش ديل الذكية"},
    'Français': {'motto': "PARLE , PAIE , TERMINÉ .", 'saden': "Token Mutuel Saden", 'agent': "🤝 Agent Intelligent", 'exec': "Conclure l'Accord 🚀", 'cert': "CERTIFICAT OFFICIEL", 'price': "199.99 €", 'prod': "Étoile Smart"},
    'Italiano': {'motto': "PARLA , PAGA , FATTO .", 'saden': "Sicurezza Saden", 'agent': "🤝 Agente Intelligente", 'exec': "Concludi l'Affare 🚀", 'cert': "CERTIFICATO UFFICIALE", 'price': "199.99 €", 'prod': "Stella Smart"}
}

# --- 4. الشريط الجانبي (Master Alpha 🔓) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=55)
    selected_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    
    acc_level = st.radio("Access Level", ["Standard User", "Master Alpha 🔓"])
    if acc_level == "Master Alpha 🔓":
        st.success("Master Alpha Mode: Active")
        add_to_memory("Master Alpha Authenticated")
    
    st.divider()
    with st.expander("📜 Memory Log / سجل الذاكرة", expanded=True):
        if not st.session_state.history: st.write("Waiting for actions...")
        else:
            for item in reversed(st.session_state.history):
                st.write(item)

# --- 5. الهيكل الرئيسي (عنوان -> شعار -> أزرار) ---

# أولاً: العنوان الرئيسي
st.markdown("<h1 class='main-title'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

# ثانياً: الشعار الأسود (Motto)
st.markdown(f"<p class='motto-black'>{t['motto']}</p>", unsafe_allow_html=True)

# النجمة الكبيرة
st.markdown('<div class="star">★</div>', unsafe_allow_html=True)

# ثالثاً: أزرار التحكم العلوية
top_cols = st.columns(4)
if top_cols[0].button("✋ Sign"): add_to_memory("Sign Detected")
if top_cols[1].button("🔒 Lock"): add_to_memory("System Locked")
if top_cols[2].button("👤 Face"): add_to_memory("Face Scan Active")
if top_cols[3].button("🔑 Key"): add_to_memory("Key Engaged")

st.divider()

# --- 6. الوكيل الذكي والمنتج (الاحتفالية والشهادة) ---
c_left, c_right = st.columns([1.5, 1])

with c_left:
    st.subheader(t['agent'])
    deal_desc = st.text_input("Deal details / تفاصيل الصفقة", placeholder="Ex: Supply Chain Agreement")
    
    # عند الضغط على الزر تنطلق الاحتفالية والشهادة والموسيقى تلقائياً
    if st.button(t['exec'], type="primary", use_container_width=True):
        st.balloons()
        st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        
        st.success("TRANSACTION SECURED! ✅")
        st.markdown(f"""
        <div class="cert-card">
            <h2 style="color: gold;">{t['cert']}</h2>
            <hr style="border: 0.5px solid gold;">
            <p style="font-size: 20px;"><b>{deal_desc if deal_desc else "Standard FlashDeal Asset"}</b></p>
            <p>Timestamp: {time.strftime("%d/%m/%Y - %H:%M:%S")}</p>
            <p style="color: #00ffcc; font-weight: bold;">Verified by Master Alpha 🔓</p>
            <p style="font-size: 10px; color: #888;">Hash: SADEN-2026-CONFIRMED</p>
        </div>
        """, unsafe_allow_html=True)
        add_to_memory(f"Deal Certified: {deal_desc}")

with c_right:
    # سد ثغرة الرابط المكسور باستخدام أيقونة احترافية مضمونة
    st.markdown(f"""
    <div class="glass-product">
        <h4 style="color: gold;">💎 {t['prod']}</h4>
        <p style="font-size: 32px; color: #00ffcc; font-weight: bold; margin-bottom: 0px;">{t['price']}</p>
        <div style="font-size: 100px; margin: 10px 0;">⭐</div>
        <p style="font-size: 14px; color: #aaa;">Limited Innovation Team Edition</p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. سادن والتحكم المنزلي والسيارة ---
st.divider()
tab1, tab2 = st.tabs(["🔒 Saden Security", "🏠 Smart Home & Car"])

with tab1:
    st.markdown(f"### {t['saden']}")
    sc1, sc2 = st.columns([3, 1])
    with sc1: st.text_input("Mutual Token Code", type="password", key="saden_key")
    with sc2: 
        if st.button("Verify🛡️"): 
            st.toast("Linked!")
            add_to_memory("Token Verified")
    st.camera_input("Identity Verification")

with tab2:
    ca, cb = st.columns(2)
    if ca.button("🚗 Start Car Engine"): 
        st.success("Engine Started!"); add_to_memory("Car Active")
    if cb.button("🏠 Home Security"): 
        st.info("Home Link Active"); add_to_memory("Home Managed")

st.chat_input("Sony-Agent: Pitch Day mode enabled. How can I assist?")
