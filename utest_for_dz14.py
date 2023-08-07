import unittest
from dz14 import Rectangle, InvalidRectangleError


class TestRectangle(unittest.TestCase):
    def test_create_valid_rectangle(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.length, 5)
        self.assertEqual(rectangle.width, 10)

    def test_create_invalid_rectangle(self):
        with self.assertRaises(InvalidRectangleError):
            Rectangle(0, 10)
        with self.assertRaises(InvalidRectangleError):
            Rectangle(5, 0)

    def test_create_negative_length_rectangle(self):
        with self.assertRaises(InvalidRectangleError) as context:
            Rectangle(-5, 10)
        self.assertEqual(str(context.exception), "Прямоугольник не может иметь нулевую или отрицательную длину "
                                                 "или ширину.")

    def test_create_negative_width_rectangle(self):
        with self.assertRaises(InvalidRectangleError) as context:
            Rectangle(5, -10)
        self.assertEqual(str(context.exception), "Прямоугольник не может иметь нулевую или отрицательную длину "
                                                 "или ширину.")

    def test_perimeter(self):
        rectangle = Rectangle(5, 10)
        perimeter = rectangle.perimeter()
        self.assertEqual(perimeter, 30)

    def test_area(self):
        rectangle = Rectangle(5, 10)
        area = rectangle.area()
        self.assertEqual(area, 50)

    def test_add_rectangles(self):
        rectangle1 = Rectangle(5, 10)
        rectangle2 = Rectangle(3, 7)
        rectangle3 = rectangle1 + rectangle2
        self.assertEqual(rectangle3.length, 8)
        self.assertEqual(rectangle3.width, 17)

    def test_subtract_rectangles(self):
        rectangle1 = Rectangle(5, 10)
        rectangle2 = Rectangle(3, 7)
        rectangle4 = rectangle1 - rectangle2
        self.assertEqual(rectangle4.length, 2)
        self.assertEqual(rectangle4.width, 3)


if __name__ == '__main__':
    unittest.main()
