#Date Detection

import re
dateregex= re.compile(r'(\d\d)/(\d{2})/(\d{4})')
mo= dateregex.search('28/02/2020')
day=str(mo.group(1))
month=str(mo.group(2))
year=str(mo.group(3))
if int(year)>=1000 and int(year)<=2999:

    if month in ["01", "03", "05", "07", "08", "10" "12"]:
        if int(day)<=31:
            print(mo.group())
        else:
            print("Doesn't Exist")

    if month in ["04", "06", "09", "11"]:
        if int(day)<=30:
            print(mo.group())
        else:
            print("Doesn't Exist")
    if month=="02":
        if ((int(year) % 400 == 0) or  
        (int(year) % 100 != 0) and  
        (int(year) % 4 == 0)) and int(day)<=29:
            print(mo.group())

        elif month=="02" and not ((int(year) % 400 == 0) or  
            (int(year) % 100 != 0) and  
            (int(year) % 4 == 0)) and int(day)<=28:
            print(mo.group())
        else:
            "Doesn't Exist"
else:
    print("Doesn't exist")
