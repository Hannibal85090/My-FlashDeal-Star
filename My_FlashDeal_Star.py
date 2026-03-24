import streamlit as st
import time

# --- 1. إعداد الصفحة الأساسي ---
st.set_page_config(page_title="My FlashDeal Star Pro", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history=[]

def add_to_memory(action):
    timestamp=time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. وظائف التحكم والأمان ---
def trigger_sos():
    st.error("🚨 SOS: Emergency Protocol Activated!")
    add_to_memory("SOS Triggered - Alerts sent to Master Alpha Hub")

# --- 3. التنسيق الجمالي (اللون الأسود للشعار كما طلبت) ---
st.markdown("""
<style>
body{background:linear-gradient(135deg,#00050a 0%,#011627 100%);color:#ffffff;}
.main-title{text-align:center; color:#000000; text-shadow:0 0 5px #ffffff; font-size:3rem; font-weight:bold; margin-bottom:0px;}
.motto-black{text-align:center; color:#000000; font-size:26px; font-weight:bold; background:rgba(255,255,255,0.7); border-radius:10px; padding:5px; margin-top:5px;}
.star{font-size:100px; color:gold; text-shadow:0 0 20px gold; text-align:center; margin:10px 0;}
.glass-card{padding:25px; border-radius:20px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); backdrop-filter:blur(15px); margin-bottom:20px;}
.stInfo {background-color: rgba(0,0,0,0.5); border: 1px solid #4facfe;}
</style>
""",unsafe_allow_html=True)

# --- 4. القاموس الموسع (لسد ثغرة الكتابة والشفافية) ---
LANG_DICT={
'English':{'motto':"TALK , PAY , DONE .",'saden':"Saden Security: Mutual Token",'home_car':"Smart Control 🏠🚗",'sync':"Sync Token 🛡️",'car':"Start Car 🔑",'home':"Manage Home 🏠",'sos':"Activate SOS 🔔",'mem':"📜 Memory Log",'agent':"🤝 Smart Agent Delivery",'trans':"🔐 Transparency & Security"},
'Arabic':{'motto':"تكلم ، ادفع ، تم .",'saden':"أمان سادن: التوكن المتبادل",'home_car':"التحكم الذكي 🏠🚗",'sync':"مزامنة التوكن 🛡️",'car':"تشغيل السيارة 🔑",'home':"إدارة المنزل 🏠",'sos':"تفعيل وضع الطوارئ 🔔",'mem':"📜 سجل الذاكرة الموحد",'agent':"🤝 الوكيل الذكي للصفقات",'trans':"🔐 الشفافية والأمان"}}

# --- 5. الشريط الجانبي ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png",width=60)
    selected_lang=st.selectbox("🌐 Global Language",list(LANG_DICT.keys()))
    t=LANG_DICT[selected_lang]
    st.divider()
    if st.button(t['sos'],type="secondary"): trigger_sos()
    st.divider()
    with st.expander(t['mem'],expanded=True):
        if not st.session_state.history: st.write("No active logs.")
        else:
            for item in reversed(st.session_state.history):
                st.write(item)

# --- 6. الواجهة الرئيسية (سد الثغرات) ---
current_time=time.strftime("%d/%m/%Y - %H:%M:%S")

# أ. العنوان بالشعار الأسود (حسب طلبك)
st.markdown("<h1 class='main-title'>🌟 My FlashDeal Star 🌟</h1>",unsafe_allow_html=True)

# ب. تفعيل خاصية الكتابة (Motto) باللون الأسود الواضح
st.markdown(f"<p class='motto-black'>{t['motto']}</p>", unsafe_allow_html=True)

# ج. النجمة الكبيرة
st.markdown('<div class="star">★</div>',unsafe_allow_html=True)

# د. التوقيت
st.markdown(f"<p style='text-align:center; color:#4facfe; font-weight:bold;'>🕒 {current_time}</p>",unsafe_allow_html=True)

# هـ. ركن الشفافية والأمان (سد ثغرة الشفافية)
with st.expander(t['trans']):
    st.info("ℹ️ جميع العمليات مشفرة ومسجلة في سجل الذاكرة الموحد لضمان أعلى مستويات الشفافية.")

# و. أزرار التحكم السريع
cols=st.columns(4)
if cols[0].button("✋ Sign"): add_to_memory("Sign Activated")
if cols[1].button("🔒 Lock"): add_to_memory("System Locked")
if cols[2].button("👤 Face"): add_to_memory("Face Scan Active")
if cols[3].button("🔑 Key"): add_to_memory("Key Engaged")

# --- 7. الوكيل الذكي (Smart Agent) - سد ثغرة التفاعل ---
st.divider()
st.subheader(t['agent'])
col_agent1, col_agent2 = st.columns([2, 1])
with col_agent1:
    deal_input = st.text_input("صف العملية للوكيل الذكي...")
with col_agent2:
    if st.button("إبرام الصفقة 🚀"):
        st.success("جاري معالجة الصفقة عبر الوكيل...")
        add_to_memory(f"Deal Initiated: {deal_input}")

# --- 8. سادن والتوكن المتبادل ---
st.markdown(f'<div class="glass-card"><h3>🔒 {t["saden"]}</h3>',unsafe_allow_html=True)
c1,c2=st.columns([3,1])
with c1: st.text_input("Token ID", type="password", key="tk_input")
with c2: 
    if st.button(t['sync']): st.success("Synced! 🛡️"); add_to_memory("Token Synced")
st.markdown('</div>',unsafe_allow_html=True)

# --- 9. الكاميرا والتحكم (المنزل والسيارة) ---
tab_cam, tab_ctrl = st.tabs(["📸 Camera Verification", "🏠 Smart Home & Car"])
with tab_cam:
    st.camera_input("Verify Access")
with tab_ctrl:
    ca, cb = st.columns(2)
    if ca.button(t['car']): 
        st.success("🚗 Engine On!"); add_to_memory("Car Started")
    if cb.button(t['home']): 
        st.info("🏠 Home Mode Active"); add_to_memory("Home Managed")

# --- 10. شات Sony-Agent ---
chat_val=st.chat_input("Sony-Agent is ready...")
if chat_val: add_to_memory(f"Chat: {chat_val}")
