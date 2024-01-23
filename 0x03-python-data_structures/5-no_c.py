#!/usr/bin/python3
def no_c(my_string):
new_string = ""
for elements in range(len(my_string)):
if (my_string[elements] != 'c' and my_string[elements] != 'C':
new_string += my_string[elements]
return new_string
