import unittest

class IntegerArithmeticTestCase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("用例执行前，只执行一次")
    @classmethod
    def tearDownClass(cls):
        print("用例执行后，只执行一次")

    # def setUp(self):
    #     #每个用例执行之前，先执行一次
    #     print(111)
    #
    # def tearDown(self):
    #     #每个用例执行之后，执行一次
    #     print(222)

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()