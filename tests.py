import unittest
from lib import randbelow

class TestRandBelow(unittest.TestCase):
    def test_random_num_is_in_range(self):
        self.assertGreaterEqual(randbelow(1), 0)

if __name__ == '__main__':
    unittest.main()
