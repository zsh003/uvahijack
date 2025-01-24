import unittest
from app.services.hijack_service import perform_hijack

# 运行测试：python -m unittest tests/test_hijack_service.py
class TestHijackService(unittest.TestCase):
    def test_perform_hijack(self):
        result = perform_hijack("192.168.1.1", 8080)
        self.assertEqual(result, "Hijack performed on 192.168.1.1:8080")

if __name__ == '__main__':
    unittest.main()