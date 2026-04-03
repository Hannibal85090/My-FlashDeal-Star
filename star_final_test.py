import streamlit as st
import time
import cv2
import face_recognition
import numpy as np

st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

# --- سجل الأحداث بصيغة JSON + حفظ خارجي ---
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action, status="OK"):
    timestamp = time.strftime("%d/%m/%Y - %H:%M:%S")
    log_entry = {"time": timestamp, "action": action, "status": status}
    st.session_state.history.append(log_entry)

    # حفظ في ملف خارجي
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] - {action} ({status})\n")

# --- بروتوكولات الأمان ---
def trigger_emergency_protocol():
    try:
        st.error("🚨 SOS: Emergency Protocol Activated!")
        add_to_memory("SOS Triggered - Alerts sent to Master Alpha Hub")
        with st.status("Verifying Security Links..."):
            time.sleep(1)
            st.warning("All Smart Links: IMMOBILIZED 🔒")
    except Exception as e:
        st.error(f"Emergency protocol failed: {e}")
        add_to_memory("SOS Error", status="FAIL")

# --- التعرف على الوجه ---
def handle_face(img_data):
    try:
        bytes_data = img_data.getvalue()
        nparr = np.frombuffer(bytes_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_frame)

        if encodings:
            st.success("Identity verified with AI! ✅")
            add_to_memory("Face Verified")
        else:
            st.error("No face detected ❌")
            add_to_memory("Face verification failed", status="FAIL")
    except Exception as e:
        st.error(f"Face recognition error: {e}")
        add_to_memory("Face recognition error", status="FAIL")

# --- واجهة المستخدم ---
st.title("🌟 My FlashDeal Star 🌟")

# اختيار مستوى الوصول
acc = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])

# زر الطوارئ مرتبط بالصلاحيات
if acc == "Master Alpha 🔓":
    if st.button("Activate SOS Mode 🔔"):
        trigger_emergency_protocol()
else:
    st.warning("SOS Mode requires Master Alpha access")

# سجل الأحداث
st.subheader("📜 Unified Memory Log")
if not st.session_state.history:
    st.write("No active logs.")
else:
    for item in reversed(st.session_state.history):
        st.write(f"[{item['time']}] - {item['action']} ({item['status']})")

# التعرف على الوجه
st.subheader("👤 Biometric Face Recognition")
try:
    img_data = st.camera_input("Activate Camera for Face Recognition")
    if img_data:
        handle_face(img_data)
except Exception as e:
    st.error(f"Camera error: {e}")
    add_to_memory("Camera error", status="FAIL")
