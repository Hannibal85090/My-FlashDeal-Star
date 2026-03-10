import streamlit as st

# -------------------------------
# إعدادات عامة
# -------------------------------
st.set_page_config(page_title="My FlashDeal Star", layout="wide")

# -------------------------------
# الترجمات
# -------------------------------
translations = {
    "en": {
        "title": "🌟 FlashDeal Star",
        "welcome": "Welcome to FlashDeal Star",
        "tagline": "Talk. Pay. Done.",
        "security": "Security Center",
        "log": "Transparency Log",
        "deal": "Deal Execution",
        "agent": "Smart Agent",
        "help": "Help Center",
        "rate": "Rate Product",
        "follow": "Follow-up",
        "caption": "Wireless Headphones",
        "price": "Price: $59.99",
        "voice": "🎤 Voice",
        "gesture": "✋ Gesture",
        "writing": "✍️ Writing",
        "rating_label": "⭐ Choose your rating"
    },
    "ar": {
        "title": "🌟 نجم FlashDeal",
        "welcome": "مرحبا بك في FlashDeal Star",
        "tagline": "تحدث. ادفع. تم.",
        "security": "مركز الحماية",
        "log": "سجل الشفافية",
        "deal": "تنفيذ الصفقة",
        "agent": "الوكيل الذكي",
        "help": "مركز المساعدة",
        "rate": "قيم المنتج",
        "follow": "المتابعة",
        "caption": "سماعات لاسلكية",
        "price": "السعر: 59.99 دينار",
        "voice": "🎤 صوت",
        "gesture": "✋ إيماءة",
        "writing": "✍️ كتابة",
        "rating_label": "⭐ اختر تقييمك"
    },
    "fr": {
        "title": "🌟 FlashDeal Star",
        "welcome": "Bienvenue à FlashDeal Star",
        "tagline": "Parlez. Payez. Terminé.",
        "security": "Centre de sécurité",
        "log": "Journal de transparence",
        "deal": "Exécution de l'offre",
        "agent": "Agent intelligent",
        "help": "Centre d'aide",
        "rate": "Évaluer le produit",
        "follow": "Suivi",
        "caption": "Casque sans fil",
        "price": "Prix : 59,99 €",
        "voice": "🎤 Voix",
        "gesture": "✋ Geste",
        "writing": "✍️ Écriture",
        "rating_label": "⭐ Choisissez votre note"
    }
}

# -------------------------------
# اختيار اللغة
# -------------------------------
lang = st.sidebar.selectbox("🌐 Language / اللغة / Langue", ["en", "ar", "fr"])
texts = translations[lang]

# -------------------------------
# العنوان والترحيب
# -------------------------------
st.title(texts["title"])
st.write(texts["welcome"])
st.write(texts["tagline"])

# -------------------------------
# صورة المنتج مع السعر
# -------------------------------
st.image("assets/images/headphones_small.png", caption=texts["caption"], use_column_width=True)
st.subheader(texts["price"])

# -------------------------------
# خيارات التفاعل (صوت، إيماءة، كتابة)
# -------------------------------
st.markdown("### Interaction Options")
interaction = st.radio("Choose interaction mode:", [texts["voice"], texts["gesture"], texts["writing"]])
st.info(f"You selected: {interaction}")

# -------------------------------
# تقييم المنتج
# -------------------------------
st.markdown("### " + texts["rate"])
rating = st.slider(texts["rating_label"], 1, 5, 3)
st.success(f"{texts['rate']}: {rating} ⭐")

# -------------------------------
# الأقسام الرئيسية
# -------------------------------
st.header(texts["security"])
st.write("🔒 " + texts["security"] + " content goes here...")

st.header(texts["log"])
st.write("📑 " + texts["log"] + " content goes here...")

st.header(texts["deal"])
st.write("⚡ " + texts["deal"] + " content goes here...")

st.header(texts["agent"])
st.write("🤖 " + texts["agent"] + " content goes here...")

st.header(texts["help"])
st.write("❓ " + texts["help"] + " content goes here...")

st.header(texts["follow"])
st.write("📌 " + texts["follow"] + " content goes here...")

# -------------------------------
# إشعار نجاح
# -------------------------------
st.success("✅ جميع الخصائص مضبوطة: العنوان، الصورة، السعر، الأقسام، اللغات، الترجمة، خيارات التفاعل، التقييم.")
