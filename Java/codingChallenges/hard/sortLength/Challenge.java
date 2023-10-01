/* Project

    Create a function that takes a string and returns a string ordered by the length of the words. From shortest to longest word. If there are words with the same amount of letters, order them alphabetically.

* Example

    sortByLength("Hello my friend") ➞ "my Hello friend"

    sortByLength("Have a wonderful day") ➞ "a day Have wonderful"

    sortByLenght("My son loves pineapples") ➞ "My son loves pineapples"

* Links

    https://edabit.com/challenge/6RStzK9uub9vHDt53

* Notes

    Punctuation (periods, commas, etc) belongs to the word in front of it.

* Thoughts

    - split string by spaces (" ")
        - put these strings in an arraylist
        - linearly iterate through arraylist, finding string with smallest length
            - if multiple string of shortest length exist, sort alphabetically.
        - append this shortest string to a new string. Delete from array.
    - probably could also have an array, and sort by size (ie. move smallest to front), then print the entire array one by one, separated by spaces.
        - this makes it so that I do not have to use an arraylist (less resource intensive)

*/

package hard.sortLength;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Challenge {
    public static String sortByLength(String str) {
        List<String> words = new ArrayList<String>(Arrays.asList(str.split(" ")));
        String sortedString = "";
        while (words.size() > 0) // while list is non-empty
        {
            // find the first occurrence of the shortest string. That is, another string of equal length, will not overwrite the current shortest.
            int currShortest = words.get(0).length();
            int shortestIndex = 0;
            for (int i = 0; i < words.size(); i++) {
                if (currShortest > words.get(i).length()) {
                    currShortest = words.get(i).length();
                    shortestIndex = i;
                } else if (currShortest == words.get(i).length()) {
                    // going to compare the two and the one that comes first alphabetically will be deemed the shortest. Capitalization may conflict (need clarification on how capital letters should interact)
                    // I will treat all strings as lower case, for comparison purposes, as that is what the test results seem to point towards.
                    if (words.get(shortestIndex).toLowerCase().compareTo(words.get(i).toLowerCase()) > 1) {
                        // if the current shortest string compared the new found shortest string has a positive comparison, it means, the new found string occurs earlier, alphebetically.
                        shortestIndex = i;
                    }
                }
            }
            sortedString += " " + words.get(shortestIndex); // append to new string
            words.remove(shortestIndex); // remove current shortest from arraylist
        }
        return (sortedString.substring(1)); // return the sorted string, excluding the first character (which is an added space)
    }
}

// tested Sept. 2, 2023. Took a little longer than expected, due to not reading instructions fully (did not realise I was sorting alphabetically when equal length). Additionally, instructions were slightly ambiguous on what to do with capital letters when sorting alphabetically.