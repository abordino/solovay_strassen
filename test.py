import unittest
import solov


class MyTest(unittest.TestCase):
    def test_solovay(self):
        self.assertEqual(solov.test_solovay(3), True)
        self.assertEqual(solov.test_solovay(19), True)
        self.assertEqual(solov.test_solovay(22), False)

    def test_gcd(self):
        self.assertEqual(solov.gcd(180, 297), 9)
        self.assertEqual(solov.gcd(125, 176), 1)

    def test_jacoby(self):
        self.assertEqual(solov.jacobi(23, 45), -1.0)
        self.assertEqual(solov.jacobi(1, 54), 1)


if __name__ == "__main__":
    unittest.main()
