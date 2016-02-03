from pyexample import examples
import unittest


class TestSimplePySparkExample(unittest.TestCase):
    def test_pyexample(self):
        self.assertEqual(examples.example(), 5)

if __name__ == "__main__":
    unittest.main()
