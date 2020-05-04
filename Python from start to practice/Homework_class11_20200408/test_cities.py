import unittest
from city_functions import get_city_country_name


class NameTestCase(unittest.TestCase):
    '''
    测试city_functions.py
    '''
    def test_city_country(self):
        '''
        测试能否正确处理像Santiago,Chile格式的输入
        '''
        format_name = get_city_country_name('Santiago', 'Chile')
        self.assertEqual(format_name,'Santiago, Chile- population 4000000')

    def test_city_country_population(self):
        '''
        测试能否正确处理像Santiago,Chile,5000000格式的输入
        '''
        format_name = get_city_country_name('Santiago','Chile','5000000')
        self.assertEqual(format_name,'Santiago, Chile- population 5000000')




unittest.main()





