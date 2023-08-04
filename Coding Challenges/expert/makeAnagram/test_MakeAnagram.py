from makeAnagram import make_anagram
import unittest

# a list of test cases taken from the edabit testing page. I modified the contents to be executable in my use case.

class testAnagram(unittest.TestCase):

    def test_1(self):
        self.assertEqual(make_anagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'), 30)

    def test_2(self):
        self.assertEqual(make_anagram('bugexikjevtubidpulaelsbcqlupwetzyzdvjphn', 'lajoipfecfinxjspxmevqxuqyalhrsxcvgsdxxkacspbchrbvvwnvsdtsrdk'), 40)
    
    def test_3(self):
        self.assertEqual(make_anagram('fsqoiaidfaukvngpsugszsnseskicpejjvytviya', 'ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget'), 42)

    def test_4(self):
        self.assertEqual(make_anagram('showman', 'woman'), 2)

    def test_5(self):
        self.assertEqual(make_anagram('imkhnpqnhlvaxlmrsskbyyrhwfvgteubrelgubvdmrdmesfxkpykprunzpustowmvhupkqsyjxmnptkcilmzcinbzjwvxshubeln', 'wfnfdassvfugqjfuruwrdumdmvxpbjcxorettxmpcivurcolxmeagsdundjronoehtyaskpwumqmpgzmtdmbvsykxhblxspgnpgfzydukvizbhlwmaajuytrhxeepvmcltjmroibjsdkbqjnqjwmhsfopjvehhiuctgthrxqjaclqnyjwxxfpdueorkvaspdnywupvmy'), 102)

    def test_6(self):
        self.assertEqual(make_anagram('cde', 'abc'), 4)


if __name__ == "__main__":
    unittest.main()