import streamlit as st
import datetime
import base64
from gtts import gTTS

st.set_page_config(page_title="🌟 FlashDeal Star Assistant 🌟", layout="wide")

# تشغيل نغمة قصيرة
def play_sound(file_name="success.wav"):
    try:
        with open(file_name, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            md = f"""
            <audio autoplay>
            <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass  # لا نعرض تحذيرات مزعجة

# تحويل النص إلى صوت منطوق
def speak_text(text, filename="response.mp3"):
    try:
        tts = gTTS(text=text, lang="ar")
        tts.save(filename)
        audio_file = open(filename, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    except:
        st.warning("⚠️ لم يتم توليد الصوت، تأكد من تثبيت gTTS.")

# سجل الذاكرة
if "memory_log" not in st.session_state:
    st.session_state.memory_log = []

# العنوان والشعار
st.title("🌟 FlashDeal Star Assistant 🌟")
st.subheader("💎 مساعد المنتجات الذكي")

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

# الأمان والتحكم
st.success("✅ الأمان: سادن فعال")
st.write("🏠 تحكم المنزل")
st.toggle("تشغيل/إيقاف المنزل")
st.write("🚗 تحكم السيارة")
st.toggle("تشغيل/إيقاف السيارة")
st.button("📷 الكاميرا")

# التوكنات
token = st.text_input("🔑 أدخل التوكن")
token2 = st.text_input("🔑 التوكن المتبادل", type="password")

# إدخال نوع المنتج
st.subheader("🛒 تقييم المنتجات")
products = st.text_area("أدخل أسماء المنتجات (افصل بينها بفاصلة)")

if st.button("ابحث عن خيارات"):
    if products.strip():
        product_list = [p.strip() for p in products.split(",") if p.strip()]
        options_map = {
            "حاسوب محمول": [
                {"name": "Dell XPS 15", "quality": 0.92, "price": 1500},
                {"name": "MacBook Pro 14", "quality": 0.95, "price": 2000},
                {"name": "Lenovo ThinkPad X1", "quality": 0.89, "price": 1400},
            ],
            "هاتف ذكي": [
                {"name": "iPhone 15 Pro", "quality": 0.96, "price": 1200},
                {"name": "Samsung Galaxy S25", "quality": 0.94, "price": 1100},
                {"name": "Google Pixel 9", "quality": 0.91, "price": 900},
            ]
        }

        for product in product_list:
            st.write(f"📊 أهم الخيارات لـ {product}:")
            options = options_map.get(product, [])
            if not options:
                st.warning(f"⚠️ لا توجد بيانات جاهزة لـ {product}")
                continue

            best_quality = max(options, key=lambda x: x["quality"])
            best_value = min(options, key=lambda x: x["price"]/x["quality"])

            for opt in options:
                response = f"{opt['name']} جودة {opt['quality']*100:.0f}% بسعر {opt['price']}$."
                if opt["quality"] > 0.9:
                    st.success("✅ " + response)
                    play_sound("success.wav")
                elif opt["quality"] > 0.85:
                    st.info("ℹ️ " + response)
                    play_sound("neutral.wav")
                else:
                    st.warning("⚠️ " + response)
                    play_sound("alert.wav")
                speak_text(response)
                st.session_state.memory_log.append(
                    f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - تقييم: {response}"
                )

            # توصية نهائية
            final_msg = f"🔎 أفضل جودة: {best_quality['name']} ({best_quality['quality']*100:.0f}%). أفضل قيمة مقابل السعر: {best_value['name']}."
            st.write(final_msg)
            speak_text(final_msg)
            st.session_state.memory_log.append(
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - توصية: {final_msg}"
            )
    else:
        st.error("⚠️ الرجاء إدخال أسماء المنتجات أولًا.")

# سجل الذاكرة في الشريط الجانبي
st.sidebar.subheader("📝 سجل التقييمات")
if st.session_state.memory_log:
    for entry in st.session_state.memory_log:
        st.sidebar.write(entry)
else:
    st.sidebar.write("لا توجد تقييمات بعد...")
