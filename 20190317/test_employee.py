import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class employee."""

    def setUp(self):
        """
        Create a employee' attribute for use in all test methods.
        """
        self.my_employee = Employee('zachary', 'zhuo', 0)

    def test_give_default_raise(self):
        """Test that give default raise propertly."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 5000)

    def test_give_custom_raise(self):
        """Test that give custom raise propertly."""
        self.my_employee.give_raise(8000)
        self.assertEqual(self.my_employee.salary, 8000)

unittest.main()


"""
assertEqual(a, b)       驗證 a==b
assertNotEqual(a, b)    驗證 a!=b
assertTrue(x)           驗證 x 為 True
assertFalse(x)          驗證 x 為 False
assertIn(item, list)    驗證 item 有在 list 串列內
assertNotIn(item, list) 驗證 item 沒有在 list 串列內
"""