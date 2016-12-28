# code-katas
CodeWars Assignments for Snow Day.

Convert a String to an Array (8 kyu)
- Module:string_to_array.py
- Tests: test_string_to_array.py
- Link: https://www.codewars.com/kata/convert-a-string-to-an-array/train/python
- Interesting/simplest Solution: I didn't think to add the space in the .split().

```python
def string_to_array(string):
    """Solution by jerod84."""
    return string.split(" ")
    
```

Last (8 kyu)
- Module: last.py
- Tests: test_last.py
- Link: https://www.codewars.com/kata/last/train/python
- Interesting Solution: I love try/except.  It's so simple.
```python
def last(*args):
    """Solution by jake9066."""
    try:
        return args[-1][-1]
    except:
        return args[-1]
```

Fake Binary (8 kyu)
- Module: fake_binary.py
- Tests: fake_binary.py
- Link: https://www.codewars.com/kata/fake-binary
- Interesting Solution: 
```python
def fake_bin(s):
    """Solution by PilgrimShadow."""
  return ''.join('0' if int(c) < 5 else '1' for c in s)
```

Count of positives / sum of negatives (8 kyu)
- Module: count_positives_sum_negatives.py
- Tests: test_count_positives_sum_negatives.py
- Link: https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives/train/python
- Interesting Solution: I think these ternaries are interesting but I'm not sure I like them.  I think they're kind of hard to read.  Are they more pythonic than ifs and fors?
```python
def count_positives_sum_negatives(arr):
    """Solution by j.pihlgren."""
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
```

Convert number to reversed array of digits (8 kyu)
- Module: digitize.py
- Tests: test_digitize.py
- Link: https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/python
- Interesting Solution: I liked map functions in js but am not yet used to them in python.
```python
def digitize(n):
    """Solution by colbydauph."""
    return map(int, str(n)[::-1])
```

Ones and zeros (8 kyu)
- Module: binary_list_to_number.py
- Tests: test_list_array_to_number.py
- Link: https://www.codewars.com/kata/ones-and-zeros/train/python
- Interesting Solution: Still love that map.  Didn't know about the binary optional argument in int().  That's cool.
```python
def binary_array_to_number(arr):
    """Solution by andrewferk."""
    return int("".join(map(str, arr)), 2)
```


Holiday V - SeaSick Snorkelling (7 kyu)
- Module: sea_sick.py
- Tests: test_sea_sick.py
- Link: https://www.codewars.com/kata/holiday-v-seasick-snorkelling/train/python
- Interesting Solution: Another simple ternary.  I think this one is easy to read and clear.
```python
def sea_sick(sea):
    """Solution by kevin.du."""
    return "Throw Up" if (sea.count("~_") + sea.count("_~")) > 0.2*len(sea) else "No Problem"
```

String Reversing, Changing case, etc. (7 kyu)
- Module: reverse_and_mirror.py
- Tests: test_reverse_and_mirror.py
- Link: https://www.codewars.com/kata/string-reversing-changing-case-etc/train/python
- Interesting Solution: Simple ternary.  I think this one is even clearer and easier to read.
```python
def reverseAndMirror(s1,s2):
    """Solution by dkleist."""
    return s2.swapcase()[::-1] + '@@@' + s1.swapcase()[::-1] + s1.swapcase()
```

Flatten Me (7 kyu)
- Module: flatten_me.py
- Tests: test_flatten_me.py
- Link: https://www.codewars.com/kata/flatten-me/train/python
- Interesting Solution: I'm hoping that if I look at enough of these ternaries I'll start using them.
```python
def flatten_me(lst):
    """Soltion by daddepledge."""
    return [v for sub in [e if type(e) == list else [e] for e in lst] for v in sub]
```

Sum up the random string (7 kyu)
- Module: sum_from_string.py
- Tests: test_sum_from_string.py
- Link: https://www.codewars.com/kata/sum-up-the-random-string/train/python
- Interesting Solution: I spent some time trying to do it this way, but I come up short figuring out the regex.  
```python
import re
def sum_from_string(string):
    """Solution by JustFY."""
    d = re.findall("\d+",string)
    return sum(int(i) for i in d)
```

Show multiples of 2 numbers within a range (7 kyu)
- Module: multiples.py
- Tests: test_multiples.py
- Link: https://www.codewars.com/kata/show-multiples-of-2-numbers-within-a-range/train/python
- Interesting Solution: I like that they used not a % s1.  I didnt think to use a not with modulus but it makes so much sense.  Will do that in the future.
```python
def multiples(s1, s2, s3):
    """Solution by zebulan."""
    return [a for a in xrange(1, s3) if not(a % s1 or a % s2)]
```

Sum of the first nth terms of a series (7 kyu)
- Module: series_sum.py
- Tests: test_series_sum.py
- Link: http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/train/python
- Interesting Solution: Making the numerator a float() was smart.
```python
def series_sum(n):
    """Solution by MMMAAANNN"""
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
```


Proper Parenthetics
- Module: proper_parenthetics.py
- Tests: test_proper_parenthetics.py


Sort Cards (7kyu)
-Module: sort_cards.py
-Tests: test_sort_cards.py
-Link: https://www.codewars.com/kata/sort-deck-of-cards/train/python
