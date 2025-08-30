# 📚 BookBot:
A CLI Text AnalyzerBookBot is a simple Command-Line Interface (CLI) tool written in Python. It's designed to analyze text files, providing two key pieces of information: the total word count and the frequency of each character, sorted from most to least frequent.This tool is perfect for anyone who wants a quick way to get basic statistics from any text file, whether it's a book, an article, or a simple document.

## ✨ Features
- Word Count: Quickly get the total number of words in a text file.
- Character Frequency: See a detailed breakdown of how many times each character appears.
- Sorted Output: The character count is presented in a clear, easy-to-read list, sorted in descending order.

## 🚀 Getting Started
To use BookBot, you'll need Python 3.x installed on your system.
Clone the repository:
```bash
git clone [https://github.com/AlexMarchi2000/bookbot.git](https://github.com/AlexMarchi2000/bookbot.git)
cd bookbot
```
Run the tool:
Use the bookbot.py script and pass your file as an argument.
```bash
python3 main.py <path_to_your_file>
```
For example:
```bash
python3 main.py books/frankenstein.txt
```

## 📋 Example Output
After running the command on a sample file, the output will look something like this:
```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
,: 5962
p: 5952
g: 5795
b: 4868
v: 3737
.: 3121
k: 1661
;: 1350
x: 691
“: 506
j: 497
q: 325
”: 316
z: 235
:: 211
?: 208
!: 201
-: 173
’: 144
_: 124
—: 123
*: 97
1: 91
============= END ===============
```
