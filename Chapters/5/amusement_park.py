age = 12

"""
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
"""

"""
it would be more concise to set just the price inside the if-elif-else chain
and then have a simple print statement that runs after the chain has been
evaluated:
"""
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else: # senior discount
	price = 5

print("Your admission cost is $" + str(price) + ".")