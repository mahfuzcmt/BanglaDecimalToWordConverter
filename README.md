## [BDT Decimal to Words Converter](https://pypi.org/project/bdtdecimaltowordsconverter/)

## Prerequisites

* python 3x
* pip3

## Installation

**BEFORE YOU INSTALL:** please ensure the [prerequisites](#prerequisites)
```bash
pip install bdtdecimaltowordsconverter
```

## Usage

### import DecimalToWords from bdtdecimaltowordsconverter

```bash
from bdtdecimaltowordsconverter.bdtdecimaltowordsconverter import DecimalToWords

```

### make object of bdtdecimaltowordsconverter

```bash
decimal_to_words = DecimalToWords()
```
### call the convertAmount() function with your value
```bash
decimal_to_words.convertAmount(8.89, False, False, 'bng')
```

### parameters
##### (numericValue, is_ignorable_taka_if_zero, is_ignorable_paisa_if_zero, language)

* 1. number value that need to be converted. can be used interger or decimal
* 2. If you don't want to get zero value of taka, for an example you need to convert 0.23 and you want to skip/ignore zero in the return value then pass True otherwise False. If you pass False ( decimal_to_word.convertAmount(0.23, False, False, 'eng') ) then result will be 'zero taka and twenty three paisa only' and if you pass True ( decimal_to_word.convertAmount(0.23, True, False, 'eng') ) then result will be 'twenty three paisa only'
* 3. same as taka here is the value of paisa.
* 4. output language available languages
	'bng' for bangla and 'eng' for english

### [Javascript Version](http://jsfiddle.net/mahfuzcmt/vxmta5ua/1/)

### [Number Converter](https://github.com/mahfuzcmt/numberconverter)

## Contact with [Author](https://www.fb.com/mahfuzcmt)
