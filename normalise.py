#This program reads in a string and strips any leading
#or trailing spaces, the program also convert the string to lower case.
#This program also output the length of the input and output strings.
#Author: Caoimhe McBrien 

rawstring= input ("please enter a string: ")
normalisedstring = rawstring.strip().lower()
print (normalisedstring)        