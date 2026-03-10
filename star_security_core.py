import re
import hashlib

class FlashDealStarSecurity:
    """
    النواة الأمنية لمشروع My FlashDeal Star (النسخة عالية الجودة)
    تشمل: فلترة المحتوى، إدارة التوكن، والتحقق البيومتري.
    """
    def __init__(self):
        self.hoax_keywords = ["virus", "format", "urgent", "broadcast", "macron", "con"]
        self.version = "2.0.0"

    # --- 1. محرك فلترة المحتوى (الميزة الجديدة) ---
    def validate_content(self, message):
        """يفحص الرسائل والروابط لمنع الاحتيال"""
        score = 0
        content_lower = message.lower()
        
        # فحص الكلمات المشبوهة
        for word in self.hoax_keywords:
            if word in content_lower:
                score += 1
        
        # فحص الروابط (Regex)
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        if re.search(url_pattern, content_lower):
            score += 2

        if score >= 3:
            return False, "BLOCK: Malicious content or Hoax detected."
        return True, "SAFE"

    # --- 2. إدارة التوكن (Token Aspect) ---
    def generate_secure_token(self, data):
        """توليد توكن فريد لكل عملية لضمان الأمان"""
        raw_token = f"{data}{self.version}"
        return hashlib.sha256(raw_token.encode()).hexdigest()

    # --- 3. التحقق البيومتري (مستقبلي) ---
    def verify_biometrics(self, bio_type):
        """محاكي للتحقق عبر البصمة أو الوجه أو حركة الجسم"""
        # سيتم ربطها بالحساسات لاحقاً في Star Device
        return f"Verifying {bio_type}... Access Granted."

# --- منطقة التشغيل التجريبي ---
if __name__ == "__main__":
    security = FlashDealStarSecurity()
    
    # تجربة الفلترة على الرسالة المشبوهة
    msg = "Attention, la vidéo Macron est un virus qui formate votre mobile."
    is_safe, status = security.validate_content(msg)
    
    # في حالة الأمان فقط، يتم إصدار التوكن
    if is_safe:
        token = security.generate_secure_token("Transaction_001")
        # print(f"Status: {status} | Token: {token}")
    else:
        # print(f"Security Alert: {status}")
        pass
