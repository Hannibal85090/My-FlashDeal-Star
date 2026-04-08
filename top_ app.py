import streamlit as st
import datetime
from transformers import pipeline
import base64

st.set_page_config(page_title="🌟 Product Quality Evaluator 🌟", layout="wide")

# وظيفة لتشغيل صوت قصير عند النجاح
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
        st.warning("⚠️ ملف الصوت غير موجود، الرجاء إضافته للمشروع.")

# سجل الذاكرة
if "memory_log" not in st.session_state:
    st.session_state.memory_log = []

# العنوان
st.title("🌟 Product Quality Evaluator 🌟")
st.write("🔍 ابحث عن منتج وقيم جودته بالذكاء الاصطناعي")

# إدخال المنتج
product_name = st.text_input("🛒 أدخل اسم المنتج")
if st.button("بحث وتقييم"):
    if product_name.strip():
        # تحليل النص بالذكاء الاصطناعي
        sentiment_analyzer = pipeline("sentiment-analysis")
        result = sentiment_analyzer(product_name)[0]
        label = result['label']
        score = result['score']

        # رد كتابي ذكي
        if label == "POSITIVE":
            response = f"✅ المنتج {product_name} يبدو عالي الجودة بنسبة {score:.2f}. أنصح باعتماده."
            st.success(response)
            play_sound("success.wav")
        elif label == "NEGATIVE":
            response = f"⚠️ المنتج {product_name} حصل على تقييم سلبي بنسبة {score:.2f}. ربما تحتاج إلى بديل."
            st.warning(response)
            play_sound("alert.wav")
        else:
            response = f"ℹ️ المنتج {product_name} تقييمه محايد بنسبة {score:.2f}. يمكنك المتابعة بحذر."
            st.info(response)
            play_sound("neutral.wav")

        # تسجيل في سجل الذاكرة
        st.session_state.memory_log.append(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - تقييم المنتج: {product_name} → {response}"
        )
    else:
        st.error("⚠️ الرجاء إدخال اسم المنتج أولًا.")

# سجل الذاكرة في الشريط الجانبي
st.sidebar.subheader("📝 سجل التقييمات")
if st.session_state.memory_log:
    for entry in st.session_state.memory_log:
        st.sidebar.write(entry)
else:
    st.sidebar.write("لا توجد تقييمات بعد...")
