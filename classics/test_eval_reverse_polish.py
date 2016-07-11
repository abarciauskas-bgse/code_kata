import unittest
execfile('eval_reverse_polish.py')

class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(ValueError) as context:
            eval_reverse_polish(["4", "13", "5", "/"])

        self.assertTrue("Bad arguments: invalid operator operand combination" in context.exception)

if __name__ == '__main__':
    unittest.main()
