python-calculator
A command-line calculator in pure Python, no libraries.

Features
Add, subtract, multiply, divide, with a divide-by-zero guard
Keeps running until you type quit
history replays every calculation from the session
History is a list of dicts, one per operation
Run it
text

python3 cal.py
Notes
None handling is what caused most of the bugs here — an operation that failed still
returned something, and that something got stored in history. The current version
checks the result before appending it.
