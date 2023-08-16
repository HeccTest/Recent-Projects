from copyPaste import keyboard_shortcut
import unittest

# a list of test cases taken from the edabit testing page. I modified the contents to be executable in my use case.

class testingCopyPaste(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon"), "the egg and the egg and the spoon")
    
    def test_2(self):
        self.assertEqual(keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V"), "WARNING WARNING")
    
    def test_3(self):
        self.assertEqual(keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"), "The The Town The The Town")
    
    def test_4(self):
        self.assertEqual(keyboard_shortcut("bacteria Ctrl + C Ctrl + V Ctrl + C Ctrl + V Ctrl + C Ctrl + V"), "bacteria bacteria bacteria bacteria bacteria bacteria bacteria bacteria")
    
    def test_5(self):
        self.assertEqual(keyboard_shortcut("You gotta copy something Ctrl + V first my Ctrl + V guy"), "You gotta copy something first my guy")
    
    def test_6(self):
        self.assertEqual(keyboard_shortcut("You gotta paste at Ctrl + C some point my Ctrl + C guy"), "You gotta paste at some point my guy")
    
if __name__ == "__main__":
    unittest.main()