import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setup')

    def test01(self):
        self.assertEqual(1+2,3)

    def test02(self):
        self.assertGreaterEqual(5,4)

    def tearDown(self):
        print('teardown')


if __name__ == '__main__':
    unittest.main()