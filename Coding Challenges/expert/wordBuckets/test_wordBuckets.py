from wordBuckets import split_into_buckets
import unittest

# a list of test cases taken from the edabit testing page. I modified the contents to be executable in my use case.

class testingWordBuckets(unittest.TestCase):

    def test_1(self):
        self.assertEqual(split_into_buckets("she sells sea shells by the sea", 2), [])

    def test_2(self):
        self.assertEqual(split_into_buckets("ab bc cd", 1), [])

    def test_3(self):
        self.assertEqual(split_into_buckets("she sells sea shells by the sea", 10), ["she sells", "sea shells", "by the sea"])

    def test_4(self):
        self.assertEqual(split_into_buckets("the mouse jumped over the cheese", 7), ["the", "mouse", "jumped", "over", "the", "cheese"])

    def test_5(self):
        self.assertEqual(split_into_buckets("fairy dust coated the air", 20), ["fairy dust coated", "the air"])

    def test_6(self):
        self.assertEqual(split_into_buckets("do the hokey pokey", 6), ["do the", "hokey", "pokey"])

    def test_7(self):
        self.assertEqual(split_into_buckets("do the hokey pokey", 12), ["do the hokey", "pokey"])

    def test_8(self):
        self.assertEqual(split_into_buckets("rich magnificent trees dotted the landscape", 12), ["rich", "magnificent", "trees dotted", "the", "landscape"])

    def test_9(self):
        self.assertEqual(split_into_buckets("rich magnificent trees dotted the landscape", 15), ["rich", "magnificent", "trees dotted", "the landscape"])

    def test_10(self):
        self.assertEqual(split_into_buckets("rich magnificent trees dotted the landscape", 18), ["rich magnificent", "trees dotted the", "landscape"])

    def test_11(self):
        self.assertEqual(split_into_buckets("rich magnificent trees dotted the landscape", 22), ["rich magnificent trees", "dotted the landscape"])

    def test_12(self):
        self.assertEqual(split_into_buckets("rich magnificent trees dotted the landscape", 40), ["rich magnificent trees dotted the", "landscape"])

    def test_13(self):
        self.assertEqual(split_into_buckets("rich magnificent trees dotted the landscape", 43), ["rich magnificent trees dotted the landscape"])

    def test_14(self):
        self.assertEqual(split_into_buckets("beep bo bee bop bee bo bo bop", 6), ["beep", "bo bee", "bop", "bee bo", "bo bop"])

    def test_15(self):
        self.assertEqual(split_into_buckets("beep bo bee bop bee bo bo bop", 10), ["beep bo", "bee bop", "bee bo bo", "bop"])

    def test_16(self):
        self.assertEqual(split_into_buckets("a b c d e", 3), ["a b", "c d", "e"])

    def test_17(self):
        self.assertEqual(split_into_buckets("a b c d e", 2), ["a", "b", "c", "d", "e"])

    def test_18(self):
        self.assertEqual(split_into_buckets("a b c d e", 1), ["a", "b", "c", "d", "e"])


    
if __name__ == "__main__":
    unittest.main()