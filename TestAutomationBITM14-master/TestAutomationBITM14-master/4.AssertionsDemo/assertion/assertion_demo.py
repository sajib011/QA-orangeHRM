import unittest

class LoginTest(unittest.TestCase):

    def test_001(self):
        # assertEqual(expected, actual 'error message')
        self.assertEqual(10, 10, '10 is equal to 1')


if __name__ == '__main__':
    unittest.main()
