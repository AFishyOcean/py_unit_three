import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_assignment_three(self):
        self.assertEqual(25, assignment_three.rectangle_area(5, 5))
        self.assertEqual(42, assignment_three.rectangle_area(6, 7))
        self.assertEqual(150, assignment_three.calculate_surface_area(5, 5, 5))
        #self.assertEqual(150, assignment_three.calculate_surface_area(5, 5, 5))
        # add assertion here

if __name__ == '__main__':
    unittest.main()
