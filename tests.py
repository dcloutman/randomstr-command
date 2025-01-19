import unittest
from lib import randbelow

class TestRandBelow(unittest.TestCase):
    def test_random_num_is_in_range(self):
        self.assertGreaterEqual(randbelow(1), 0)

    def test_randbelow_generates_unequal_nums(self):
        """Test that the random number generator doesn't repeat the same number over and over. It is possible that this test will generate false negative results."""    
        num_times_first_num_repeated = 0
        first_num = randbelow(1000000000)
        for i in range(5):
            n = randbelow(1000000000)
            if n == first_num:
                num_times_first_num_repeated += 1
        self.assertNotEqual(num_times_first_num_repeated, 5)

if __name__ == '__main__':
    unittest.main()
