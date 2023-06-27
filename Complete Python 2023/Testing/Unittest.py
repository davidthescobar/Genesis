# Testing is a method to test whether units (functions) work properly
# Usually, there is a test file for every python module (file)
# 100 files = 100 test files
import unittest
import main

# Create a function with the correct outcome, see if the prediction is right
class TestMain(unittest.TestCase):
  def test_do_stuff(self):
    test_param = 10
    result = main.do_stuff(test_param)
    self.assertEqual(result, 15)

  def test_do_stuff2(self):
    test_param = 'qpwihwq'
    result = main.do_stuff(test_param)
    self.assertEqual(result, TypeError)

unittest.main()