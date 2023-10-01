/* Project

    Create a function that takes an array of numbers and return "Boom!" if the digit 7 appears in the array. Otherwise, return "there is no 7 in the array".

* Example

    sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!"
    // 7 contains the number seven.

    sevenBoom([8, 6, 33, 100]) ➞ "there is no 7 in the array"
    // None of the items contain 7 within them.

    sevenBoom([2, 55, 60, 97, 86]) ➞ "Boom!"
    // 97 contains the number seven.

* Links

    https://edabit.com/challenge/CKqfEowjmSTw2jsso

* Notes

    N/A

* Thoughts

    - two possible outputs: "Boom!" or "there is no 7 in the array"
    - unsorted list
    - check each item linearly, and check all characters for any 7's
        - I could unconditionally convert to string, and check character by character for 7's (most expensive solution)
        - maybe some formula, ie. if number is divisble by 7, that means there is a 7 in the number (this is a made up example)

*/

package hard.sevenBoom;

public class Challenge {
    public static String sevenBoom(int[] arr) {
        for (int i = 0; i < arr.length; i++) { // iterate through entire array
            if (String.valueOf(arr[i]).contains("7")) { // if an item in the array, casted to string. Contains a "7"
                return ("Boom!");
            }
        }
        return ("there is no 7 in the array");
    }
}

// tested Sept. 2, 2023. I took the simplest solution, there may be a more efficient solution.