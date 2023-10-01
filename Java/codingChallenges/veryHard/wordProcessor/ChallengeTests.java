package veryHard.wordProcessor;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class ChallengeTests {
    @Test
    public void test1() {
        assertEquals("hello my\nname is\nBessie\nand this\nis my\nessay",
                Challenge.wordprocessor(10, 7, "hello my name is Bessie and this is my essay"));
    }

    @Test
    public void test2() {
        assertEquals("college students\nin the USA are\neligible for\nselection as\nfinalists",
                Challenge.wordprocessor(11, 16, "college students in the USA are eligible for selection as finalists"));
    }
}