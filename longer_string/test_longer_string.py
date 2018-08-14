import unittest
from main import longer_string

class Test(unittest.TestCase):

    def test_only_accept_string(self):
        with self.assertRaises(TypeError) as context:
            longer_string(1, 2)
            longer_string(True, False)
            longer_string('one', False)
            longer_string(True, 'two')
            self.assertEqual('Argument should be a string', context.exception.message, 'String inputs allowed only')

    def test_correct_output_if_one_longer(self):
        self.assertEqual(longer_string('jimmy', 'jake'), 'jimmy', msg='Output not correct')

    def test_correct_output_if_both_input_equal(self):
        self.assertEqual(longer_string('june', 'jake'), 'june\njake', msg='All input should return equal')

    def test_output_as_line_break_if_both_equal(self):
        result = longer_string('jack', 'jane')
        self.assertEqual(result, 'jack\njane', msg='Output should be printed line by line')


if __name__ == '__main__':
    unittest.main()
