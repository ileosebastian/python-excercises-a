"""
Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person.
 Then compose your message and store it in a new variable called message. Print your message.
"""

famous_person = "linus torvalds"
author_quote = "A computer is like air conditioning - it becomes useless when you oper Windows."

message = "\t" + famous_person.title() + " once said, " + "\""+ author_quote +"\""

print (message)