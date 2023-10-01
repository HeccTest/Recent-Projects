/* Project

    You have a pack of 5 randomly numbered cards, which can range from 0-9. You can win if you can produce a higher two-digit number from your cards than your opponent. Return true if your cards win that round.

* Example

    winRound([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ true
    // Your cards can make the number 96
    // Your opponent can make the number 73
    // You win the round since 96 > 73

    winRound([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ true

    winRound([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]) ➞ false

    winRound([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]) ➞ false

* Links

    https://edabit.com/challenge/qE9gCJtrtcMurvQtT

* Notes

    Return false if you and your opponent reach the same maximum number (see example #4).

* Thoughts

    - if player wins, return true. Otherwise (player lose, or tie), return false.
        - player wins by having the first array form higher number value
    - highest possible card values can be found by putting the highest value card, followed by the second highest valued card.

*/

package hard.numberedCards;

public class NumberedCard {
    public static boolean winRound(int[] you, int[] opp) {
        if (highestCombination(you) > highestCombination(opp)) {
            return (true);
        } else {
            return (false);
        }
    }

    public static int highestCombination(int[] cards) {
        int highestCard = 0;
        int ignoredIndex = 0;
        for (int j = 0; j < cards.length; j++) {
            if (cards[j] > highestCard) {
                highestCard = cards[j];
                ignoredIndex = j;
            }
        }

        int combination = highestCard * 10;

        highestCard = 0;
        for (int j = 0; j < cards.length; j++) {
            if (cards[j] > highestCard && j != ignoredIndex) {
                highestCard = cards[j];
            }
        }

        combination += highestCard;

        return (combination);
    }
}

// tested Sept. 4, 2023.