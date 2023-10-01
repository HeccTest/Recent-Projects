/* Project

    In this challenge, transform a string into a series of words (or sequences of characters) separated by a single space, with each word having the same length given by the first 15 digits of the decimal representation of Pi:

    3.14159265358979

    If a string contains more characters than the total quantity given by the sum of the Pi digits, the unused characters are discarded and you will use only those needed to form 15 words.

    Also if a string contains less characters than the total quantity given by the sum of the Pi digits, in any case you have to respect the sequence of the digits to obtain the words.

    If the letters contained in the string don't match exactly the digits, in this case you will repeat the last letter until the word will have the correct length.

    If the given string is empty, an empty string has to be returned.

    Given a string txt, implement a function that returns the same string formatted accordingly to the above instructions.

* Example

    pilish_string("33314444") ➞ "333 1 4444"
    // 3.14

    pilish_string("TOP") ➞ "TOP"
    // 3

    pilish_string("X")➞ "XXX"
    // "X" has to match the same length of the first digit (3)
    // The last letter of the word is repeated

    pilish_string("")➞ ""

* Links

    https://edabit.com/challenge/Fy2ySuj6XK5mxrsgR

* Notes

    This challenge is a simplified concept inspired by the Pilish, a peculiar type of constrained writing that uses all the known possible digits of Pi. A potentially infinite text can be written allowing punctuation and a set of additional rules, that permits to avoid long sequences of small digits, substituting them with words bigger than 9 letters and making so appear the composition more similar to a free-verse poem.
    
    The dot that separes the integer part of Pi from the decimal part hasn't to be considered in the function: it's present in Instructions and Examples only for readability.

* Thoughts

    - run until the first 15 digits of Pi are accounted for, or until string is empty.
        - iterate through at most 15 times, and at minimum 0 times (empty string)
        - each iteration will substring the appropriate number of characters from the string. and delete them from our shallow copy of the input.
    - ensure base case empty string is accounted for
    - repeat last char if string is shorter than the current Pi digit.

*/

package expert.pilishStrings;

public class Challenge {
    public static String pilish_string(String s) {
        int[] piDigits = { 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9 };
        String result = "";
        int iterator = 0;

        while (iterator < 15 && !(s.equals(""))) {
            try {
                result += s.substring(0, piDigits[iterator]) + " "; // take pi digits at the front, append to results with an empty space at the end
                s = s.substring(piDigits[iterator]); // s is now the remaining string
                iterator++;
            } catch (Exception e) { // if string index out of bounds. not enough characters in s to substring pidigits.
                result += s;
                int extraChar = piDigits[iterator] - s.length(); // find how many extra digits
                result += (s.substring(s.length() - 1)).repeat(extraChar); // append the last char, (extraChar) times.
                return (result);
            }
        }

        if (iterator > 0) { // if result is non-empty
            result = result.substring(0, result.length() - 1); // remove the last char which is an empty space I added.
        }
        return (result);
    }
}

//  tested Sept. 28, 2023. Took about 50 mins from reading question to completion.