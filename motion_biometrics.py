import math

class MotionBiometrics:
    def __init__(self, movement_threshold=0.85):
        self.threshold = movement_threshold

    def calculate_movement_signature(self, accel_data):
        """تحويل بيانات الحساسات (X, Y, Z) إلى بصمة حركة فريدة"""
        if not accel_data: return 0
        mag = [math.sqrt(x**2 + y**2 + z**2) for x, y, z in accel_data]
        return sum(mag) / len(mag)

    def verify_user_gait(self, live_data, stored_signature):
        """مقارنة حركة المستخدم الحالية بالنمط المخزن"""
        current_sig = self.calculate_movement_signature(live_data)
        if stored_signature == 0: return False
        similarity = 1 - abs(current_sig - stored_signature) / stored_signature
        return similarity >= self.threshold
