package veryHard.piggyBank;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class ChallengeTests {
    @Test
    public void test1() {
        assertEquals(53, Challenge.NumberOfDays(2050, 1200, 10));
    }

    @Test
    public void test2() {
        assertEquals(123, Challenge.NumberOfDays(10000, 2500, 50));
    }

    @Test
    public void test3() {
        assertEquals(75, Challenge.NumberOfDays(3333, 1111, 22));
    }

    @Test
    public void test4() {
        assertEquals(97, Challenge.NumberOfDays(1000, 100, 0));
    }

    @Test
    public void test5() {
        assertEquals(409, Challenge.NumberOfDays(19999, 5000, 5));
    }

    @Test
    public void test6() {
        assertEquals(4, Challenge.NumberOfDays(500, 300, 50));
    }

    @Test
    public void test7() {
        assertEquals(2, Challenge.NumberOfDays(7000, 6500, 250));
    }
}