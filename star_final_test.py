import unittest
from star_handshake_logic import StarSuperHandshake

class TestFlashDealStar(unittest.TestCase):
    def setUp(self):
        self.system = StarSuperHandshake()

    def test_full_security_flow(self):
        # تجربة بيانات صحيحة (مشية طبيعية وبصمة مطابقة)
        result = self.system.authorize_access("Ali_Arfaoui", "valid_pattern", [[0,0,9.8], [0.1,0,9.7]], 9.75)
        self.assertEqual(result['status'], 'authorized')
        print("✅ تم اجتياز اختبار المصافحة والأمان بنجاح.")

if __name__ == '__main__':
    unittest.main()
