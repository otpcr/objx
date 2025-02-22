# This file is placed in the Public Domain.
# ruff: noqa: F403,F405


"interface"


import logging
import sys
import unittest
import objx


from objx.objects import *


PACKAGE = [
    '__doc__',
    '__file__',
    '__loader__',
    '__name__',
    '__package__',
    '__spec__',
]


METHODS = [
    '__class__',
    '__contains__',
    '__delattr__',
    '__dict__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__getstate__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__iter__',
    '__le__',
    '__len__',
    '__lt__',
    '__module__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__str__',
    '__subclasshook__',
    '__weakref__'
]


DICT = {}


DIFF = [
    "__dict__",
    "__module__",
    "__slots__",
]


OBJECT = objx.objects


class TestInterface(unittest.TestCase):

    "TestInterface"

    def test_package(self):
        "test methods interface."
        okd = True
        for meth in PACKAGE:
            func1 = getattr(OBJECT, meth)
            if not func1:
                continue
            func2 = DICT.get(meth)
            if not func2:
                continue
            if dir(func1) != dir(func2):
                print(func1, func2)
                okd = False
            sys.stdout.flush()
        self.assertTrue(okd)


    def test_objects(self):
        "test methods interface."
        okd = True
        obj = Object()
        for meth in METHODS:
            func1 = getattr(obj, meth)
            if not func1:
                continue
            func2 = DICT.get(meth)
            if not func2:
                continue
            if dir(func1) != dir(func2):
                print(func1, func2)
                okd = False
            sys.stdout.flush()
        self.assertTrue(okd)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("SomeTest.testSomething").setLevel(logging.DEBUG)
    unittest.main()
