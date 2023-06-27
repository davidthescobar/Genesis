import unittest
import TestingExercise

class TestMain(unittest.TestCase):
  def test_run_guess(self):
    result = TestingExercise.run_guess(5, 5)
    self.assertTrue(result)

def test_run_guess_incorrect(self):
    result = TestingExercise.run_guess(5, 0)
    self.assertTrue(result)

def test_run_guess_wrongnum(self):
    result = TestingExercise.run_guess(5, 11)
    self.assertTrue(result)

def test_run_guess_string(self):
    result = TestingExercise.run_guess(5, '11')
    self.assertTrue(result)

if __name__ == '__main__':
  unittest.main()