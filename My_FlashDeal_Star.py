import streamlit as st
import time

# --- إعداد الوقت ---
current_time = time.strftime("%d/%m/%Y - %H:%M:%S")

# اختيار اللغة
lang = st.selectbox("اختر اللغة / Choose Language", ["English", "العربية", "Français"])

# ترجمة الشعار حسب اللغة
motto = {
    "English": "TALK , PAY , DONE .",
    "العربية": "تكلم ، ادفع ، تم .",
    "Français": "PARLE , PAIE , TERMINÉ ."
}[lang]

# العنوان
st.markdown("<h1 style='text-align:center;color:#000000;text-shadow:0 0 10px #444444;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)

# الشعار
st.markdown(f"<p style='text-align:center;color:gold;font-size:22px;'>{motto}</p>", unsafe_allow_html=True)

# النجمة الكبيرة
st.markdown('<div style="text-align:center;font-size:60px;color:gold;">★</div>', unsafe_allow_html=True)

# التوقيت
st.markdown(f"<p style='text-align:center;color:#4facfe;'>🕒 Current Time: {current_time}</p>", unsafe_allow_html=True)

# --- الميزات الإضافية ---
st.subheader("🔐 الشفافية والأمان")
st.info("كل العمليات مسجلة وآمنة عبر التوكنات المشفرة.")

st.subheader("🤝 الوكيل الذكي")
st.button("تواصل مع الوكيل لإبرام صفقة")

st.subheader("📸 الكاميرا")
st.camera_input("التقط صورة للتحقق أو المشاركة")

st.subheader("💎 التوكن المتبادل")
tokens = st.number_input("أدخل عدد التوكنات للتبادل", min_value=0)
if st.button("نفّذ التبادل"):
    st.success(f"تم تبادل {tokens} توكن بنجاح!")

st.subheader("🏠 تأمين السيارة والمنزل")
st.checkbox("تأمين السيارة")
st.checkbox("تأمين المنزل")
