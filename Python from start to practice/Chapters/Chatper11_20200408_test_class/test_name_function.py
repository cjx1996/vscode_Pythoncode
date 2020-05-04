import unittest
from name_function import get_formatted_name
class NameTestCase(unittest.TestCase):
    '''
    测试name_function.py
    '''
    def test_first_last_name(self):
        '''
        能够正确处理像Janis Joplin这样的姓名吗？
        '''
        format_name = get_formatted_name('Janis', 'Joplin')
        self.assertEqual(format_name, 'Janis Joplin')


    def test_first_last_middle_name(self):
        '''
        能够正确处理像Wolfgang Amadeus Mozart这样的姓名吗？
        '''
        format_name  = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(format_name, 'Wolfgang Amadeus Mozart')







unittest.main()




