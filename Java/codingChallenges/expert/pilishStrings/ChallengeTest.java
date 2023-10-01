package expert.pilishStrings;

/**
 *
 * @author edwardclark
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class ChallengeTest {
    @Test
    public void test1() {
        assertEquals("FOR A LOOP", Challenge.pilish_string("FORALOOP"));
    }

    @Test
    public void test2() {
        assertEquals("CAN I MAKE A GUESS", Challenge.pilish_string("CANIMAKEAGUESS"));
    }

    @Test
    public void test3() {
        assertEquals("CAN I MAKE A GUESS NOWWWWWWW", Challenge.pilish_string("CANIMAKEAGUESSNOW"));
    }

    @Test
    public void test4() {
        assertEquals("XXX", Challenge.pilish_string("X"));
    }

    @Test
    public void test5() {
        assertEquals("ARA N DOMS E QUENC EOFLETTER SS", Challenge.pilish_string("ARANDOMSEQUENCEOFLETTERS"));
    }

    @Test
    public void test6() {
        assertEquals("", Challenge.pilish_string(""));
    }

    @Test
    public void test7() {
        assertEquals("333 1 4444 1 55555 999999999 22 666666 55555 333 55555 88888888 999999999 7777777 999999999",
                Challenge.pilish_string(
                        "33314444155555999999999226666665555533355555888888889999999997777777999999999"));
    }

    @Test
    public void test8() {
        assertEquals("### * @@@@", Challenge.pilish_string("###*@"));
    }

    @Test
    public void test9() {
        assertEquals("... . .... . .....", Challenge.pilish_string(".........."));
    }

    @Test
    public void test10() {
        assertEquals("Now I fall A tired suburbian In liquid under the trees Drifting alongside forests simmmmmmm",
                Challenge.pilish_string("NowIfallAtiredsuburbianInliquidunderthetreesDriftingalongsideforestssimm"));
    }

    @Test
    public void test11() {
        assertEquals("HOW I NEED A DRINK ALCOHOLIC IN NATURE AFTER THE HEAVY LECTURES INVOLVING QUANTUM MECHANICS",
                Challenge.pilish_string(
                        "HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYLECTURESINVOLVINGQUANTUMMECHANICSANDALLTHESECRETSOFTHEUNIVERSE"));
    }

    @Test
    public void test12() {
        assertEquals("HOW I NEED A DRINK ALCOHOLIC IN NATURE AFTER THE HEAVY CODINGGG",
                Challenge.pilish_string("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYCODING"));
    }
}