import unittest
from load_results import calculate_mark


class CalculateMarkTest(unittest.TestCase):
    def testOnlyOneTopic(self):
        solved = [1, 1, 1, 1, 1, 1,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0]
        expected = 1
        got = calculate_mark(solved)
        self.assertEqual(expected, got)
    
    def testOnlyOneLevel(self):
        solved = [1, 0, 0, 0, 0, 0,
                  1, 0, 0, 0, 0, 0,
                  1, 0, 0, 0, 0, 0,
                  1, 0, 0, 0, 0, 0,
                  1, 0, 0, 0, 0, 0]
        expected = 1
        got = calculate_mark(solved)
        self.assertEqual(expected, got)
    
    def testFullSolved(self):
        solved = [1, 0, 0, 0, 0, 0,
                  0, 0, 1, 0, 0, 0,
                  0, 1, 0, 0, 0, 0,
                  0, 0, 0, 1, 0, 0,
                  0, 0, 0, 0, 0, 1]
        expected = 5
        got = calculate_mark(solved)
        self.assertEqual(expected, got)
        
    def testPartiallySolved(self):
        solved = [1, 0, 0, 0, 0, 0,
                  0, 0, 1, 0, 0, 0,
                  0, 1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 1]
        expected = 4
        got = calculate_mark(solved)
        self.assertEqual(expected, got)
        
    def testZeroSolved(self):
        solved = [0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0]
        expected = 0
        got = calculate_mark(solved)
        self.assertEqual(expected, got)

    def testVsevolod(self):
        solved = [1, 0, 1, 0, 0, 1,
                  0, 0, 1, 0, 0, 0,
                  0, 1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 1]
        expected = 4
        got = calculate_mark(solved)
        self.assertEqual(expected, got)
        
    @unittest.skip
    def testTenPoints(self):
        solved = [1, 1, 1, 1, 1, 1,
                  1, 0, 0, 0, 0, 0,
                  0, 1, 0, 0, 0, 0,
                  0, 0, 1, 0, 0, 0,
                  0, 0, 0, 1, 0, 0]
        expected = 10
        got = calculate_mark(solved)
        self.assertEqual(expected, got)
    
if __name__ == '__main__':
    unittest.main()