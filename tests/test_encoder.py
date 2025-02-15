# This file is placed in the Public Domain.
#
#
# pylint: disable=C,R,W1503


"no tests"


import unittest


from objx import Object, dumps


class TestEncoder(unittest.TestCase):

    def test_emptystring(self):
        aaa = ""
        res = dumps(aaa)
        self.assertEqual(res, '""')

    def test_string(self):
        a = "b"
        res = dumps(a)
        self.assertEqual(res, '"b"')

    def test_zero(self):
        a = 0
        res = dumps(a)
        self.assertEqual(res, "0")

    def test_integer(self):
        a = 1
        res = dumps(a)
        self.assertEqual(res, "1")

    def test_zerofloat(self):
        a = 0.0
        res = dumps(a)
        self.assertEqual(res, "0.0")

    def test_float(self):
        a = 1.1
        res = dumps(a)
        self.assertEqual(res, "1.1")

    def test_true(self):
        a = True
        res = dumps(a)
        self.assertEqual(res, "true")

    def test_false(self):
        a = False
        res = dumps(a)
        self.assertEqual(res, "false")

    def test_emptydict(self):
        a = {}
        res = dumps(a)
        self.assertEqual(res, "{}")

    def test_dict(self):
        a = {"a": "b"}
        res = dumps(a)
        self.assertEqual(res, '{"a": "b"}')

    def test_emptyobject(self):
        o = Object()
        res = dumps(o)
        self.assertEqual(res, '{}')

    def test_object(self):
        o = Object()
        o.aaa = "b"
        res = dumps(o)
        self.assertEqual(res, '{"aaa": "b"}')
