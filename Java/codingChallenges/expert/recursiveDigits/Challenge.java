/* Project

    We define super digit of an integer x using the following rules:

    - If x has only 1 digit, then its super digit is x.
    - Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

    For example, the super digit of x will be calculated as:

        superDigit(9875)    9+8+7+5 = 29 
        superDigit(29)      2 + 9 = 11
        superDigit(11)      1 + 1 = 2
        superDigit(2) = 2

    You are given two numbers n and k. The number p is created by concatenating the string n, k times. Continuing the above example where n = 9875, assume your value k=4. Your initial p = 9875 9875 9875 9875 (spaces added for clarity).

        superDigit(p) = superDigit(9875987598759875)
        5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116

        superDigit(p) = superDigit(116)
        1+1+6 = 8

        superDigit(p) = superDigit(8)

    All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it's the super digit.

    Complete the superDigit() method. It must return the calculated super digit as an integer.

    superDigit has the following parameter(s):

        n: a string representation of an integer.
        k: an integer, the times to concatenate n to make p.

* Example

    superDigit("148", 3) ➞ 3

    superDigit("123", 3) ➞ 9

    superDigit("99999999999999999999999999", 104500) ➞ 9

* Links

    https://edabit.com/challenge/ABgaWqqn2XDjBqwKy

* Notes

    Each problem must be solved in less than 1 second.

* Thoughts

    - time is a concern.
    - lots of casting to String and back to int? Try to minimize.
    - base case:
        - currently looking at a string with length() == 1 or an integer with value < 10
        - recursion may not be necessary
    - going to assume no negative numbers for now

*/

package expert.recursiveDigits;

public class Challenge {
    public static int superDigit(String n, int k) {
        n = findSuperDigit(n);
        n = n.repeat(k);
        n = findSuperDigit(n);

        return (Integer.parseInt(n));
    }

    public static String findSuperDigit(String n) {
        while (n.length() > 1) {
            int newNum = 0;
            for (int i = 0; i < n.length(); i++) {
                newNum += Integer.parseInt(n.substring(i, i + 1));
            }
            n = Integer.toString(newNum);
        }

        return (n);
    }
}

/* first run works, but is inefficient. Completing test 1 in 1.3s, where requirement is to complete test in < 1000ms. Work on improving efficiency.

    code at first run:

        n = n.repeat(k);
        while (n.length() > 1) {
            int newNum = 0;
            for (int i = 0; i < n.length(); i++) {
                newNum += Integer.parseInt(n.substring(i, i + 1));
            }
            n = Integer.toString(newNum);
        }
        System.out.println(n);
        return (Integer.parseInt(n));
    
*/

// revised code works more efficiently. It finds the super digit of n, then duplicates n, k num of times. Then finds the super digit of the new string. This solution is sufficient in solving the problem in less than 1000 ms.
// tested Sept. 30, 2023. Approx. 30 min from reading question to completion.