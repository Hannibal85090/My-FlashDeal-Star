import streamlit as st
import sys
import os

# --- تأمين المسارات البرمجية ---
# هذا السطر يضمن أن البرنامج يرى الملفات الجانبية في GitHub
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# محاولة استيراد المنطق الأمني مع معالجة الأخطاء
try:
    from star_handshake_logic import StarSuperHandshake
except ImportError:
    st.error("⚠️ خطأ في العثور على ملفات النظام الأساسية. تأكد من وجود star_handshake_logic.py")

# --- إعداد واجهة FlashDeal Star ---
st.set_page_config(
    page_title="FlashDeal Star Core",
    page_icon="🌟",
    layout="wide"
)

# العنوان والهوية البصرية
st.title("🌟 نظام FlashDeal Star الموازي")
st.markdown(f"### **Slogan:** Talk. Pay. Done.")
st.write("---")

# --- استدعاء المحرك الأمني ---
if 'system' not in st.session_state:
    try:
        st.session_state.system = StarSuperHandshake()
    except Exception as e:
        st.error(f"فشل تشغيل المحرك الأمني: {e}")

# --- تصميم الواجهة التفاعلية ---
st.subheader("(Handshake) بروتوكول المصافحة والأمان")

col1, col2 = st.columns([2, 1])

with col1:
    st.info("قم بمحاكاة عملية التوثيق البيومتري والحركي للمعاملة")
    
    if st.button("🚀 بدء فحص الهوية والحركة"):
        # بيانات المحاكاة (يمكن تطويرها لاحقاً لإدخال حي)
        user_id = "Ali_Arfaoui"
        
        # تنفيذ عملية التوثيق عبر النظام الموازي عالي الجودة
        try:
            result = st.session_state.system.authorize_access(
                user_id=user_id,
                bio_sample="valid_pattern",
                movement_data=[[0,0,9.8], [0.1,0,9.7]], # محاكاة حساس التسارع
                stored_pattern=9.75
            )
            
            if result.get('status') == 'authorized':
                st.success(f"✅ تم التحقق من الهوية ونمط الحركة لـ {user_id}")
                st.markdown(f"**التوكن المولد:** `{result.get('token')[:20]}...`")
                st.balloons()
            else:
                st.error(f"❌ مرفوض: {result.get('reason')}")
        except Exception as e:
            st.warning("حدث خطأ أثناء المعالجة، تأكد من تحديث ملفات star_security_core")

with col2:
    st.write("**الحالة التقنية الحالية:**")
    status_data = {
        "Secure_Core": "Active ✅",
        "Motion_Engine": "Ready ⚡",
        "Token_Service": "Online 🔐",
        "AI_Agent": "Standby 🤖"
    }
    st.json(status_data)

# تذييل الصفحة
st.write("---")
st.caption("FlashDeal Star - High Quality Parallel Project v1.0")
