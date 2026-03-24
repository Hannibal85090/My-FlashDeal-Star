# --- العنوان الجديد مع التاريخ والتوقيت ---
current_time = time.strftime("%d/%m/%Y - %H:%M:%S")
st.markdown("<h1 style='text-align:center;color:#000000;text-shadow:0 0 10px #444444;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:gold;font-size:24px;'>{t['motto']}</p>", unsafe_allow_html=True)
st.markdown('<div class="star">★</div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;color:#4facfe;'>🕒 Current Time: {current_time}</p>", unsafe_allow_html=True)
