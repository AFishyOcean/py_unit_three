import unittest
import return_addtion
import triangle_area

class MyTestCase(unittest.TestCase):

    def test_return_addtion(self):

        self.assertEqual(15, return_addtion.add_two(7, 8))
        self.assertEqual(45, return_addtion.add_two(40, 5))
        # Add two more tests of your own below here
        self.assertEqual(75, return_addtion.add_two(25, 50))
        self.assertEqual(-45, return_addtion.add_two(-40, -5))

    def test_triangle_area(self):
        self.assertEqual(6.0, triangle_area.area(3, 4, 5))
        self.assertAlmostEqual(12.968712349343, triangle_area.area(7, 5, 11), 0.1)


if __name__ == '__main__':
    unittest.main()
