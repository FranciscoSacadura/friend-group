"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

Jill = {'name':'Jill', 'age':26, 'job':'biologist', 'relationships':{'Zalika':'friend','John':'partner'}}

Zalika = {'name':'Zalika', 'age':28, 'job':'artist', 'relationships':{'Jill':'friend'}}

John = {'name':'John', 'age':27, 'job':'writer', 'relationships':{'Jill':'partner'}}

Nash = {'name':'Nash', 'age':34, 'job':'chef', 'relationships':{'John':'cousin','Zalika':'landlord'}}

my_group = {'Jill':Jill,'Zalika':Zalika,'John':John,'Nash':Nash}
