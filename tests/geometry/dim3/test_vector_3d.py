# -*- coding: utf-8 -*-
import unittest

from algolib.geometry.dim3 import Point3D, Vector3D


class Vector3DTest(unittest.TestCase):
    OFFSET = Vector3D.EPSILON

    def test__coordinates__then_triple_of_coordinates(self):
        # when
        result = Vector3D(5.0, -19.0, 14.2).coordinates
        # then
        self.assertTupleEqual((5.0, -19.0, 14.2), result)

    def test__length__then_length_of_vector(self):
        # when
        result = Vector3D(18.0, -6.0, 13.0).length
        # then
        self.assertAlmostEqual(23.0, result, delta=self.OFFSET)

    def test__op_pos__then_copied(self):
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        result = +vector
        # then
        self.assertIsNot(vector, result)
        self.assertEqual(Vector3D(5.4, 9.0, -12.3), result)

    def test__op_neg__then_negate_each_coordinate(self):
        # when
        result = -Vector3D(5.4, 9.0, -12.3)
        # then
        self.assertEqual(Vector3D(-5.4, -9.0, 12.3), result)

    def test__op_add__then_add_each_coordinate(self):
        # when
        result = Vector3D(5.4, 9.0, -12.3) + Vector3D(7.9, -8.1, 1.4)
        # then
        self.assertEqual(Vector3D(13.3, 0.9, -10.9), result)

    def test__op_iadd__then_add_each_coordinate(self):
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector += Vector3D(7.9, -8.1, 1.4)
        # then
        self.assertEqual(Vector3D(13.3, 0.9, -10.9), vector)

    def test__op_sub__then_subtract_each_coordinate(self):
        # when
        result = Vector3D(5.4, 9.0, -12.3) - Vector3D(7.9, -8.1, 1.4)
        # then
        self.assertEqual(Vector3D(-2.5, 17.1, -13.7), result)

    def test__op_isub__then_subtract_each_coordinate(self):
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector -= Vector3D(7.9, -8.1, 1.4)
        # then
        self.assertEqual(Vector3D(-2.5, 17.1, -13.7), vector)

    def test__op_mul__then_multiply_each_coordinate(self):
        # when
        result = Vector3D(5.4, 9.0, -12.3) * 3
        # then
        self.assertEqual(Vector3D(16.2, 27.0, -36.9), result)

    def test__op_mul__when_multiplication_by_zero__then_zero_vector(self):
        # when
        result = Vector3D(5.4, 9.0, -12.3) * 0
        # then
        self.assertEqual(Vector3D(0.0, 0.0, 0.0), result)

    def test__op_rmul__then_multiply_each_coordinate(self):
        # when
        result = 3 * Vector3D(5.4, 9.0, -12.3)
        # then
        self.assertEqual(Vector3D(16.2, 27.0, -36.9), result)

    def test__op_imul__then_multiply_each_coordinate(self):
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector *= 3
        # then
        self.assertEqual(Vector3D(16.2, 27.0, -36.9), vector)

    def test__op_truediv__then_divide_each_coordinate(self):
        # when
        result = Vector3D(5.4, 9.0, -12.3) / 3
        # then
        self.assertEqual(Vector3D(1.8, 3.0, -4.1), result)

    def test__op_truediv__when_division_by_zero__then_zero_division_error(self):
        # then
        with self.assertRaises(ZeroDivisionError):
            # when
            _ = Vector3D(1.0, 1.0, 1.0) / 0

    def test__op_itruediv__then_divide_each_coordinate(self):
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector /= 3
        # then
        self.assertEqual(Vector3D(1.8, 3.0, -4.1), vector)

    def test__between__then_vector_from_begin_to_end(self):
        # when
        result = Vector3D.between(Point3D(2.4, 7.8, -10.3), Point3D(-1.5, 13.2, 15.8))
        # then
        self.assertEqual(Vector3D(-3.9, 5.4, 26.1), result)

    def test__dot__then_scalar_product(self):
        # when
        result = Vector3D.dot(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5))
        # then
        self.assertAlmostEqual(-6.25, result, delta=self.OFFSET)

    def test__dot__when_orthogonal__then_zero(self):
        # when
        result = Vector3D.dot(Vector3D(1.0, 0.0, 1.0), Vector3D(0.0, -2.0, 0.0))
        # then
        self.assertAlmostEqual(0.0, result, delta=self.OFFSET)

    def test__cross__then_cross_product(self):
        # when
        result = Vector3D.cross(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5))
        # then
        self.assertEqual(Vector3D(-42.75, -44.25, 32.25), result)

    def test__cross__when_parallel__then_zero(self):
        # when
        result = Vector3D.cross(Vector3D(3.0, 3.0, 3.0), Vector3D(-8.0, -8.0, -8.0))
        # then
        self.assertEqual(Vector3D(0.0, 0.0, 0.0), result)

    def test__area__then_length_of_cross_product(self):
        # when
        result = Vector3D.area(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5))
        # then
        self.assertAlmostEqual(69.46716850426538, result, delta=self.OFFSET)

    def test__area__when_parallel__then_zero(self):
        # when
        result = Vector3D.area(Vector3D(3.0, 3.0, 3.0), Vector3D(-8.0, -8.0, -8.0))
        # then
        self.assertAlmostEqual(0.0, result, delta=self.OFFSET)

    def test__volume__then_scalar_triple_product(self):
        # when
        result = Vector3D.volume(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5),
                                 Vector3D(1.0, -1.0, 1.0))
        # then
        self.assertAlmostEqual(33.75, result, delta=self.OFFSET)

    def test__volume__when_parallel__then_zero(self):
        # when
        result = Vector3D.volume(Vector3D(3.0, 3.0, 3.0), Vector3D(-8.0, -8.0, -8.0),
                                 Vector3D(2.0, -2.0, 2.0))
        # then
        self.assertAlmostEqual(0.0, result, delta=self.OFFSET)

    def test__volume__when_orthogonal__then_zero(self):
        # when
        result = Vector3D.volume(Vector3D(3.0, 3.0, 3.0), Vector3D(1.0, 0.0, 1.0),
                                 Vector3D(0.0, -2.0, 0.0))
        # then
        self.assertAlmostEqual(0.0, result, delta=self.OFFSET)
