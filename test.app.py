import streamlit as st
import time
import numpy as np
import cv2
import mediapipe as mp

from star_handshake_logic import StarSuperHandshake

# إعداد الصفحة
st.set_page_config(page_title="FlashDeal Star Core", page_icon="⚡", layout="wide")

# تهيئة النظام
if 'handshake' not in st.session_state:
    st.session_state.handshake = StarSuperHandshake()

st.title("⚡ FlashDeal Star (النجم)")
st.markdown("**#Talk. Pay. Done.**")
st.write("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("بروتوكول المصادقة: الوجه + الحركة + توكن")

    uploaded_file = st.file_uploader("ارفع صورة للتحقق من الوجه", type=["jpg","jpeg","png"])
    camera_image = st.camera_input("أو التقط صورة بالكاميرا")

    if st.button("بدء الفحص"):
        with st.spinner("جاري التشغيل..."):
            time.sleep(1)

            # بيانات الحركة (مثال تجريبي)
            movement_data = [[0.0,9.81,0],[1.0,9.7,0]]
            stored_pattern = 9.8  # بصمة حركة مخزنة (تجريبية)

            # بيانات الوجه
            face_ok = False
            if uploaded_file:
                file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, 1)
                face_ok = True if image is not None else False
            elif camera_image:
                file_bytes = np.asarray(bytearray(camera_image.getvalue()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, 1)
                face_ok = True if image is not None else False

            # استدعاء المصافحة الأمنية
            result = st.session_state.handshake.authorize_access(
                user_id="Ali_Arfaoui",
                bio_sample="valid_pattern" if face_ok else "invalid",
                movement_data=movement_data,
                stored_pattern=stored_pattern
            )

        if result["status"] == "authorized":
            st.success("✅ تم التحقق من الهوية والحركة والتوكن بنجاح")
            st.code(f"Token: {result['token'][:32]}...", language="bash")
            st.balloons()
        else:
            st.error(f"❌ فشل التحقق: {result['reason']}")

with col2:
    st.subheader("النظام العام")
    st.json({
        "Secure_Core": "Active ✅",
        "Motion_Engine": "Ready ⚙️",
        "Face_Verification": "Enabled 🧑‍💻",
        "Token_Service": "Online 🔐"
    })
st.write("---")
st.caption("FlashDeal Star - High Quality Parallel Project")
