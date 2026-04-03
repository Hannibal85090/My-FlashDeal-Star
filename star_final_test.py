import streamlit as st
import cv2
import os
import sqlite3
import secrets
from deepface import DeepFace
import PIL.Image
import numpy as np

# --- 1. الإعدادات اللوجستية (Zero-Error Setup) ---
def initial_setup():
    if not os.path.exists("faces"):
        os.makedirs("faces")
    conn = sqlite3.connect("flashdeal_star_final.db", check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (name TEXT, image_path TEXT, secret_code TEXT, token TEXT)''')
    conn.commit()
    return conn, c

conn, c = initial_setup()

# --- 2. واجهة المستخدم (Talk. Pay. Done.) ---
st.set_page_config(page_title="FlashDeal Star Final Test", page_icon="⭐", layout="centered")

st.title("⭐ My FlashDeal Star")
st.markdown("### `Talk. Pay. Done.`")
st.info("النسخة النهائية للاختبار والتدقيق البرمجي")

menu = ["التحقق والدفع (Login)", "تسجيل مستخدم (Register)"]
choice = st.sidebar.selectbox("القائمة البرمجية", menu)

# --- 3. وظيفة التسجيل (التثبت من البيانات) ---
if choice == "تسجيل مستخدم (Register)":
    st.subheader("📸 تسجيل الهوية البيومترية")
    with st.form("registration_form"):
        name = st.text_input("الاسم الكامل")
        s_code = st.text_input("الرمز السري (Secret Code)", type="password")
        img_file = st.camera_input("التقط صورة التسجيل")
        submit = st.form_submit_button("اعتماد التسجيل النهائي")

        if submit and img_file and name and s_code:
            path = f"faces/{name.replace(' ', '_')}.jpg"
            # حفظ الصورة بدقة
            img = PIL.Image.open(img_file)
            img.save(path)
            
            c.execute("INSERT INTO users (name, image_path, secret_code) VALUES (?, ?, ?)", 
                      (name, path, s_code))
            conn.commit()
            st.success(f"تم تسجيل {name} بنجاح في قاعدة بيانات FlashDeal.")

# --- 4. وظيفة التحقق والدفع (المنطق الموازي) ---
elif choice == "التحقق والدفع (Login)":
    st.subheader("🔐 بوابة العبور الآمن")
    img_file = st.camera_input("مسح الوجه للتحقق")

    if img_file:
        # حفظ مؤقت للمقارنة
        temp_path = "temp_test.jpg"
        img = PIL.Image.open(img_file)
        img.save(temp_path)
        
        found_user = None
        
        with st.spinner("جاري التمحيص والمطابقة..."):
            c.execute("SELECT name, image_path, secret_code FROM users")
            users = c.fetchall()
            
            for u_name, u_path, u_code in users:
                try:
                    # التدقيق باستخدام VGG-Face لسرعة الاستجابة
                    check = DeepFace.verify(img1_path=temp_path, img2_path=u_path, 
                                            model_name='VGG-Face', enforce_detection=True)
                    if check["verified"]:
                        found_user = u_name
                        break
                except Exception as e:
                    continue

        if found_user:
            # توليد التوكن المتبادل (Mutual Token) كما اتفقنا
            m_token = secrets.token_hex(12).upper()
            st.session_state['current_token'] = m_token
            
            st.success(f"تم التحقق بنجاح! مرحباً {found_user}")
            st.markdown(f"---")
            st.write(f"🎫 **Mutual Token:** `{m_token}`")
            
            if st.button("تأفيذ العملية: Talk. Pay. Done."):
                st.balloons()
                st.success("تمت المعاملة بأمان عبر My FlashDeal Star")
        else:
            st.error("فشل التحقق البصري.")
            # خيار الرمز السري كبديل جودة
            input_code = st.text_input("أدخل الرمز السري للاستمرارية", type="password")
            if st.button("دخول يدوي"):
                c.execute("SELECT name FROM users WHERE secret_code=?", (input_code,))
                res = c.fetchone()
                if res:
                    st.success(f"تم الدخول بالرمز السري! مرحباً {res[0]}")
                else:
                    st.error("الرمز غير صحيح.")

# --- 5. إغلاق الاتصال ---
# conn.close() # يفضل تركه مفتوحاً أثناء تشغيل Streamlit
