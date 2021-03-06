"""
distribution.py
Author: Funjando
Credit: DCFC21, Cedrik Julian, Payton, Michael J. Barber, 

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

#Import
import string

#Input
U_sen=input("Please enter a string of text (the bigger the better): ")

sen=U_sen.lower()
sen=sen.replace(" ", "")
sen=sen.replace(",", "")
sen=sen.replace(".", "")

#List
alpha=string.ascii_lowercase


lttr=[]
lttr_nr=[]



#Code
print('The distribution of characters in "' + U_sen + '" ' + 'is: ')


for x in alpha:
    if sen .count(x) != 0:
        lttr.append(x)
        lttr_nr.append(0-(sen .count(x)))



L1=zip(lttr_nr, lttr)





L1s=sorted(L1, key=lambda element: (element[0], element[1]))
#L1s=L1s[::-1]

#List



for item in L1s:

    print(item[1]*(-1*item[0]))








