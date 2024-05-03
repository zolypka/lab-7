from second import find_mm
import unittest

def find_mm(s):
    bfint = 0
    bfstr = ''
    for i in range(1, len(s)):
        for j in range(0, i):
            if s[j:i] >= bfint and len(bfstr) < len(s[j:i]):
                bfint = s.count(s[j:i])
                bfstr = s[j:i]
            elif s.count(s[j:i]) > bfint:
                bfint = s.count(s[j:i])
                bfstr = s[j:i]
    return bfint, bfstr

class TestFindMm(unittest.TestCase):
    def test_find_mm(self):
        self.assertEqual(find_mm("abcaabcaab"), (3, "ab"))

if __name__ == "__main__":
    unittest.main()