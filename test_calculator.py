import unittest
import subprocess

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = subprocess.run(['python', 'first.py', 'add', '2', '3'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Result: 5.0")

    def test_subtract(self):
        result = subprocess.run(['python', 'first.py', 'subtract', '5', '3'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Result: 2.0")

    def test_multiply(self):
        result = subprocess.run(['python', 'first.py', 'multiply', '2', '3'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Result: 6.0")

    def test_divide(self):
        result = subprocess.run(['python', 'first.py', 'divide', '6', '3'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Result: 2.0")

    def test_power(self):
        result = subprocess.run(['python', 'first.py', 'power', '2', '3'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Result: 8.0")

    def test_modulo(self):
        result = subprocess.run(['python', 'first.py', 'modulo', '7', '3'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Result: 1.0")

    def test_invalid_operation(self):
        result = subprocess.run(['python', 'first.py', 'invalid', '2', '3'], capture_output=True, text=True)
        self.assertIn("usage: first.py [-h] {add,subtract,multiply,divide,power,modulo}", result.stderr)

if __name__ == '__main__':
    unittest.main()
