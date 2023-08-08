#Sandwich Maker
import pyinputplus as pyip
price= {'Wheat': 10, 'White': 12, 'Sourdough': 15, 'Chicken': 30, 'Turkey': 33, 'Ham': 35, 'Tofu': 40, 'Cheddar': 10, 'Swiss': 12, 'Mozzarella': 15, 'Mayo': 3, 'Mustard': 5, 'Lettuce': 7, 'Tomato': 7}

while True:
    order=[]
    a= pyip.inputMenu(['Wheat', 'White', 'Sourdough'], prompt="Choose bread type- \n", numbered=True)
    order.append(a)
    b= pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt="Choose protein type- \n", numbered=True)
    order.append(b)
    c= pyip.inputYesNo(prompt="Do you want cheese? \n")
    if c=='Yes' or c=='yes':
        d= pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt="Choose type of cheese- \n", numbered=True)
        order.append(d)
    e= pyip.inputYesNo(prompt="Do you want mayo? \n")
    if e=='Yes' or e=='yes':
        order.append('Mayo')
    f= pyip.inputYesNo(prompt="Do you want mustard? \n")
    if f=='Yes' or f=='yes':
        order.append('Mustard')

    g= pyip.inputYesNo(prompt="Do you want lettuce? \n")
    if g=='Yes' or g=='yes':
        order.append('Lettuce')
    h= pyip.inputYesNo(prompt="Do you want tomato? \n")
    if h=='Yes' or h=='yes':
        order.append('Tomato')
    num= pyip.inputInt(prompt="How many sandwiches do you want? ", min=1)
    bill=0
    for ingredients in order:
        cost= price[ingredients]
        bill+=cost
    print("Total bill= ", bill*num)
    ask= pyip.inputYesNo(prompt="Do you want to order something else?")
    if ask=='Yes' or ask=='yes':
        continue
    else:
        break

