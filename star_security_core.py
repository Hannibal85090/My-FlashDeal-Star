import hashlib
import secrets
import time

class FlashDealSecurity:
    def __init__(self):
        self.session_active = False
        self.token_registry = {}

    def generate_mutual_token(self, user_id):
        """إنشاء توكن فريد (Mutual Token) لضمان أمان المعاملة"""
        raw_token = f"{user_id}-{secrets.token_hex(16)}-{time.time()}"
        secure_token = hashlib.sha256(raw_token.encode()).hexdigest()
        self.token_registry[user_id] = {"token": secure_token, "timestamp": time.time()}
        return secure_token

    def verify_biometric_logic(self, biometric_data, expected_pattern):
        """التحقق الحيوي (بصمة/وجه) مع دعم تجاوز الخطأ"""
        try:
            return biometric_data == expected_pattern
        except Exception:
            return False

    def start_secure_transaction(self, user_id, auth_token):
        """تفعيل الجلسة الآمنة فقط في حال تطابق التوكن"""
        if user_id in self.token_registry and self.token_registry[user_id]["token"] == auth_token:
            self.session_active = True
            return True
        return False
