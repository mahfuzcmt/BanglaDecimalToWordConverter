import unittest

from BanglaDecimalToWordConverter import DecimalToWord

decimal_to_word = DecimalToWord()


class TestCases(unittest.TestCase):

    def test9(self):
        self.assertEqual(decimal_to_word.convertAmount(1234567.08, False, False, 'bng'), 'বার লক্ষ চৌত্রিশ হাজার পাঁচ শত সাতষট্টি টাকা এবং আট পয়সা মাত্র')

    def test8(self):
        self.assertEqual(decimal_to_word.convertAmount(718265.04, False, False, 'bng'),'সাত লক্ষ আঠারো হাজার দুই শত পঁয়ষট্টি টাকা এবং চার পয়সা মাত্র')

    def test7 (self):
        self.assertEqual(decimal_to_word.convertAmount(98769.27, False, False, 'bng'),'আটানব্বই হাজার সাত শত উনসত্তুর টাকা এবং সাতাশ পয়সা মাত্র')

    def test6 (self):
        self.assertEqual(decimal_to_word.convertAmount(1782.19, False, False, 'bng'), 'এক হাজার সাত শত বিরাশি টাকা এবং উনিশ পয়সা মাত্র')

    def test5 (self):
        self.assertEqual(decimal_to_word.convertAmount(769.96, False, False, 'bng'), 'সাত শত উনসত্তুর টাকা এবং ছিয়ানব্বই পয়সা মাত্র')

    def test4 (self):
        self.assertEqual(decimal_to_word.convertAmount(88.07, False, False, 'bng'), 'অষ্টআশি টাকা এবং সাত পয়সা মাত্র')


    def test3(self):
        self.assertEqual(decimal_to_word.convertAmount(8.65, False, False, 'bng'), 'আট টাকা এবং পঁয়ষট্টি পয়সা মাত্র')

    def test2(self):
        self.assertEqual(decimal_to_word.convertAmount(6, False, False, 'bng'), 'ছয় টাকা এবং শূন্য পয়সা মাত্র')

    def test1(self):
        self.assertEqual(decimal_to_word.convertAmount(0.18, False, False, 'bng'), 'শূন্য টাকা এবং আঠারো পয়সা মাত্র')




if __name__ == '__main__':
    unittest.main()

