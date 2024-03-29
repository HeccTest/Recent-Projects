/* Project

    Bessie the cow is working on an essay for her writing class. Since her handwriting is quite bad, she decides to type the essay using a word processor. The essay contains N words (1≤N≤100), separated by spaces. Each word is between 1 and 15 characters long, inclusive, and consists only of uppercase or lowercase letters.

    According to the instructions for the assignment, the essay has to be formatted in a very specific way: each line should contain no more than K (1≤K≤80) characters, not counting spaces. Fortunately, Bessie's word processor can handle this requirement, using the following strategy:

    If Bessie types a word, and that word can fit on the current line, put it on that line. Otherwise, put the word on the next line and continue adding to that line. Of course, consecutive words on the same line should still be separated by a single space. There should be no space at the end of any line.

    Unfortunately, Bessie's word processor just broke. Please help her format her essay properly!

    You will be given n, k, and the string e.

* Example

    wordprocessor(10, 7  "hello my name is Bessie and this is my essay") ➞
        "hello my
        name is
        Bessie
        and this
        is my
        essay"

* Links

    https://edabit.com/challenge/tJNLCKPzNg3e9Whdt

* Notes

    - You'll need to return a string with a new line after every line, there should be no spaces after or before each line.

* Thoughts

    - need a clear definition of when a line ends, and consequently, when a new line begins
    - I am going to assume there is no one word that has length greater than k. Because there has been no specification as to what to do in this case.

*/

package veryHard.wordProcessor;

public class Challenge {
    public static String wordprocessor(int n, int k, String e) {
        // n = num of words
        // k = num of characters in one line, excluding spaces.
        String[] words = e.split(" ");
        int CurrLine = words[0].length();
        String processedWords = words[0];

        for (int i = 1; i < n; i++) {
            CurrLine += words[i].length();

            // word is too long, move to next line
            if (CurrLine > k) {
                CurrLine = words[i].length();
                processedWords += "\n" + words[i];
            }
            // word is valid for current line
            else {
                processedWords += " " + words[i];
            }
        }

        return (processedWords);
    }
}

// tested Sept. 22, 2023