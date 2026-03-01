import hashlib
import time
import secrets

class FlashDealTokenEngine:
    def __init__(self):
        # معايير جودة عالية: استخدام أرقام سرية مشفرة
        self.secret_salt = secrets.token_hex(16)

    def generate_mutual_token(self, user_id, star_device_id):
        """
        إنشاء 'Mutual Token' يربط بين المستخدم وجهاز 'My FlashDeal Star'
        """
        timestamp = str(int(time.time() // 30))  # التوكين يتغير كل 30 ثانية لأمان أعلى
        raw_data = f"{user_id}:{star_device_id}:{timestamp}:{self.secret_salt}"
        return hashlib.sha256(raw_data.encode()).hexdigest()

    def verify_token(self, provided_token, user_id, star_device_id):
        # التحقق من مطابقة التوكين لضمان تنفيذ (Talk. Pay. Done.)
        expected_token = self.generate_mutual_token(user_id, star_device_id)
        return secrets.compare_digest(provided_token, expected_token)
