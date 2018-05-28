import unittest

from BanglaDecimalToWordConverter import DecimalToWord

decimal_to_word = DecimalToWord()


class TestCases(unittest.TestCase):

    def bng_test10(self):
        self.assertEqual(decimal_to_word.convertAmount(97779101873517.89),'সাতানব্বই লক্ষ সাতাত্তর হাজার নয় শত দশ কোটি আঠারো লক্ষ তেহাত্তুর হাজার পাঁচ শত সতেরো টাকা এবং ঊনানব্বুই পয়সা মাত্র')

    def bng_test9(self):
        self.assertEqual(decimal_to_word.convertAmount(1234567.08), 'বার লক্ষ চৌত্রিশ হাজার পাঁচ শত সাতষট্টি টাকা এবং আট পয়সা মাত্র')

    def bng_test8(self):
        self.assertEqual(decimal_to_word.convertAmount(718265.04),'সাত লক্ষ আঠারো হাজার দুই শত পঁয়ষট্টি টাকা এবং চার পয়সা মাত্র')

    def bng_test7 (self):
        self.assertEqual(decimal_to_word.convertAmount(98769.27),'আটানব্বই হাজার সাত শত উনসত্তুর টাকা এবং সাতাশ পয়সা মাত্র')

    def bng_test6 (self):
        self.assertEqual(decimal_to_word.convertAmount(1782.19), 'এক হাজার সাত শত বিরাশি টাকা এবং উনিশ পয়সা মাত্র')

    def bng_test5 (self):
        self.assertEqual(decimal_to_word.convertAmount(769.96), 'সাত শত উনসত্তুর টাকা এবং ছিয়ানব্বই পয়সা মাত্র')

    def bng_test4 (self):
        self.assertEqual(decimal_to_word.convertAmount(88.07), 'অষ্টআশি টাকা এবং সাত পয়সা মাত্র')


    def bng_test3(self):
        self.assertEqual(decimal_to_word.convertAmount(8.65), 'আট টাকা এবং পঁয়ষট্টি পয়সা মাত্র')

    def bng_test2(self):
        self.assertEqual(decimal_to_word.convertAmount(6), 'ছয় টাকা এবং শূন্য পয়সা মাত্র')

    def bng_test1(self):
        self.assertEqual(decimal_to_word.convertAmount(0.18), 'শূন্য টাকা এবং আঠারো পয়সা মাত্র')





if __name__ == '__main__':
    unittest.main()


#
# class Test():
#     d_to_w = DecimalToWord()
#     first_input = .18
#     sec_input = 6
#     third_input = 8.65
#     fourth_input = 88.07
#     fiveth_input = 769.96
#     sixth_input = 1782.19
#     seventh_input = 98769.27
#     eightth_input = 718265.04
#     nineth_input = 1234567.08
#     tenth_input = 97779101873517.89
#
#     wrong = 2.1
#
#     #amountinword = d_to_w.convertAmount(first_input)
#
#     print('input : %s >>  output :%s ' % (first_input, d_to_w.convertAmount(first_input)))
#     print('input : %s >>  output :%s ' % (sec_input, d_to_w.convertAmount(sec_input)))
#     print('input : %s >>  output :%s ' % (third_input, d_to_w.convertAmount(third_input)))
#     print('input : %s >>  output :%s ' % (fourth_input, d_to_w.convertAmount(fourth_input)))
#     print('input : %s >>  output :%s ' % (fiveth_input, d_to_w.convertAmount(fiveth_input)))
#
#
#     print('input : %s >>  output :%s ' % (sixth_input, d_to_w.convertAmount(sixth_input)))
#     print('input : %s >>  output :%s ' % (seventh_input, d_to_w.convertAmount(seventh_input)))
#     print('input : %s >>  output :%s ' % (eightth_input, d_to_w.convertAmount(eightth_input)))
#     print('input : %s >>  output :%s ' % (nineth_input, d_to_w.convertAmount(nineth_input)))
#     print('input : %s >>  output :%s ' % (wrong, d_to_w.convertAmount(wrong)))
#
#     print('input : %s >>  output :%s ' % (wrong, d_to_w.convertAmount(wrong)))
