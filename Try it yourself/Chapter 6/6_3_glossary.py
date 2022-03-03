"""
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
    • Think of five programming words you’ve learned about in the previous
    chapters. Use these words as the keys in your glossary, and store their
    meanings as values.
    • Print each word and its meaning as neatly formatted output. You might
    print the word followed by a colon and then its meaning, or print the word
    on one line and then print its meaning indented on a second line. Use the
    newline character (\n) to insert a blank line between each word-meaning
    pair in your output.
"""

glossary = {
    'if': "if statement is a conditional test that use to check an information.",
    'for': "for statement is a loop that to iterate a block code.",
    'list': "is a data structure that store, show and administrate information.",
    'print': "is a statement that to show the information in the promnt or a terminal.",
    'string': "is a data structure primitive, contains the set alfanumerical characters.",
}
# glossary.__len__()


print("Glossary for python." + "\n" +
    "print:" + "\n\t" +
    glossary['print'] + '\n' +
    "string:" + "\n\t" +
    glossary['string'] + '\n' +
    "if:" + "\n\t" +
    glossary['if'] + '\n' +
    "list:" + "\n\t" +
    glossary['list'] + '\n' +
    "for:" + "\n\t" +
    glossary['for'] 
)

