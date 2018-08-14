import unittest
from main import pig_latin_converter

class Test(unittest.TestCase):

    def test_input_as_string(self):
        with self.assertRaises(TypeError) as context:
            pig_latin_converter(1)
            pig_latin_converter(False)
            self.assertEqual(
                'Argument should be a string',
                context.exception.message,
                'String inputs allowed only'
            )
            
    def test_correct_output_if_vowel_at_first_pos(self):
        result1 = pig_latin_converter('andela')
        result2 = pig_latin_converter('ipsum')
        self.assertEqual(result1, 'andelaway')
        self.assertEqual(result2, 'ipsumway')

    def test_correct_output_if_first_pos_not_vowel(self):
        result1 = pig_latin_converter('dryer')
        result2 = pig_latin_converter('chemistry')
        result3 = pig_latin_converter('verge')
        self.assertEqual(result1, 'erdryay')
        self.assertEqual(result2, 'emistrychay')
        self.assertEqual(result3, 'ergevay')


if __name__ == '__main__':
    unittest.main()
