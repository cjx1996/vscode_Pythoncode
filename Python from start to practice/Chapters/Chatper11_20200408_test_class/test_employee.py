from employee import Employee
import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self):
        '''创建一个对象和一组数值，供测试方法使用'''
        self.employee = Employee('Zhang','san',6000)
        self.raises = [3000,6000]

    def test_give_default_raise(self):
        '''测试能否正确提高默认薪水'''
        self.employee.give_raise()
        self.assertEqual(self.employee.wage,11000)

    def test_give_custom_raise(self):
        self.employee.give_raise(self.raises[1])
        self.assertEqual(self.employee.wage, 6000+self.raises[1])

unittest.main()

















