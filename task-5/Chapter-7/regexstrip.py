#Regex Version of the strip() Method

import re
def stripfn(str1,specchr):
    ask= input("Do you want to remoce specific characters from string? Y or N: ")
    if ask=="N":
        return str1.strip()
    else: 
        specchr= input("Enter character to be removed: ")
        str1regex= re.compile(specchr)
        return str1regex.sub("", str1)
specchr= ""
str1= input("Enter a string: ")
print(stripfn(str1, specchr))