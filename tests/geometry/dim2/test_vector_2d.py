import unittest

from algolib.geometry.dim2 import Point2D, Vector2D


class Vector2DTest(unittest.TestCase):
    OFFSET = Vector2D.EPSILON

    def test__between__then_vector_from_begin_to_end(self):
        # when
        result = Vector2D.between(Point2D(2.4, 7.8), Point2D(-1.5, 13.2))
        # then
        self.assertEqual(Vector2D(-3.9, 5.4), result)

    def test__coordinates__then_array(self):
        # when
        result = Vector2D(5.0, -19.0).coordinates
        # then
        self.assertTupleEqual((5.0, -19.0), result)

    def test__dot__then_scalar_product(self):
        # when
        result = Vector2D.dot(Vector2D(1.5, -4.0), (Vector2D(9.0, -2.5)))
        # then
        self.assertAlmostEqual(23.5, result, delta=self.OFFSET)

    def test__dot__when_orthogonal__then_zero(self):
        # when
        result = Vector2D.dot(Vector2D(1.0, 0.0), (Vector2D(0.0, -2.0)))
        # then
        self.assertAlmostEqual(0.0, result, delta=self.OFFSET)

    def test__area__then_length_of_cross_product(self):
        # when
        result = Vector2D.area(Vector2D(1.5, -4.0), (Vector2D(9.0, -2.5)))
        # then
        self.assertAlmostEqual(32.25, result, delta=self.OFFSET)

    def test__area__when_parallel__then_zero(self):
        # when
        result = Vector2D.area(Vector2D(3.0, 3.0), (Vector2D(-8.0, -8.0)))
        # then
        self.assertAlmostEqual(0.0, result, delta=self.OFFSET)

    def test__length__then_length_of_vector(self):
        # when
        result = Vector2D(8.0, -6.0).length
        # then
        self.assertAlmostEqual(10.0, result, delta=self.OFFSET)

    def test__add__then_add_each_coordinate(self):
        # when
        result = Vector2D(5.4, 9.0) + Vector2D(7.9, -8.1)
        # then
        self.assertEqual(Vector2D(13.3, 0.9), result)

    def test__sub__then_subtract_each_coordinate(self):
        # when
        result = Vector2D(5.4, 9.0) - Vector2D(7.9, -8.1)
        # then
        self.assertEqual(Vector2D(-2.5, 17.1), result)

    def test__mul__then_multiply_each_coordinate(self):
        # when
        result = Vector2D(5.4, 9.0) * 3
        # then
        self.assertEqual(Vector2D(16.2, 27.0), result)

    def test__mul__when_multiplication_by_zero__then_zero_vector(self):
        # when
        result = Vector2D(5.4, 9.0) * 0
        # then
        self.assertEqual(Vector2D(0, 0), result)

    def test__truediv__then_divide_each_coordinate(self):
        # when
        result = Vector2D(5.4, 9.0) / 3
        # then
        self.assertEqual(Vector2D(1.8, 3.0), result)

    def test__truediv__when_division_by_zero__then_zero_division_error(self):
        # then
        with self.assertRaises(ZeroDivisionError):
            _ = Vector2D(1.0, 1.0) / 0
