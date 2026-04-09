import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder

# إعدادات الصفحة
st.set_page_config(page_title="NAVIGAÅ Edu", page_icon="⭐")

# إدارة حالة الجلسة (Session State) لضمان استمرارية البيانات
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'correct_answer' not in st.session_state:
    st.session_state.correct_answer = None

class NavigaAgent:
    def __init__(self):
        pass

    def generate_math_problem(self):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        return n1 + n2, f"كم حاصل جمع {n1} و {n2}؟"

agent = NavigaAgent()

# واجهة المستخدم
st.title("NAVIGAÅ: الملاح التربوي الذكي")
st.markdown("### Talk. Learn. Done.")
st.divider()

# عرض الرصيد في الجانب
st.sidebar.metric("رصيد التوكنز 🪙", st.session_state.tokens)

# منطق توليد المسائل
if st.session_state.current_problem is None:
    ans, prob = agent.generate_math_problem()
    st.session_state.correct_answer = ans
    st.session_state.current_problem = prob

st.write(f"## {st.session_state.current_problem}")

# 🎙️ ميكروفون التفاعل الصوتي (تم تصحيح الفواصل هنا)
st.write("اضغط للتحدث بالإجابة:")
audio_data = mic_recorder(
    start_prompt="🎤 ابدأ التحدث الآن",
    stop_prompt="⏹️ توقف",
    key='naviga_mic'
)

# معالجة المدخلات الصوتية
if audio_data and audio_data.get('text'):
    spoken_text = audio_data['text'].strip()
    st.info(f"سمعتك تقول: {spoken_text}")
    
    try:
        # محاولة استخراج الرقم من النص
        user_val = int(''.join(filter(str.isdigit, spoken_text)))
        
        if user_val == st.session_state.correct_answer:
            st.success("✅ رائع! إجابة صحيحة.")
            st.balloons()
            st.session_state.tokens += 10
            # تحديث المسألة للمرة القادمة
            ans, prob = agent.generate_math_problem()
            st.session_state.correct_answer = ans
            st.session_state.current_problem = prob
            if st.button("المسألة التالية"):
                st.rerun()
        else:
            st.error(f"❌ للأسف، {user_val} ليست الإجابة المطلوبة. حاول مجدداً!")
            
    except ValueError:
        st.warning("⚠️ من فضلك قل الرقم بوضوح ليتمكن NAVIGAÅ من فهمك.")

st.divider()
st.caption("نظام NAVIGAÅ يعمل بطاقة FlashDeal الذكية")

