# -*- coding: utf-8 -*-
import unittest

from assertpy import assert_that

from algolib.geometry.dim2 import Point2D, Vector2D


class Vector2DTest(unittest.TestCase):
    OFFSET = Vector2D.EPSILON

    @staticmethod
    def test__coordinates__then_pair_of_coordinates():
        # when
        result = Vector2D(5.0, -19.0).coordinates
        # then
        assert_that(result).is_equal_to((5.0, -19.0))

    def test__length__then_length_of_vector(self):
        # when
        result = Vector2D(8.0, -6.0).length
        # then
        assert_that(result).is_close_to(10.0, self.OFFSET)

    @staticmethod
    def test__op_pos__then_copied():
        # given
        vector = Vector2D(5.4, 9.0)
        # when
        result = +vector
        # then
        assert_that(result).is_not_same_as(vector)
        assert_that(result).is_equal_to(Vector2D(5.4, 9.0))

    @staticmethod
    def test__op_neg__then_negate_each_coordinate():
        # when
        result = -Vector2D(5.4, 9.0)
        # then
        assert_that(result).is_equal_to(Vector2D(-5.4, -9.0))

    @staticmethod
    def test__op_add__then_add_each_coordinate():
        # when
        result = Vector2D(5.4, 9.0) + Vector2D(7.9, -8.1)
        # then
        assert_that(result).is_equal_to(Vector2D(13.3, 0.9))

    @staticmethod
    def test__op_iadd__then_add_each_coordinate():
        # given
        vector = Vector2D(5.4, 9.0)
        # when
        vector += Vector2D(7.9, -8.1)
        # then
        assert_that(vector).is_equal_to(Vector2D(13.3, 0.9))

    @staticmethod
    def test__op_sub__then_subtract_each_coordinate():
        # when
        result = Vector2D(5.4, 9.0) - Vector2D(7.9, -8.1)
        # then
        assert_that(result).is_equal_to(Vector2D(-2.5, 17.1))

    @staticmethod
    def test__op_isub__then_subtract_each_coordinate():
        # given
        vector = Vector2D(5.4, 9.0)
        # when
        vector -= Vector2D(7.9, -8.1)
        # then
        assert_that(vector).is_equal_to(Vector2D(-2.5, 17.1))

    @staticmethod
    def test__op_mul__then_multiply_each_coordinate():
        # when
        result = Vector2D(5.4, 9.0) * 3
        # then
        assert_that(result).is_equal_to(Vector2D(16.2, 27.0))

    @staticmethod
    def test__op_mul__when_multiplication_by_zero__then_zero_vector():
        # when
        result = Vector2D(5.4, 9.0) * 0
        # then
        assert_that(result).is_equal_to(Vector2D(0, 0))

    @staticmethod
    def test__op_imul__then_multiply_each_coordinate():
        # given
        vector = Vector2D(5.4, 9.0)
        # when
        vector *= 3
        # then
        assert_that(vector).is_equal_to(Vector2D(16.2, 27.0))

    @staticmethod
    def test__op_rmul__then_multiply_each_coordinate():
        # when
        result = 3 * Vector2D(5.4, 9.0)
        # then
        assert_that(result).is_equal_to(Vector2D(16.2, 27.0))

    @staticmethod
    def test__op_truediv__then_divide_each_coordinate():
        # when
        result = Vector2D(5.4, 9.0) / 3
        # then
        assert_that(result).is_equal_to(Vector2D(1.8, 3.0))

    @staticmethod
    def test__op_truediv__when_division_by_zero__then_zero_division_error():
        # when
        def function(n):
            return Vector2D(1.0, 1.0) / n

        # then
        assert_that(function).raises(ZeroDivisionError).when_called_with(0)

    @staticmethod
    def test__op_itruediv__then_divide_each_coordinate():
        # given
        vector = Vector2D(5.4, 9.0)
        # when
        vector /= 3
        # then
        assert_that(vector).is_equal_to(Vector2D(1.8, 3.0))

    @staticmethod
    def test__between__then_vector_from_begin_to_end():
        # when
        result = Vector2D.between(Point2D(2.4, 7.8), Point2D(-1.5, 13.2))
        # then
        assert_that(result).is_equal_to(Vector2D(-3.9, 5.4))

    def test__dot__then_scalar_product(self):
        # when
        result = Vector2D.dot(Vector2D(1.5, -4.0), Vector2D(9.0, -2.5))
        # then
        assert_that(result).is_close_to(23.5, self.OFFSET)

    def test__dot__when_orthogonal__then_zero(self):
        # when
        result = Vector2D.dot(Vector2D(1.0, 0.0), Vector2D(0.0, -2.0))
        # then
        assert_that(result).is_close_to(0.0, self.OFFSET)

    def test__area__then_length_of_cross_product(self):
        # when
        result = Vector2D.area(Vector2D(1.5, -4.0), Vector2D(9.0, -2.5))
        # then
        assert_that(result).is_close_to(32.25, self.OFFSET)

    def test__area__when_parallel__then_zero(self):
        # when
        result = Vector2D.area(Vector2D(3.0, 3.0), Vector2D(-8.0, -8.0))
        # then
        assert_that(result).is_close_to(0.0, self.OFFSET)
