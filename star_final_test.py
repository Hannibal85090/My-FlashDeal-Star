import streamlit as st
import cv2
import sqlite3
import numpy as np
from deepface import DeepFace
from firebase_admin import credentials, initialize_app, storage

st.title("🔐 Face Recognition & Motion Login System")

# --------------------------
# 🔗 إعداد Firebase للتخزين السحابي
# --------------------------
cred = credentials.Certificate("firebase_key.json")  # ملف مفتاح الخدمة
initialize_app(cred, {"storageBucket": "your-bucket-name.appspot.com"})
bucket = storage.bucket()

# الاتصال بقاعدة بيانات SQLite (يمكن استبدالها بـ سحابية مثل Supabase)
conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    image_url TEXT NOT NULL,
    embedding BLOB NOT NULL
)''')
conn.commit()

menu = ["Register", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

# --------------------------
# 🧾 تسجيل مستخدم جديد
# --------------------------
if choice == "Register":
    st.subheader("Register New Face")
    name = st.text_input("Enter your name")
    image_file = st.file_uploader("Upload your face image", type=["jpg", "png"])

    if st.button("Save"):
        if image_file and name:
            # رفع الصورة للسحابة
            blob = bucket.blob(f"faces/{name}.jpg")
            blob.upload_from_file(image_file, content_type="image/jpeg")
            image_url = blob.public_url

            # استخراج embedding
            with open("temp.jpg", "wb") as f:
                f.write(image_file.getbuffer())
            embedding = DeepFace.represent("temp.jpg", model_name="Facenet", enforce_detection=False)[0]["embedding"]
            embedding_bytes = np.array(embedding).tobytes()

            c.execute("INSERT INTO users (name, image_url, embedding) VALUES (?, ?, ?)", (name, image_url, embedding_bytes))
            conn.commit()
            st.success("User registered successfully!")

# --------------------------
# 🔓 تسجيل الدخول بالوجه + كشف الحركة
# --------------------------
elif choice == "Login":
    st.subheader("Login with Face & Motion Detection")

    run = st.checkbox("Start Camera")
    camera = cv2.VideoCapture(0)
    FRAME_WINDOW = st.image([])

    prev_frame = None
    while run:
        ret, frame = camera.read()
        if not ret:
            st.error("Camera error")
            break

        FRAME_WINDOW.image(frame, channels="BGR")

        # كشف الحركة
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if prev_frame is None:
            prev_frame = gray
            continue

        diff = cv2.absdiff(prev_frame, gray)
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        motion_level = np.sum(thresh) / 255

        if motion_level > 5000:  # عتبة للحركة
            st.warning("Motion detected!")

        prev_frame = gray

        # حفظ صورة مؤقتة
        cv2.imwrite("temp.jpg", frame)

        # التحقق من الوجه
        c.execute("SELECT name, embedding FROM users")
        users = c.fetchall()

        temp_embedding = DeepFace.represent("temp.jpg", model_name="Facenet", enforce_detection=False)[0]["embedding"]
        temp_embedding = np.array(temp_embedding)

        for user in users:
            stored_embedding = np.frombuffer(user[1], dtype=np.float64)
            distance = np.linalg.norm(temp_embedding - stored_embedding)
            if distance < 0.7:
                st.success(f"Welcome {user[0]} 🎉")
                run = False
                break

    camera.release()
