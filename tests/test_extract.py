import unittest
import os
import acbpy


class TestExtract(unittest.TestCase):
    def setUp(self):
        pass

    def test_one(self):
        abspath = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(abspath, "sample.acb"), "rb") as f:
            print(acbpy.parse_binary(f))
