import unittest
from lib import rand_below, gen_single_chr_from_string

class TestRandBelow(unittest.TestCase):
    def test_random_num_is_in_range(self):
        self.assertGreaterEqual(rand_below(1), 0)

    def test_rand_below_generates_unequal_nums(self):
        """Test that the random number generator doesn't repeat the same number over and over. It is possible that this test will generate false negative results."""    
        num_times_first_num_repeated = 0
        first_num = rand_below(1000000000)
        for i in range(5):
            n = rand_below(1000000000)
            if n == first_num:
                num_times_first_num_repeated += 1
        self.assertNotEqual(num_times_first_num_repeated, 5)

class TestGenSingleChrFromString(unittest.TestCase):
    def test_empty_string_raises_exception(self):
        with self.assertRaises(Exception):
            gen_single_chr_from_string("")

    def test_single_character_returns_that_character(self):
        self.assertEqual(gen_single_chr_from_string("A"), "A")

    def test_multiple_characters_returns_one_of_them(self):
        result = gen_single_chr_from_string("ABC")
        self.assertIn(result, ["A", "B", "C"])
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
