import re
'''
(0) re module
(1) Methods to search or matches
(2) Methods on a match object
(3) Meta characters
(4) More special sequences
(5) Sets
(6) Quantiier
(7) Conditions
(8) Grouping
(9) Modifications
(10) Compilations flags
# Note : always compile what you want to search.
'''

'''
# THis is one way to get data
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

#***************************************************************

# THis is second way to get data
test_string = '123abc456789abc123ABC'
matches = re.finditer(r"abc",test_string)

for match in matches:
    print(match)
'''

'''
# Difference in r
a = r"\tHello"
print(a)
a = "\tHello"
print(a)
'''


#**************************** (1) Methods to search or matches ****************************#

# match(), search(), findall(), finditer()

'''
# finditer()

test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
'''

'''
# findall()

test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.findall(test_string)

for match in matches:
    print(match)
'''
'''
# match()

# It finds the elements only at the begining
# test_string = '123abc456789abc123ABC'
test_string = 'abc456789abc123ABC'
pattern = re.compile(r"abc")
match = pattern.match(test_string)

print(match)
'''

'''
# search()

# It will search elements only once in the whatever data we have, if it get the matching result then it will stop finding elements in remaining database
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
match = pattern.search(test_string)

print(match)
'''

#**************************** (2) Methods on a match object ****************************#

# group(), span(), start(), end()
'''
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

for match in matches:
    # print(match.span(), match.start(), match.end())
    print(match.group())
'''

#**************************** (3) Meta characters ****************************#

# All Meta Characters : . ^ $ * + ? { } [ ] \ ( )

'''
.   : Any character (except newline charcter)
^   : starts with "^hello"
$   : ends with "hello$"
*   : Zero or more occurance "aix*"
+   : One or more occurance "aix+"
{ } : Exactly the specified number of occurrences "al{2}"
[ ] : A set of charcters "[a-z]"
\   : Special sequence (or escape special charcters) "\d" or "\."
|   : Either or "Dhoni|Sachin|Sehevag"
( ) : Capture and group
'''

'''
# It will print all the charadters
test_string = '123abc456789abc123ABC'
pattern = re.compile(r".")
matches = pattern.finditer(test_string)

for match in matches:
    print(match.group())

#####################################################

# i we want to search only "." perticularly
test_string = '123abc456789abc123ABC.'
pattern = re.compile(r"\.")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

'''
'''
# if we want search the characers are at the beginning or not
test_string = '123abc456789abc123ABC.'
pattern = re.compile(r"^123")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

#####################################################

# if we want search the characers are at the end or not
test_string = '123abc456789abc123ABC.'
pattern = re.compile(r"ABC$")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
'''



#**************************** (4) More special sequences ****************************#

'''
\d : Matches any decimal digit [0-9]
\D : Matches any non-decimal characters
\s : Matches any whitespace character (space " ", tab "\t", newline "\n")
\S : Matches any non-whitespace character
\w : Matches any alphanumaric characters [a-zA-Z0-9_]
\W : Matches any non-alphanumaric characters
\b : Matches where the speciied characters are at the beginning or at the end of the word
\B : Matches where the speciied characters, but not at the beginning
'''

'''
test_string = "hello 123_@ heyho hohey"
# pattern = re.compile(r"\d")
# pattern = re.compile(r"\D")
# pattern = re.compile(r"\s")
# pattern = re.compile(r"\S")
# pattern = re.compile(r"\w")
# pattern = re.compile(r"\W")
# pattern = re.compile(r"\bhello")
# pattern = re.compile(r"\b123")
# pattern = re.compile(r"\bhey")
# pattern = re.compile(r"\Bhey")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
'''



#**************************** (5) Sets ****************************#

'''
test_string = 'helloHello 123-_'
# pattern = re.compile(r"[lo]")   # find 'l' and 'o' in the string
# pattern = re.compile(r"[a-z]")  # find any charcter between 'a' and 'z'
# pattern = re.compile(r"[A-Z]")  # find any charcter between 'A' and 'Z'
# pattern = re.compile(r"[0-9]")  # find any digit between 0 and 9
# pattern = re.compile(r"[0-9-]")  # if we want find '-' also and digit alse
pattern = re.compile(r"[a-zA-Z0-9-_]")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
'''

#**************************** (6) Quantiier ****************************#
'''
*       : 0 o or more
+       : 1 or more
?       : 0 or 1, -> optional charater
{4}     : exact number
{1,9}   : range in numbers (min,max)
'''

'''
# test_string = '123abc456789abc123ABC.'
# pattern = re.compile(r"_?\d+")
test_string = 'hello_123456789'
pattern = re.compile(r"\d{1,5}")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
'''

"""
dates = '''
01.04.2020

2020.04.01

2020-04-01
2020-01-12
2020-11-05
2020-12-02

2020/04/01

2020_12_01
2020_07_15
'''

'''
# pattern = re.compile(r"\d\d\d\d-\d\d-\d\d")
# pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
# pattern = re.compile(r"\d{4}/\d{2}/\d{2}")
# pattern = re.compile(r"\d{2}\.\d{2}\.\d{4}")
# pattern = re.compile(r"\d{4}_\d{2}_\d{2}")
# pattern = re.compile(r"\d{4}[_\.?]\d{2}[_\.?]\d{2}")
matches = pattern.finditer(dates)

for match in matches:
    print(match)
'''
"""
#**************************** (7) Conditions ****************************#

"""
test_string = '''
Mr Joshi
Mrs Mahajan
Mr. Smith
Ms Landge
Mr. T
'''

'''
# pattern = re.compile(r"Mr\.?\s\w+")
pattern = re.compile(r"(Mr|Mrs|Ms)\.?\s\w+")
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
'''
"""


"""
test_urls = '''
http://example.com
http://example_123.in
https://google123.in

'''

pattern = re.compile(r"(http://|https://)([a-z_0-9]+)(\.[a-z]+)")
matches = pattern.finditer(test_urls)

for match in matches:
    print(match[2])
    print(match)
"""


#**************************** (8) Grouping ****************************#

"""
test_email = '''
rohanpurane0@gmail.com
tata_capital@tcs.org
infosys.software_123@info.in
'''
pattern = re.compile(r"([a-z\_.?0-9]+)@([a-z]+)\.(com|org|in)")
matches = pattern.finditer(test_email)

for match in matches:
    print(match[1])
    # print(match.group(2))
    # print(match.group(3))
"""






#**************************** (9) Modiications ****************************#
# split, sub

'''
test_string = '123abc456789abc123ABC'
pattern = re.compile(r"abc")
splitted = pattern.split(test_string)

print(splitted)
'''
'''
test_string = 'hello world, you are the best world'
pattern = re.compile(r"world")
subbed_string = pattern.sub("planet", test_string)

print(subbed_string)
'''


"""
test_urls = '''
hello
2020-05-20
http://example.com
http://www.example_123.in
https://www.google123.in
https://www.python-engineer.net
http://www.python-world.net
'''
# pattern = re.compile(r"(http://www|https://www)\.([a-zA-Z0-9-?]+)\.([a-z]+)")
# pattern = re.compile(r"(https://www|http://www|http://)\.?([a-zA-Z0-9-?]+)\.([a-z]+)")
pattern = re.compile(r"(https://www|http://www|http://)\.?([a-zA-Z0-9_?]+)\.([a-z]+)")
matches = pattern.finditer(test_urls)
for match in matches:
    print(match)
"""



"""
test_urls = '''
hello
2020-05-20
http://example.com
http://www.example_123.in
https://www.google123.in
https://www.python-engineer.net
http://www.python-world.net
'''

pattern = re.compile(r"(https://www|http://www|http://)\.?([a-zA-Z0-9_?]+)(\.[a-z]+)")
matches = pattern.finditer(test_urls)
for match in matches:
    print(match.group(3))

# subbed_urls = pattern.sub(r"\1\2",test_urls)
# print(subbed_urls)
"""

#**************************** (10) Compilations flags ****************************#
'''
ASCII, A
DOTALL, S
IGNORECASE, I
LOCALE, L
MULTILINE, M
VERBOSE, X
'''

'''
my_string = "Hello World"
pattern = re.compile(r"world", re.I)
matches = pattern.finditer(my_string)
for match in matches:
    print(match)
'''