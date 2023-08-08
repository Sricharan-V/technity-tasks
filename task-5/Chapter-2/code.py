# 3
print("and operator truth table")
print("False and True gives", (False and True))
print("True and False gives", (True and False))
print("True and True gives", (True and True))
print("False and False gives", (False and False), "\n")

print("or operator truth table")
print("False and True gives", (False or True))
print("True and False gives", (True or False))
print("True and True gives", (True or True))
print("False and False gives", (False or False), "\n")

print("not operator truth table")
print("not True gives", (not True))
print("not False gives",  (not False))


#9
spam= input("Enter value: ")
if spam=="1":
    print("Hello")
elif spam == "2":
    print("Howdy")
else:
    print("Greetings!")


#13
#Using for loop 
for i in range(1,11):
    print(i)

# Using while loop
i=1
while i<11:
    print(i)
    i+=1