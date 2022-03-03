user_0 = {
    'username' : 'ileosebastian',
    'first' : 'leo',
    'last' : 'intriago',
    }


for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

print(user_0.keys())

print()

"""
    .items() provide a set objects
        in fact, is a tuple and inside a list of tuples
        ( [ ( , ), ( , ), ... ],  
          [ ( , ), ( , ), ... ], 
          [ ( , ), ( , ), ... ],
          ... )
"""

# This list doesn't make sense
list_wtf = ([('fear_year', 2020), ('name', 'ileosebastian')], 
            [('old_year', 1984), ('last', 'intriago')])

print("LIST WTF")

for wtf, XD in list_wtf:
    print(wtf, XD, sep='\t')
    print("Only XD: ", XD)

print("\tFirst list of a tuple: " + str(list_wtf[0]))
print("\t\tFirst tuple in a list: " + str(list_wtf[0][0]))
print("\t\t\tFirst value in a tuple: " + str(list_wtf[0][0][0]))
