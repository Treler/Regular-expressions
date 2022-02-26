God damn.

This scrypts can help you with find emails and RUS numbers using regular expressions.
In my opinion, this reg exs so powerful, however you can modified them.

Check the examples in "emails.txt" and "numbers.txt".

Regex for numbers description:

*-----*

pattern = \+?[78](([\s-]|[({[])*\d{3}([\s-]|[)\]}])*\d{3}[\s-]*\d{2}[\s-]*\d{2})\b

\+ - escapes symbol "+". Number can starts with "+" and maybe not (+7 900 800 70 61 or 7 900 800 70 61)

? - 0 or 1 repetitions left pattern. Symbol "+" can be exists and maybe not

[7, 8] - one of the symbols in list. Russian numbers can starts with number "7" or "8"

([\s-]|[({[])*:

[\s-] - starts with any space symbol (space or tab) or symbol "-"
[({[] - There are numbers with brackes, such as "(", "{", "[". For example 7 (900) 800 70 61
| - operator "OR". Numbers may contain both space symbols and brackets and etc.
* - 0 or more repetitions left pattern.
\d - numbers from 0 to 9
{x} - count repetitions left pattern. \d{3} - code of RUS operator. For example, 495, 985 and etc.

*-----*


Regex for emails description:

*-----*

pattern = [-.\w]{1,25}@[-\w]{1,12}.[rucom]{2,3}

[-.\w] - email may consist symbols "-" or "." and letters. For example, emample.ex1@gmail.com

{1,25} - limitations of email contained characters

@ - no comments

.[rucom] - major part of emails ends with .ru or .com. This part of regex will be accepted even .ro and .co and etc. Therefore it needs some repair


*-----*

What do you need to do before using this scrypt:

1) Install python (ver. 3.x)


Files "numbers.txt" or "emails.txt" MUST BE in the same folder with scrypt.
File "clear_*.txt" will be created in the same folder as scrypt.
