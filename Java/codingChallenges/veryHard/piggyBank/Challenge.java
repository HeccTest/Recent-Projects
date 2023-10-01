/* Project

    John wants to save money for his first car. He puts money in his piggy bank every day. Every day, he puts in $1 more than the previous day. Every Monday he starts with a new value ⁠— $1 more than the previous Monday.

    Week 1 (starting at $1)
    Day	Amount	Sum
    Monday	$1	$1
    Tuesday	$2	$3
    Wednesday	$3	$6
    Thursday	$4	$10
    Friday	$5	$15
    Saturday	$6	$21
    Sunday	$7	$28

    Week 2
    Day	Amount	Sum
    Monday	$2	$30
    Tuesday	$3	$33
    Wednesday	$4	$37
    etc ...

    Write a function that returns the number of days he needs to buy his first car cost. John had some savings (include it before counting). On the first Monday, he puts the start amount into his piggy bank.

* Example

    Challenge.NumberOfDays(2050, 1200, 10) ➞ 53
    // 2050: cost of car, 1200: savings, 10: start amount 
    // After 53 days he can buy a car.

    Challenge.NumberOfDays(10000, 2500, 50) ➞ 123
    // After 123 days he can buy a car.

    Challenge.NumberOfDays(500, 300, 50) ➞ 4
    // After 4 days he can buy a car.

* Links

    https://edabit.com/challenge/JLQ4upWrq5LkzdhPE

* Notes

    - The first day is always Monday.
    - To buy a car, he needs money greater than or equal to cost.
    - All given numbers will be greater than 0.
    - BONUS: Try not adding the sum every day!

* Thoughts

    - while savings is less than cost, we will continue.

*/

package veryHard.piggyBank;

public class Challenge {
    public static int NumberOfDays(int cost, int savings, int start) {
        int daysPassed = 1;
        int supplement = 0;
        while (savings < cost) {
            savings += start + supplement;

            if (savings < cost) { // not enough savings, we will continue saving
                supplement += 1;
                if (daysPassed % 7 == 0) { // if we're at the end of the week
                    start += 1; // incrementing the starting amount, next week starts at 1 dollar more than the previous.
                    supplement = 0;
                }
                daysPassed += 1;
            }
        }

        return (daysPassed);
    }
}

// tested Sept. 5, 2023. Took longer than expected (about 40 min testing, based on the test run times), because I was incrementing days and supplement amount, then resetting at inaccurate times. Moved them around, and only reset when appropriate now.
