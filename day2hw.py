#A phrase is a  Palindrome if, after converting all uppercase letters into 
#lowercase letters and removing all non-alphanumeric characters, 
#it reads the same forward and backward. Alphanumeric characters 
#include letters and numbers.
#Given a string >>>>s<<<<<, return true or false.


#Establish a function first 
def findpalin(s):
#We need to establish string and remove spaces if needed and use .lower()
    s = s.lower().replace(" ","")
#We have to compare the string given to the reversed version of the string
    if s == s[::-1]:
#if the reversed s == s
        return True
#We return False if not a palindrome
    else:
        return False

print(findpalin("maam"))
print(findpalin("john"))
print(findpalin("racecar"))