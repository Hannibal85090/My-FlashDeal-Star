import streamlit as st
import datetime
from transformers import pipeline
import base64

st.set_page_config(page_title="🌟 My FlashDeal Star 🌟", layout="wide")

# وظيفة لتشغيل صوت قصير عند النجاح
def play_success_sound():
    sound_file = "success.wav"  # ملف صوتي قصير (ضعه في مجلد المشروع)
    with open(sound_file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        md = f"""
        <audio autoplay>
        <source src="data:audio/wav;base64,{b64}" type="audio/wav">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# العنوان والشعار
st.title("🌟 My FlashDeal Star 🌟")
st.markdown("⭐")
st.subheader("💎 شعار التطبيق")

# التوقيت والتاريخ
now = datetime.datetime.now()
st.write(f"🕒 {now.strftime('%A, %d %B %Y %H:%M:%S')}")

# الأزرار بالأيقونات
col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.button("🙂 Face")
with col2: st.button("🔑 Key")
with col3: st.button("✋ Hand")
with col4: st.button("🔒 Lock")
with col5: st.button("💎 Gem")

# الأمان
st.success("✅ الأمان: سادن فعال")

# التحكم
st.write("🏠 تحكم المنزل")
st.toggle("تشغيل/إيقاف المنزل")
st.write("🚗 تحكم السيارة")
st.toggle("تشغيل/إيقاف السيارة")

# الكاميرا
st.button("📷 الكاميرا")

# التوكنات
token = st.text_input("🔑 أدخل التوكن")
token2 = st.text_input("🔑 التوكن المتبادل", type="password")

# سجل الذاكرة
if "memory_log" not in st.session_state:
    st.session_state.memory_log = []

# الصفقة
st.write("🤝 إبرام الصفقة")
deal_text = st.text_area("اكتب للتفاعل")
if st.button("إتمام الصفقة"):
    st.balloons()
    st.success("🎉 تم إتمام الصفقة!")
    st.info("📜 شهادة إتمام الصفقة صادرة")
    play_success_sound()
    if deal_text:
        st.session_state.memory_log.append(f"صفقة: {deal_text} - {now.strftime('%Y-%m-%d %H:%M:%S')}")

# سماعات وسعر
st.write("🎧 سماعات")
st.write("💲 السعر: 99")

# الذكاء الاصطناعي مع ردود ذكية
st.subheader("🤖 AI Agent")
ai_input = st.text_area("أدخل نص للتحليل")
if ai_input:
    sentiment_analyzer = pipeline("sentiment-analysis")
    result = sentiment_analyzer(ai_input)[0]
    st.write(f"Sentiment: {result['label']} (score: {result['score']:.2f})")
    if result['label'] == "POSITIVE":
        st.success("✅ التحليل إيجابي! أقترح تسجيل هذه الصفقة في سجل الذاكرة.")
    elif result['label'] == "NEGATIVE":
        st.warning("⚠️ التحليل سلبي. ربما تحتاج إلى إعادة النظر في الصفقة.")
    else:
        st.info("ℹ️ التحليل محايد. يمكنك المتابعة بحذر.")
    play_success_sound()

# وضع الأوامر (Command Mode)
st.subheader("⌨️ Command Mode")
command = st.text_input("أدخل أمر (مثال: /deal صفقة جديدة)")
if command:
    if command.startswith("/deal"):
        text = command.replace("/deal", "").strip()
        st.session_state.memory_log.append(f"صفقة بالأمر: {text} - {now.strftime('%Y-%m-%d %H:%M:%S')}")
        st.success(f"تم تسجيل صفقة: {text}")
        play_success_sound()
    elif command.startswith("/ai"):
        text = command.replace("/ai", "").strip()
        sentiment_analyzer = pipeline("sentiment-analysis")
        result = sentiment_analyzer(text)[0]
        st.write(f"AI Command Sentiment: {result['label']} (score: {result['score']:.2f})")
        play_success_sound()
    elif command.startswith("/lang"):
        lang = command.replace("/lang", "").strip()
        st.success(f"تم تغيير اللغة إلى: {lang}")
        play_success_sound()
    else:
        st.warning("⚠️ أمر غير معروف")

# الشريط الجانبي
st.sidebar.subheader("🌐 اللغات")
st.sidebar.radio("اختر اللغة:", ["عربي", "Français", "English"])
st.sidebar.subheader("⚙️ الوضعيات")
st.sidebar.radio("اختر الوضع:", ["Standard", "Master Alpha"])
st.sidebar.subheader("📝 سجل الذاكرة")
if st.session_state.memory_log:
    for entry in st.session_state.memory_log:
        st.sidebar.write(entry)
else:
    st.sidebar.write("لا توجد تفاعلات بعد...")
