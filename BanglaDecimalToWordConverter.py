#!/usr/bin/env python3.6


class DecimalToWords():
    def __init__(self):

        self.iWords = ['zero', ' one', ' two', ' three', ' four', ' five', ' six', ' seven', ' eight', ' nine']
        self.ePlace = ['ten', ' eleven', ' twelve', ' thirteen', ' fourteen', ' fifteen', ' sixteen', ' seventeen',
                       'eighteen', 'nineteen']

        self.tensPlace = ['', ' ten', ' twenty', ' thirty', ' forty', ' fifty', ' sixty', ' seventy', ' eighty',
                          ' ninety']
        self.inWords = list()

        self.numReversed = list()
        self.actnumber = list()
        self.i = 0
        self.j = 0

        self.taka_in_word = ''
        self.paisa_in_word = ''
        self.amountInWord = ''

        self.eng_to_bng = {}
        self.eng_to_bng[''] = ''
        self.eng_to_bng['zero'] = 'শূন্য'
        self.eng_to_bng['one'] = 'এক'
        self.eng_to_bng['two'] = 'দুই'
        self.eng_to_bng['three'] = 'তিন'
        self.eng_to_bng['four'] = 'চার'
        self.eng_to_bng['five'] = 'পাঁচ'
        self.eng_to_bng['six'] = 'ছয়'
        self.eng_to_bng['seven'] = 'সাত'
        self.eng_to_bng['eight'] = 'আট'
        self.eng_to_bng['nine'] = 'নয়'
        self.eng_to_bng['ten'] = 'দশ'

        self.eng_to_bng['eleven'] = 'এগার'
        self.eng_to_bng['twelve'] = 'বার'
        self.eng_to_bng['thirteen'] = 'তের'
        self.eng_to_bng['fourteen'] = 'চৌদ্দ'
        self.eng_to_bng['fifteen'] = 'পনের'
        self.eng_to_bng['sixteen'] = 'ষোল'
        self.eng_to_bng['seventeen'] = 'সতেরো'
        self.eng_to_bng['eighteen'] = 'আঠারো'
        self.eng_to_bng['nineteen'] = 'উনিশ'

        self.eng_to_bng['twenty'] = 'বিশ'
        self.eng_to_bng['twenty one'] = 'একুশ'
        self.eng_to_bng['twenty two'] = 'বাইশ'
        self.eng_to_bng['twenty three'] = 'তেইশ'
        self.eng_to_bng['twenty four'] = 'চব্বিশ'
        self.eng_to_bng['twenty five'] = 'পঁচিশ'
        self.eng_to_bng['twenty six'] = 'ছাব্বিশ'
        self.eng_to_bng['twenty seven'] = 'সাতাশ'
        self.eng_to_bng['twenty eight'] = 'আটাশ'
        self.eng_to_bng['twenty nine'] = 'ঊনত্রিশ'

        self.eng_to_bng['thirty'] = 'ত্রিশ'
        self.eng_to_bng['thirty one'] = 'একত্রিশ'
        self.eng_to_bng['thirty two'] = 'বত্রিশ'
        self.eng_to_bng['thirty three'] = 'তেত্রিশ'
        self.eng_to_bng['thirty four'] = 'চৌত্রিশ'
        self.eng_to_bng['thirty five'] = 'পঁয়ত্রিশ'
        self.eng_to_bng['thirty six'] = 'ছত্তিরিশ'
        self.eng_to_bng['thirty seven'] = 'সাইত্রিশ'
        self.eng_to_bng['thirty eight'] = 'আটত্রিশ'
        self.eng_to_bng['thirty nine'] = 'ঊনচল্লিশ'

        self.eng_to_bng['fourty'] = 'চল্লিশ'
        self.eng_to_bng['forty one'] = 'একচল্লিশ'
        self.eng_to_bng['forty two'] = 'বেয়াল্লিশ'
        self.eng_to_bng['forty three'] = 'তেতাল্লিশ'
        self.eng_to_bng['forty four'] = 'চুয়াল্লিশ'
        self.eng_to_bng['forty five'] = 'পঁয়তাল্লিশ'
        self.eng_to_bng['forty six'] = 'ছেচল্লিশ'
        self.eng_to_bng['forty seven'] = 'সাতচল্লিশ'
        self.eng_to_bng['forty eight'] = 'আটচল্লিশ'
        self.eng_to_bng['forty nine'] = 'ঊনপঞ্চাশ'

        self.eng_to_bng['fifty'] = 'পঞ্চাশ'
        self.eng_to_bng['fifty one'] = 'একান্'
        self.eng_to_bng['fifty two'] = 'বায়ান্ন'
        self.eng_to_bng['fifty three'] = 'তেপ্পান্ন'
        self.eng_to_bng['fifty four'] = 'চুয়ান্ন'
        self.eng_to_bng['fifty five'] = 'পঞ্চান্ন'
        self.eng_to_bng['fifty six'] = 'ছাপ্পান্ন'
        self.eng_to_bng['fifty seven'] = 'সাতান্ন'
        self.eng_to_bng['fifty eight'] = 'আটান্ন'
        self.eng_to_bng['fifty nine'] = 'ঊনষাট'

        self.eng_to_bng['sixty'] = 'ষাট'
        self.eng_to_bng['sixty one'] = 'একষট্টি'
        self.eng_to_bng['sixty two'] = 'বাষট্টি'
        self.eng_to_bng['sixty three'] = 'তেষট্টি'
        self.eng_to_bng['sixty four'] = 'চৌষট্টি'
        self.eng_to_bng['sixty five'] = 'পঁয়ষট্টি'
        self.eng_to_bng['sixty six'] = 'ছেষট্টি'
        self.eng_to_bng['sixty seven'] = 'সাতষট্টি'
        self.eng_to_bng['sixty eight'] = 'আটষট্টি'
        self.eng_to_bng['sixty nine'] = 'উনসত্তুর'

        self.eng_to_bng['seventy'] = 'সত্তর'
        self.eng_to_bng['seventy one'] = 'একাত্তর'
        self.eng_to_bng['seventy twi'] = 'বাহাত্তর'
        self.eng_to_bng['seventy three'] = 'তেহাত্তুর'
        self.eng_to_bng['seventy four'] = 'চুয়াত্তর'
        self.eng_to_bng['seventy five'] = 'পচাত্তর'
        self.eng_to_bng['seventy six'] = 'ছিয়াত্তর'
        self.eng_to_bng['seventy seven'] = 'সাতাত্তর'
        self.eng_to_bng['seventy eight'] = 'আটাত্তর'
        self.eng_to_bng['seventy nine'] = 'উনাশি'

        self.eng_to_bng['eighty'] = 'আশি'
        self.eng_to_bng['eighty one'] = 'একাশি'
        self.eng_to_bng['eighty two'] = 'বিরাশি'
        self.eng_to_bng['eighty three'] = 'তিরাশি'
        self.eng_to_bng['eighty four'] = 'চুরাশি'
        self.eng_to_bng['eighty five'] = 'পঁচাশি'
        self.eng_to_bng['eighty six'] = 'ছিয়াশি'
        self.eng_to_bng['eighty seven'] = 'সাতাশি'
        self.eng_to_bng['eighty eight'] = 'অষ্টআশি'
        self.eng_to_bng['eighty nine'] = 'ঊনানব্বুই'

        self.eng_to_bng['ninety'] = 'নব্বই'
        self.eng_to_bng['ninety one'] = 'একানব্বই'
        self.eng_to_bng['ninety two'] = 'বিরানব্বই'
        self.eng_to_bng['ninety three'] = 'তিরানব্বই'
        self.eng_to_bng['ninety four'] = 'চুরানব্বই'
        self.eng_to_bng['ninety five'] = 'পঁচানব্বই'
        self.eng_to_bng['ninety six'] = 'ছিয়ানব্বই'
        self.eng_to_bng['ninety seven'] = 'সাতানব্বই'
        self.eng_to_bng['ninety eight'] = 'আটানব্বই'
        self.eng_to_bng['ninety nine'] = 'নিরানব্বই'

        self.bng_to_eng = {}
        self.bng_to_eng[''] = ''
        self.bng_to_eng['শূন্য'] = 'zero'

        self.bng_to_eng['শত'] = 'hundred'
        self.bng_to_eng['হাজার'] = 'thousand'
        self.bng_to_eng['লক্ষ'] = 'lakh'
        self.bng_to_eng['কোটি'] = 'crore'

        self.bng_to_eng['টাকা'] = 'taka'
        self.bng_to_eng['শূন্য টাকা'] = 'zero taka'

        self.bng_to_eng['শূন্য পয়সা মাত্র'] = 'zero paisa only'
        self.bng_to_eng['এবং'] = 'and'
        self.bng_to_eng['পয়সা মাত্র'] = 'paisa only'
        self.bng_to_eng['মাত্র'] = 'only'



    def tensComplication(self):
        if (self.actnumber[self.i] == 0):
            self.inWords.insert(self.j, '')
        elif (self.actnumber[self.i] == 1):
            self.inWords.insert(self.j, self.ePlace[self.actnumber[self.i - 1]])
        else:
            self.inWords.insert(self.j, self.tensPlace[self.actnumber[self.i]])

    def convertAmount(self, numericValue, is_ignorable_taka_if_zero, is_ignorable_paisa_if_zero, lng):
        numericValue = float(numericValue)
        taka, paisa = [str(num) for num in str(numericValue).split(".")]

        if len(str(paisa)) > 2:
            paisa = paisa[:2]

        if len(str(paisa)) == 1:
            str_paisa = str(paisa)
            str_paisa += '0'
            paisa = int(str_paisa)

        if len(str(paisa)) == 2 and str(paisa).startswith("0"):
            s_paisa = str(paisa)
            s_paisa = s_paisa[1:]
            paisa = int(s_paisa)

        tk_in_word = self.convert(taka)
        paisa = self.convert(paisa)

        if tk_in_word is not False:
            self.taka_in_word = tk_in_word + ' /টাকা/'

        if is_ignorable_taka_if_zero is False and tk_in_word is False:
            self.taka_in_word = 'শূন্য টাকা/ '

        if (is_ignorable_taka_if_zero is False or tk_in_word is not False) and (paisa is not False or is_ignorable_paisa_if_zero is False):
            self.taka_in_word += 'এবং/'

        if paisa is not False:
            self.paisa_in_word = paisa + '/পয়সা মাত্র'

        elif is_ignorable_paisa_if_zero is False and paisa is False:
            self.paisa_in_word = 'শূন্য পয়সা মাত্র'

        else:
            self.paisa_in_word = 'মাত্র'

        self.amountInWord = self.taka_in_word + self.paisa_in_word

        splited = self.amountInWord.split('/')
        splited = [x.strip(' ') for x in splited]

        final_amount_inword = " "
        for w in splited:
            try:
                if lng == 'bng':
                    final_amount_inword += " " + self.eng_to_bng[w]
                else:
                    final_amount_inword += " " + self.bng_to_eng[w]

            except Exception as e:
                final_amount_inword += " " + w

        return final_amount_inword.strip()

    def convert(self, numericValue):
        self.inWords = list()
        if (numericValue == 00 or numericValue == 0):
            return False

        numArray = [int(i) for i in str(numericValue)]

        numReversed = list(reversed(numArray))

        self.actnumber = numReversed
        self.actnumber.append("")

        if (int(numericValue) == 0):
            return False

        arr_length = len(numArray)
        finalWord = ''
        self.j = 0
        self.i = 0

        for c in range(arr_length):

            if (self.i == 0):
                inWords = ""
                if (self.actnumber[self.i] == 0 or self.actnumber[self.i + 1] == 1):
                    inWords = ""
                else:
                    inWords += self.iWords[self.actnumber[self.i]]
                self.inWords.insert(self.j, inWords + '')

            if (self.i == 1):
                self.tensComplication()

            if (self.i == 2):
                if (self.actnumber[self.i] == 0):
                    self.inWords.insert(self.j, '')
                elif (self.actnumber[self.i - 1] != 0 and self.actnumber[self.i - 2] != 0):
                    self.inWords.insert(self.j, self.iWords[self.actnumber[self.i]] + ' /শত/')
                else:
                    self.inWords.insert(self.j, self.iWords[self.actnumber[self.i]] + ' /শত/')

            if (self.i == 3):
                try:
                    inWords = ""
                    if (self.actnumber[self.i] == 0 or self.actnumber[self.i + 1] == 1):
                        inWords = ""
                    else:
                        inWords = self.iWords[self.actnumber[self.i]]

                    if (self.actnumber[self.i + 1] != 0 or self.actnumber[self.i] > 0):
                        self.inWords.insert(self.j, inWords + ' /হাজার/')
                except Exception as e:
                    print(e)

            if (self.i == 4):
                self.tensComplication()

            if (self.i == 5):
                try:
                    inWords = ""
                    if (self.actnumber[self.i] == 0 or self.actnumber[self.i + 1] == 1):
                        inWords = ""

                    else:
                        inWords = self.iWords[self.actnumber[self.i]]

                    if (self.actnumber[self.i + 1] != 0 or self.actnumber[self.i] > 0):
                        self.inWords.insert(self.j, inWords + ' /লক্ষ/')

                except Exception as e:
                    print(e)

            if (self.i == 6):
                self.tensComplication()

            if (self.i == 7):
                try:
                    inWords = ""
                    if (self.actnumber[self.i] == 0 or self.actnumber[self.i + 1] == 1):
                        inWords = ""
                    else:
                        inWords = self.iWords[self.actnumber[self.i]]
                    self.inWords.insert(self.j, inWords + ' /কোটি/')
                except Exception as e:
                    print(e)

            if (self.i == 8):
                self.tensComplication()

            if (self.i == 9):
                if (self.actnumber[self.i] == 0):
                    self.inWords.insert(self.j, '')
                elif (self.actnumber[self.i - 1] != 0 and self.actnumber[self.i - 2] != 0):
                    self.inWords.insert(self.j, self.iWords[self.actnumber[self.i]] + ' /শত/')
                else:
                    self.inWords.insert(self.j, self.iWords[self.actnumber[self.i]] + ' /শত/')

            if (self.i == 10):
                try:
                    inWords = ""
                    if (self.actnumber[self.i] == 0 or self.actnumber[self.i + 1] == 1):
                        inWords = ""
                    else:
                        inWords = self.iWords[self.actnumber[self.i]]

                    if (self.actnumber[self.i + 1] != 0 or self.actnumber[self.i] > 0):
                        self.inWords.insert(self.j, inWords + ' /হাজার/')
                except Exception as e:
                    print(e)

            if (self.i == 11):
                self.tensComplication()

            if (self.i == 12):
                try:
                    inWords = ""
                    if (self.actnumber[self.i] == 0 or self.actnumber[self.i + 1] == 1):
                        inWords = ""

                    else:
                        inWords = self.iWords[self.actnumber[self.i]]

                    if (self.actnumber[self.i + 1] != 0 or self.actnumber[self.i] > 0):
                        self.inWords.insert(self.j, inWords + ' /লক্ষ/')

                except Exception as e:
                    print(e)

            if (self.i == 13):
                self.tensComplication()

            if (self.i == 14):
                try:
                    inWords = ""
                    if (self.actnumber[self.i] == 0 or self.actnumber[self.i + 1] == 1):
                        inWords = ""
                    else:
                        inWords = self.iWords[self.actnumber[self.i]]
                    self.inWords.insert(self.j, inWords + ' /কোটি/')
                except Exception as e:
                    print(e)

            if (self.i == 15):
                self.tensComplication()

            self.j += 1
            self.i += 1

        k = 0

        self.inWords = list(reversed(self.inWords))
        while k < len(self.inWords):
            finalWord += self.inWords[k]
            k += 1
        return finalWord


