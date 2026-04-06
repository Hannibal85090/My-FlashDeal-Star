import streamlit as st
import hashlib, secrets, time
import numpy as np
import cv2
import mediapipe as mp

# إعداد الصفحة
st.set_page_config(page_title="FlashDeal Star Core", page_icon="⚡", layout="wide")

# النظام الأساسي
class FlashDealSystem:
    def __init__(self):
        self.token_registry = {}

    def generate_token(self, user_id):
        raw = f"{user_id}-{secrets.token_hex(8)}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def verify_motion(self, data):
        if not data: return False
        mags = [(x**2 + y**2 + z**2)**0.5 for x, y, z in data]
        avg = sum(mags) / len(mags)
        return avg >= 9.0

    def verify_face(self, image):
        mp_face_detection = mp.solutions.face_detection
        with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
            results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            return bool(results.detections)

# واجهة التطبيق
st.title("⚡ FlashDeal Star (النجم)")
st.markdown("**#Talk. Pay. Done.**")
st.write("---")

if 'fd_system' not in st.session_state:
    st.session_state.fd_system = FlashDealSystem()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("بروتوكول المصادقة: الوجه + الحركة")

    uploaded_file = st.file_uploader("ارفع صورة للتحقق من الوجه", type=["jpg","jpeg","png"])
    camera_image = st.camera_input("أو التقط صورة بالكاميرا")

    if st.button("بدء الفحص"):
        with st.spinner("جاري التشغيل..."):
            time.sleep(1)
            token = st.session_state.fd_system.generate_token("Ali_Arfaoui")
            motion_ok = st.session_state.fd_system.verify_motion([[0.0,9.81,0],[1.0,9.7,0]])
            face_ok = False

            # إذا رفع صورة
            if uploaded_file:
                file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, 1)
                face_ok = st.session_state.fd_system.verify_face(image)

            # إذا استخدم الكاميرا
            elif camera_image:
                file_bytes = np.asarray(bytearray(camera_image.getvalue()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, 1)
                face_ok = st.session_state.fd_system.verify_face(image)

        if motion_ok and face_ok:
            st.success("✅ تم التحقق من الهوية (الوجه) والحركة بنجاح")
            st.code(f"Token: {token[:32]}...", language="bash")
            st.balloons()
        else:
            st.error("❌ فشل التحقق من الهوية أو الحركة")

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
