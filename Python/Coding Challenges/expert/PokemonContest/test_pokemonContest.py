from pokemonContest import pk_special_winner
import unittest

# a list of test cases taken from the edabit testing page. I modified the contents to be executable in my use case.

class testPokemonContest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(pk_special_winner(4, 14), 4)

    def test_2(self):
        self.assertEqual(pk_special_winner(71, 54), 71)

    def test_3(self):
        self.assertEqual(pk_special_winner(43, 44), -1)

    def test_4(self):
        self.assertEqual(pk_special_winner(83, 33), -1)

    def test_5(self):
        self.assertEqual(pk_special_winner(41, 45), 41)

    def test_6(self):
        self.assertEqual(pk_special_winner(5, 80), 80)

    def test_7(self):
        self.assertEqual(pk_special_winner(92, 51), 51)

    def test_8(self):
        self.assertEqual(pk_special_winner(27, 12), 12)

    def test_9(self):
        self.assertEqual(pk_special_winner(18, 72), -1)

    def test_10(self):
        self.assertEqual(pk_special_winner(17, 7), -1)

    def test_11(self):
        self.assertEqual(pk_special_winner(68, 6), 6)

    def test_12(self):
        self.assertEqual(pk_special_winner(60, 97), -1)

    def test_13(self):
        self.assertEqual(pk_special_winner(63, 74), -1)

    def test_14(self):
        self.assertEqual(pk_special_winner(81, 30), -1)

    def test_15(self):
        self.assertEqual(pk_special_winner(49, 37), 37)

    def test_16(self):
        self.assertEqual(pk_special_winner(24, 76), 76)

    def test_17(self):
        self.assertEqual(pk_special_winner(91, 82), 82)

    def test_18(self):
        self.assertEqual(pk_special_winner(34, 68), 34)

    def test_19(self):
        self.assertEqual(pk_special_winner(63, 51), -1)

    def test_20(self):
        self.assertEqual(pk_special_winner(90, 17), -1)

    def test_21(self):
        self.assertEqual(pk_special_winner(61, 65), -1)

    def test_22(self):
        self.assertEqual(pk_special_winner(31, 40), -1)

    def test_23(self):
        self.assertEqual(pk_special_winner(20, 3), -1)

    def test_24(self):
        self.assertEqual(pk_special_winner(58, 69), 58)

    def test_25(self):
        self.assertEqual(pk_special_winner(87, 65), -1)

    def test_26(self):
        self.assertEqual(pk_special_winner(92, 47), 92)

    def test_27(self):
        self.assertEqual(pk_special_winner(71, 66), 71)

    def test_28(self):
        self.assertEqual(pk_special_winner(9, 62), -1)

    def test_29(self):
        self.assertEqual(pk_special_winner(85, 17), -1)

    def test_30(self):
        self.assertEqual(pk_special_winner(1, 33), 33)

    def test_31(self):
        self.assertEqual(pk_special_winner(12, 13), 12)

    def test_32(self):
        self.assertEqual(pk_special_winner(52, 9), -1)

    def test_33(self):
        self.assertEqual(pk_special_winner(87, 14), -1)

    def test_34(self):
        self.assertEqual(pk_special_winner(33, 28), 28)

    def test_35(self):
        self.assertEqual(pk_special_winner(77, 52), -1)

    def test_36(self):
        self.assertEqual(pk_special_winner(19, 78), -1)

    def test_37(self):
        self.assertEqual(pk_special_winner(24, 89), -1)

    def test_38(self):
        self.assertEqual(pk_special_winner(72, 99), -1)

    def test_39(self):
        self.assertEqual(pk_special_winner(77, 18), -1)

    def test_40(self):
        self.assertEqual(pk_special_winner(25, 44), 44)

    def test_41(self):
        self.assertEqual(pk_special_winner(57, 51), -1)

    def test_42(self):
        self.assertEqual(pk_special_winner(60, 22), -1)

    def test_43(self):
        self.assertEqual(pk_special_winner(36, 65), -1)

    def test_44(self):
        self.assertEqual(pk_special_winner(98, 34), 98)

    def test_45(self):
        self.assertEqual(pk_special_winner(26, 12), 26)

    def test_46(self):
        self.assertEqual(pk_special_winner(51, 56), -1)

    def test_47(self):
        self.assertEqual(pk_special_winner(59, 94), -1)

    def test_48(self):
        self.assertEqual(pk_special_winner(70, 44), -1)

    def test_49(self):
        self.assertEqual(pk_special_winner(67, 13), 13)

    def test_50(self):
        self.assertEqual(pk_special_winner(31, 33), 31)

    def test_51(self):
        self.assertEqual(pk_special_winner(37, 85), -1)

    def test_52(self):
        self.assertEqual(pk_special_winner(3, 86), 3)

    def test_53(self):
        self.assertEqual(pk_special_winner(96, 71), 96)

    def test_54(self):
        self.assertEqual(pk_special_winner(93, 34), 34)

    def test_55(self):
        self.assertEqual(pk_special_winner(63, 99), -1)

    def test_56(self):
        self.assertEqual(pk_special_winner(69, 65), 65)

    def test_57(self):
        self.assertEqual(pk_special_winner(41, 8), -1)

    def test_58(self):
        self.assertEqual(pk_special_winner(13, 53), -1)

    def test_59(self):
        self.assertEqual(pk_special_winner(84, 35), -1)

    def test_60(self):
        self.assertEqual(pk_special_winner(73, 70), -1)

    def test_61(self):
        self.assertEqual(pk_special_winner(84, 70), 84)

    def test_62(self):
        self.assertEqual(pk_special_winner(72, 14), 72)

    def test_63(self):
        self.assertEqual(pk_special_winner(74, 22), 74)

    def test_64(self):
        self.assertEqual(pk_special_winner(61, 90), -1)

    def test_65(self):
        self.assertEqual(pk_special_winner(6, 46), 6)

    def test_66(self):
        self.assertEqual(pk_special_winner(58, 77), -1)

    def test_67(self):
        self.assertEqual(pk_special_winner(39, 46), -1)

    def test_68(self):
        self.assertEqual(pk_special_winner(79, 20), -1)

    def test_69(self):
        self.assertEqual(pk_special_winner(72, 68), 72)

    def test_70(self):
        self.assertEqual(pk_special_winner(80, 98), -1)

    def test_71(self):
        self.assertEqual(pk_special_winner(42, 97), 97)

    def test_72(self):
        self.assertEqual(pk_special_winner(26, 19), -1)

    def test_73(self):
        self.assertEqual(pk_special_winner(65, 35), -1)

    def test_74(self):
        self.assertEqual(pk_special_winner(12, 65), 12)

    def test_75(self):
        self.assertEqual(pk_special_winner(35, 49), -1)

    def test_76(self):
        self.assertEqual(pk_special_winner(58, 89), -1)
        
    def test_77(self):
        self.assertEqual(pk_special_winner(18, 67), 18)

    def test_78(self):
        self.assertEqual(pk_special_winner(75, 69), 69)

    def test_79(self):
        self.assertEqual(pk_special_winner(2, 4), 4)

    def test_80(self):
        self.assertEqual(pk_special_winner(83, 49), 83)

    def test_81(self):
        self.assertEqual(pk_special_winner(11, 57), -1)

    def test_82(self):
        self.assertEqual(pk_special_winner(56, 87), 56)

    def test_83(self):
        self.assertEqual(pk_special_winner(33, 17), -1)

    def test_84(self):
        self.assertEqual(pk_special_winner(79, 96), -1)

    def test_85(self):
        self.assertEqual(pk_special_winner(33, 4), -1)

    def test_86(self):
        self.assertEqual(pk_special_winner(80, 77), 80)

    def test_87(self):
        self.assertEqual(pk_special_winner(52, 57), 57)

    def test_88(self):
        self.assertEqual(pk_special_winner(68, 26), -1)

    def test_89(self):
        self.assertEqual(pk_special_winner(9, 38), 9)

    def test_90(self):
        self.assertEqual(pk_special_winner(99, 42), -1)

    def test_91(self):
        self.assertEqual(pk_special_winner(61, 86), -1)

    def test_92(self):
        self.assertEqual(pk_special_winner(51, 22), 22)

    def test_93(self):
        self.assertEqual(pk_special_winner(21, 77), -1)

    def test_94(self):
        self.assertEqual(pk_special_winner(32, 26), -1)

    def test_95(self):
        self.assertEqual(pk_special_winner(73, 47), 73)

    def test_96(self):
        self.assertEqual(pk_special_winner(29, 92), 92)

    def test_97(self):
        self.assertEqual(pk_special_winner(7, 37), 7)

    def test_98(self):
        self.assertEqual(pk_special_winner(12, 63), 12)

    def test_99(self):
        self.assertEqual(pk_special_winner(53, 88), -1)

    def test_100(self):
        self.assertEqual(pk_special_winner(34, 60), 60)

if __name__ == "__main__":
    unittest.main()