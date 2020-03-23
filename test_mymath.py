import sys
import mymath
import unittest
from unittest import skip

class TestAdd(unittest.TestCase):
    """
    test that we can add two numbers using teh add function from mymath
    """

    def test_add_integers(self):
        """
        test that the addition of two integers returns the correct total
        """

        result = mymath.add(4, 3)
        self.assertEqual(result, 7)


    def test_add_floats(self):
        """
        test that adding two floats returns the correct value
        """
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    @skip('Skipping the add strings test for now')
    def test_add_strings(self):
        """
        test that adding strings will produce the correct result
        """
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')


    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_adding_on_windows(self):
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
