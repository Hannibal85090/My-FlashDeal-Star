import streamlit as st
from flashdeal_app.security_engine import FlashDealSecurity

st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐")

st.title("⭐ My FlashDeal Star")
st.subheader("Talk. Pay. Done.")

# تفعيل النظام الأمني الراهن
security = FlashDealSecurity()

if st.button("تفعيل نظام التوكن الآمن"):
    if security.verify_token("FLASH_2026"):
        st.success("تم الاتصال بالنجاح! النظام جاهز للعمليات.")
    else:
        st.error("خطأ في التوكن.")

st.info("نظام حماية حركة الجسم (Body Movement) قيد التطوير في المشروع الموازي.")
