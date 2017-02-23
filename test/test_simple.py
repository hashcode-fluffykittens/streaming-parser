import unittest
# import '../input_parser'

test_example = """
5 2 4 3 100
50 50 80 30 110
1000 3
0 100
2 200
1 300
500 0
3 0 1500
0 1 1000
4 0 500
1 0 1000
"""

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testParse(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
