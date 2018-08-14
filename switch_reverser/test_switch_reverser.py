import unittest
from main import switch_reverser

class Test(unittest.TestCase):

    def test_input_as_list(self):
        with self.assertRaises(TypeError) as context:
            switch_reverser(1)
            switch_reverser(True)
            switch_reverser(1,5,7)
            self.assertEqual(
                'Argument should be a string',
                context.exception.message,
                'String inputs allowed only'
            )
            
    def test_check_if_output_is_correct(self):
        result1 = switch_reverser([47,256,17,4])
        result2 = switch_reverser([None,3.4,True,'german'])
        result3 = switch_reverser(['marshmellow','candy','pepperoni','tacos'])
        self.assertEqual(result1, [4,17,256,47])
        self.assertEqual(result2, [None,3.4,True,'german'])
        self.assertEqual(result3, ['MARSHMELLOW','CANDY','PEPPERONI','TACOS'])

    def test_check_if_output_is_a_list(self):
        results = switch_reverser([None,3.4,True,'german'])
        self.assertIsInstance(results, list, msg='Incorrect output type')


if __name__ == '__main__':
    unittest.main()
