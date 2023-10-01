/* Project

   Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num until the array length reaches length.

* Example

   arrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]

   arrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

   arrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

* Links

   https://edabit.com/challenge/rzpucPyoyEtXPo2BG

* Notes

   Notice that num is also included in the returned array.

*/
package arrayofMultiples;

public class Program {
   public static int[] arrayOfMultiples(int num, int length) {
      int[] returnList = new int[length];
      for (int i = 0; i < length; i++) {
         returnList[i] = num * (i + 1);
         System.out.println(returnList[i]);
      }
      return (returnList);
   }
}

// tested Sept. 1, 2023

/*
 * testing notes for future reference (specifically for VS Code):
 *    copy test cases from edabit
 *    create a java file for test cases
 *    go to left column, find the "testing" tab, and enable tests for java
 */