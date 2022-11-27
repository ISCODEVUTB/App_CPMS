import unittest

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci_1(self):
    self.assertEqual(fibonacci(1), 1)
