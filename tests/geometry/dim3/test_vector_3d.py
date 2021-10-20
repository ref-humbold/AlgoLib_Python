# -*- coding: utf-8 -*-
import unittest

from assertpy import assert_that

from algolib.geometry.dim3 import Point3D, Vector3D


class Vector3DTest(unittest.TestCase):
    OFFSET = Vector3D.EPSILON

    @staticmethod
    def test__coordinates__then_triple_of_coordinates():
        # when
        result = Vector3D(5.0, -19.0, 14.2).coordinates
        # then
        assert_that(result).is_equal_to((5.0, -19.0, 14.2))

    def test__length__then_length_of_vector(self):
        # when
        result = Vector3D(18.0, -6.0, 13.0).length
        # then
        assert_that(result).is_close_to(23.0, self.OFFSET)

    @staticmethod
    def test__op_pos__then_copied():
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        result = +vector
        # then
        assert_that(result).is_not_same_as(vector)
        assert_that(result).is_equal_to(Vector3D(5.4, 9.0, -12.3))

    @staticmethod
    def test__op_neg__then_negate_each_coordinate():
        # when
        result = -Vector3D(5.4, 9.0, -12.3)
        # then
        assert_that(result).is_equal_to(Vector3D(-5.4, -9.0, 12.3))

    @staticmethod
    def test__op_add__then_add_each_coordinate():
        # when
        result = Vector3D(5.4, 9.0, -12.3) + Vector3D(7.9, -8.1, 1.4)
        # then
        assert_that(result).is_equal_to(Vector3D(13.3, 0.9, -10.9))

    @staticmethod
    def test__op_iadd__then_add_each_coordinate():
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector += Vector3D(7.9, -8.1, 1.4)
        # then
        assert_that(vector).is_equal_to(Vector3D(13.3, 0.9, -10.9))

    @staticmethod
    def test__op_sub__then_subtract_each_coordinate():
        # when
        result = Vector3D(5.4, 9.0, -12.3) - Vector3D(7.9, -8.1, 1.4)
        # then
        assert_that(result).is_equal_to(Vector3D(-2.5, 17.1, -13.7))

    @staticmethod
    def test__op_isub__then_subtract_each_coordinate():
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector -= Vector3D(7.9, -8.1, 1.4)
        # then
        assert_that(vector).is_equal_to(Vector3D(-2.5, 17.1, -13.7))

    @staticmethod
    def test__op_mul__then_multiply_each_coordinate():
        # when
        result = Vector3D(5.4, 9.0, -12.3) * 3
        # then
        assert_that(result).is_equal_to(Vector3D(16.2, 27.0, -36.9))

    @staticmethod
    def test__op_mul__when_multiplication_by_zero__then_zero_vector():
        # when
        result = Vector3D(5.4, 9.0, -12.3) * 0
        # then
        assert_that(result).is_equal_to(Vector3D(0.0, 0.0, 0.0))

    @staticmethod
    def test__op_rmul__then_multiply_each_coordinate():
        # when
        result = 3 * Vector3D(5.4, 9.0, -12.3)
        # then
        assert_that(result).is_equal_to(Vector3D(16.2, 27.0, -36.9))

    @staticmethod
    def test__op_imul__then_multiply_each_coordinate():
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector *= 3
        # then
        assert_that(vector).is_equal_to(Vector3D(16.2, 27.0, -36.9))

    @staticmethod
    def test__op_truediv__then_divide_each_coordinate():
        # when
        result = Vector3D(5.4, 9.0, -12.3) / 3
        # then
        assert_that(result).is_equal_to(Vector3D(1.8, 3.0, -4.1))

    @staticmethod
    def test__op_truediv__when_division_by_zero__then_zero_division_error():
        # when
        def function(n):
            return Vector3D(1.0, 1.0, 1.0) / n

        # then
        assert_that(function).raises(ZeroDivisionError).when_called_with(0)

    @staticmethod
    def test__op_itruediv__then_divide_each_coordinate():
        # given
        vector = Vector3D(5.4, 9.0, -12.3)
        # when
        vector /= 3
        # then
        assert_that(vector).is_equal_to(Vector3D(1.8, 3.0, -4.1))

    @staticmethod
    def test__between__then_vector_from_begin_to_end():
        # when
        result = Vector3D.between(Point3D(2.4, 7.8, -10.3), Point3D(-1.5, 13.2, 15.8))
        # then
        assert_that(result).is_equal_to(Vector3D(-3.9, 5.4, 26.1))

    def test__dot__then_scalar_product(self):
        # when
        result = Vector3D.dot(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5))
        # then
        assert_that(result).is_close_to(-6.25, self.OFFSET)

    def test__dot__when_orthogonal__then_zero(self):
        # when
        result = Vector3D.dot(Vector3D(1.0, 0.0, 1.0), Vector3D(0.0, -2.0, 0.0))
        # then
        assert_that(result).is_close_to(0.0, self.OFFSET)

    @staticmethod
    def test__cross__then_cross_product():
        # when
        result = Vector3D.cross(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5))
        # then
        assert_that(result).is_equal_to(Vector3D(-42.75, -44.25, 32.25))

    @staticmethod
    def test__cross__when_parallel__then_zero():
        # when
        result = Vector3D.cross(Vector3D(3.0, 3.0, 3.0), Vector3D(-8.0, -8.0, -8.0))
        # then
        assert_that(result).is_equal_to(Vector3D(0.0, 0.0, 0.0))

    def test__area__then_length_of_cross_product(self):
        # when
        result = Vector3D.area(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5))
        # then
        assert_that(result).is_close_to(69.46716850426538, self.OFFSET)

    def test__area__when_parallel__then_zero(self):
        # when
        result = Vector3D.area(Vector3D(3.0, 3.0, 3.0), Vector3D(-8.0, -8.0, -8.0))
        # then
        assert_that(result).is_close_to(0.0, self.OFFSET)

    def test__volume__then_scalar_triple_product(self):
        # when
        result = Vector3D.volume(Vector3D(1.5, -4.0, -3.5), Vector3D(9.0, -2.5, 8.5),
                                 Vector3D(1.0, -1.0, 1.0))
        # then
        assert_that(result).is_close_to(33.75, self.OFFSET)

    def test__volume__when_parallel__then_zero(self):
        # when
        result = Vector3D.volume(Vector3D(3.0, 3.0, 3.0), Vector3D(-8.0, -8.0, -8.0),
                                 Vector3D(2.0, -2.0, 2.0))
        # then
        assert_that(result).is_close_to(0.0, self.OFFSET)

    def test__volume__when_orthogonal__then_zero(self):
        # when
        result = Vector3D.volume(Vector3D(3.0, 3.0, 3.0), Vector3D(1.0, 0.0, 1.0),
                                 Vector3D(0.0, -2.0, 0.0))
        # then
        assert_that(result).is_close_to(0.0, self.OFFSET)
