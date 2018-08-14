import unittest
from main import check_upper, check_lower, check_number, check_special, check_length, output_func

class Test(unittest.TestCase):

    def test_check_upper_returns_true(self):
        self.assertEqual(check_upper('capiTol'), True, msg='Return value is wrong')
        self.assertEqual(check_upper('CAPItOL'), True, msg='Return value is wrong')

    def test_check_upper_returns_false(self):
        self.assertEqual(check_upper('capitol'), False, msg='Return value is wrong')


    def test_check_lower_returns_true(self):
        self.assertEqual(check_lower('sMALL'), True, msg='Return value is wrong')
        self.assertEqual(check_lower('smAll'), True, msg='Return value is wrong')

    def test_check_lower_returns_false(self):
        self.assertEqual(check_lower('SMALL'), False, msg='Return value is wrong')

    def test_check_number_returns_true(self):
        self.assertEqual(check_number('cap1Tol'), True, msg='Return value is wrong')
        self.assertEqual(check_number('123Cap'), True, msg='Return value is wrong')

    def test_check_number_returns_false(self):
        self.assertEqual(check_number('Capitol'), False, msg='Return value is wrong')
        self.assertEqual(check_number('CAPITOL'), False, msg='Return value is wrong')
        self.assertEqual(check_number('capitol'), False, msg='Return value is wrong')

    def test_check_special_returns_true(self):
        self.assertEqual(check_special('C@pitol'), True, msg='Return value is wrong')
        self.assertEqual(check_special('#$@'), True, msg='Return value is wrong')
        self.assertEqual(check_special('C@p1#ol'), True, msg='Return value is wrong')

    def test_check_special_returns_false(self):
        self.assertEqual(check_special('123Caps'), False, msg='Return value is wrong')
        self.assertEqual(check_special('CaPITOl'), False, msg='Return value is wrong')
        self.assertEqual(check_special('small'), False, msg='Return value is wrong')

    def test_check_length_returns_true(self):
        self.assertEqual(check_length('#rSd456V'), True, msg='Return value is wrong')
        self.assertEqual(check_length('CAPITOL'), True, msg='Return value is wrong')
        self.assertEqual(check_length('122374583'), True, msg='Return value is wrong')

    def test_check_length_returns_false(self):
        self.assertEqual(check_length('#3Cap'), False, msg='Return value is wrong')
        self.assertEqual(check_length('@#34hdGdje3873272'), False, msg='Return value is wrong')

    def test_check_correct_output(self):
        my_list1 = ['f@b1scH', '123ol', '#$gH1sV']
        my_list2 = ['fabisch', '1234', '#$@']
        my_list3 = ['d@m$tyur#R78dsfjY', 'eg$gt', '#$Df78v']
        sample_input1 = ','.join(my_list1)
        sample_input2 = ','.join(my_list2)
        sample_input3 = ','.join(my_list3)
        list_output1 = ['f@b1scH', '#$gH1sV']
        list_output2 = ['']
        list_output3 = ['#$Df78v']
        expected_output1 = ','.join(list_output1)
        expected_output2 = ','.join(list_output2)
        expected_output3 = ','.join(list_output3)
        self.assertEqual(output_func(sample_input1), expected_output1)
        self.assertEqual(output_func(sample_input2), expected_output2)
        self.assertEqual(output_func(sample_input3), expected_output3)


if __name__ == '__main__':
    unittest.main()
