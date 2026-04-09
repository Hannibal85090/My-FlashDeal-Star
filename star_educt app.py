import streamlit as st
import random
from streamlit_mic_recorder import mic_recorder

# تفعيل حالة الجلسة لتخزين التوكنز والمسألة الحالية
if 'tokens' not in st.session_state:
    st.session_state.tokens = 0
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'correct_answer' not in st.session_state:
    st.session_state.correct_answer = None

# نافيجا - الوكيل التربوي
class NavigaVoiceAgent:
    def __init__(self):
        pass

    def get_new_problem(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        return num1 + num2, f"كم حاصل جمع {num1} و {num2}؟"

agent = NavigaVoiceAgent()

# تصميم الواجهة - مطابق للقطة الشاشة ولكن مع زر الميكروفون
st.title("NAVIGAÅ: الملاح التربوي الذكي")
st.subheader("Talk. Learn. Done.")

# عرض رصيد التوكنز في الشريط الجانبي (مطابق للصورة)
st.sidebar.markdown(f"**رصيد التوكنز:** {st.session_state.tokens}")

# إذا لم يكن هناك مسألة حالية، فأنشئ واحدة
if st.session_state.current_problem is None:
    ans, prob = agent.get_new_problem()
    st.session_state.correct_answer = ans
    st.session_state.current_problem = prob

# عرض التحدي الحالي
st.write(f"### {st.session_state.current_problem}")

# 🎙️ دمج الميكروفون للتفاعل الصوتي بدلاً من الإدخال الرقمي
st.write("اضغط على الميكروفون لقول إجابتك:")
audio = mic_recorder(
    start_prompt="🎤 ابدأ التحدث",
    stop_prompt="⏹️ توقف"،
    key='recorder',
    use_container_width=True
)

# معالجة الرد الصوتي
if audio and 'text' in audio and audio['text']:
    spoken_answer = audio['text'].strip()
    st.write(f"لقد سمعت: `{spoken_answer}`")

    # محاولة تحويل النص المسموع إلى رقم (إذا كان الرد رقماً)
    try:
        user_answer = int(spoken_answer)
        if user_answer == st.session_state.correct_answer:
            st.session_state.tokens += 10
            st.balloons()
            st.success("✅ إجابة صحيحة! حصلت على 10 توكنز.")
            # توليد مسألة جديدة للدورة القادمة
            ans, prob = agent.get_new_problem()
            st.session_state.correct_answer = ans
            st.session_state.current_problem = prob
        else:
            st.warning("💡 إجابة خاطئة. حاول مرة أخرى.")
    except ValueError:
        st.warning("⚠️ يرجى محاولة قول الإجابة كرقم، مثلاً: 'ثمانية'.")

