"""
    Now that you know how to loop through a dictionary, clean
    up the code from Exercise 6-3 (page 102) by replacing your series of print
    statements with a loop that runs through the dictionary’s keys and values.
    When you’re sure that your loop works, add five more Python terms to your
    glossary. When you run your program again, these new words and meanings
    should automatically be included in the output.
"""

glossary = {
    'if': "if statement is a conditional test that use to check an information.",
    'for': "for statement is a loop that to iterate a block code.",
    'list': "is a data structure that store, show and administrate information.",
    'print': "is a statement that to show the information in the promnt or a terminal.",
    'string': "is a data structure primitive, contains the set alfanumerical characters.",
    # Another Python terms:
    'step': "is a function for store a unondered objects uniques.",
    'dictionary': 'is a data structure dinamyc, is based on key-value pairs for to store information.',
    'not': "is a negation of a declaration.",
    'zen of python': "is python's philosophy to provide for all programmers in this language.",
    'sorted': "is a function that gives an order list or iterable.",
}

i = 1
for term, mean in glossary.items():
    print("\t", i, "\t\t", term, ": ", mean)
    i = i + 1