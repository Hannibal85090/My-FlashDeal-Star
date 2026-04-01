from star_security_core import FlashDealSecurity
from motion_biometrics import MotionBiometrics

class StarSuperHandshake:
    def __init__(self):
        self.security = FlashDealSecurity()
        self.motion = MotionBiometrics()

    def authorize_access(self, user_id, bio_sample, movement_data, stored_pattern):
        """بروتوكول المصافحة المتعدد: توكن + حركة + بصمة"""
        # 1. إنشاء توكن جديد
        tx_token = self.security.generate_mutual_token(user_id)
        
        # 2. التحقق من نمط الحركة (أمان استباقي)
        if not self.motion.verify_user_gait(movement_data, stored_pattern):
            return {"status": "denied", "reason": "نمط الحركة غير متطابق"}

        # 3. التحقق الحيوي النهائي
        if self.security.verify_biometric_logic(bio_sample, "valid_pattern"):
            self.security.start_secure_transaction(user_id, tx_token)
            return {"status": "authorized", "token": tx_token}
        
        return {"status": "denied", "reason": "فشل التحقق الحيوي"}
