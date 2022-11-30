from unittest import TestCase
import app



class TestSuma(TestCase):
    def test_suma(self):
        self.assertEqual(app.suma(2,2), 4)
