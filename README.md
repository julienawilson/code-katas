# code-katas
CodeWars Assignments for Snow Day.

Convert a String to an Array (8 kyu)
- Module:string_to_array.py
- Tests: test_string_to_array.py
- Link: https://www.codewars.com/kata/convert-a-string-to-an-array/train/python
-Interesting/simplest Solution: I didn't think to add the space in the .split().

'''python

def string_to_array(string):
    return string.split(" ")
    
'''

Last (8 kyu)
- Module: last.py
- Tests: test_last.py
- Link: https://www.codewars.com/kata/last/train/python
-Interesting Solution: I love try/except.  It's so simple.
'''python
def last(*args): 
    try:
        return args[-1][-1]
    except:
        return args[-1]
'''

Fake Binary (8 kyu)
- Module: fake_binary.py
- Tests: fake_binary.py
- Link: https://www.codewars.com/kata/fake-binary
-Interesting Solution: 
'''python
def fake_bin(s):
  return ''.join('0' if int(c) < 5 else '1' for c in s)
'''

Count of positives / sum of negatives (8 kyu)
- Module: count_positives_sum_negatives.py
- Tests: test_count_positives_sum_negatives.py
- Link: https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives/train/python
-Interesting Solution: I think these ternaries are interesting but I'm not sure I like them.  I think they're kind of hard to read.  Are they more pythonic than ifs and fors?
'''python
def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
'''

Convert number to reversed array of digits (8 kyu)
- Module: digitize.py
- Tests: test_digitize.py
- Link: https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/python
-Interesting Solution: I liked map functions in js but am not yet used to them in python.
'''python
def digitize(n):
    return map(int, str(n)[::-1])
'''

Ones and zeros (8 kyu)
- Module: binary_list_to_number.py
- Tests: test_list_array_to_number.py
- Link: https://www.codewars.com/kata/ones-and-zeros/train/python
-Interesting Solution: Still love that map.  Didn't know about the binary optional argument in int().  That's cool.
'''python
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
'''


Holiday V - SeaSick Snorkelling (7 kyu)
- Module: sea_sick.py
- Tests: test_sea_sick.py
- Link: https://www.codewars.com/kata/holiday-v-seasick-snorkelling/train/python
-Interesting Solution: Another simple ternary.  I think this one is easy to read and clear.
'''python
def sea_sick(sea):
    return "Throw Up" if (sea.count("~_") + sea.count("_~")) > 0.2*len(sea) else "No Problem"
'''

String Reversing, Changing case, etc. (7 kyu)
- Module: reverse_and_mirror.py
- Tests: test_reverse_and_mirror.py
- Link: https://www.codewars.com/kata/string-reversing-changing-case-etc/train/python
-Interesting Solution: Simple ternary.  I think this one is even clearer and easier to read.
'''python
def reverseAndMirror(s1,s2):
    return s2.swapcase()[::-1] + '@@@' + s1.swapcase()[::-1] + s1.swapcase()
'''

Flatten Me (7 kyu)
- Module: flatten_me.py
- Tests: test_flatten_me.py
- Link: https://www.codewars.com/kata/flatten-me/train/python
-Interesting Solution: ADD ME HERE
'''python
'''

Sum up the random string (7 kyu)
- Module: sum_from_string.py
- Tests: test_sum_from_string.py
- Link: https://www.codewars.com/kata/sum-up-the-random-string/train/python
-Interesting Solution: ADD ME HERE
'''python
'''

Show multiples of 2 numbers within a range (7 kyu)
- Module: multiples.py
- Tests: test_multiples.py
- Link: https://www.codewars.com/kata/show-multiples-of-2-numbers-within-a-range/train/python
-Interesting Solution: ADD ME HERE
'''python
'''

