import streamlit as st
from star_security_core import FlashDealStarSecurity

# إعدادات الصفحة
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟")

# استدعاء النظام الأمني
security = FlashDealStarSecurity()

# واجهة المستخدم
st.title("🌟 My FlashDeal Star")
st.subheader("Talk. Pay. Done.")

st.divider()

# منطقة تجربة فلترة الرسائل (الميزة الجديدة)
st.write("### 🛡️ Security Scanner")
user_input = st.text_area("أدخل الرسالة أو الرابط للفحص:", placeholder="مثال: Attention la vidéo Macron...")

if st.button("فحص الأمان"):
    if user_input:
        is_safe, message = security.validate_content(user_input)
        if is_safe:
            st.success(f"✅ {message}")
            # توليد توكن في حالة الأمان
            token = security.generate_secure_token(user_input[:10])
            st.info(f"Generated Token: {token}")
        else:
            st.error(f"⚠️ {message}")
    else:
        st.warning("الرجاء إدخال نص للفحص")

st.divider()
st.caption("FlashDeal High-Quality Parallel Project v2.0")
