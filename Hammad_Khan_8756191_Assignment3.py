print("Welcome, to Abby's Merchandizing! This tool can be used to place an order with us as well as to calculate the total cost of your order. Let's get started!")

cost = 9.99
cost2 = 14.99
hst = 1.13

print("")

print("We offer a wide range of colors for our shirts starting at $9.99 each! Please enter in the color of the shirt you want!")

print("")

class Shirts(object):
    def __init__(self, colorinput, typeinput, numinput):
        self.colorinput = colorinput
        self.typeinput = typeinput
        self.numinput = numinput

    def getColorIn(colorinput):
        print("You chose a", colorinput, "shirt. Great choice!")

    def getTypeIn(typeinput):
        print("You chose a", typeinput, "shirt. Great choice!")
    
    def getNumIn(numinput):
        print("You want:", numinput, "shirt(s).")

colorinput = (input("What color shirt would you like?: "))
result1 = Shirts.getColorIn(colorinput)

print("")

print("Next, select the type of shirt you would like. We offer two types of shirts, polo or t-shirt.")

typeinput = (input("What type of shirt would you like?: "))
result2 = Shirts.getTypeIn(typeinput)

print("")

numinput = int(input("Lastly, decide how many shirts you would like!: "))
result3 = Shirts.getNumIn(numinput)

print("") 

print("We are excited to announce that we are now selling hoodies starting at $14.99 each! Please enter in the color hoodie you want!")

print("")

class Hoodies(object):
    def __init__(self, colorinput2, typeinput2, numinput2):
        self.colorinput2 = colorinput2
        self.typeinput2 = typeinput2
        self.numinput2 = numinput2

    def getColorIn2(colorinput2):
        print("You chose a", colorinput2, "hoodie. Great choice!")

    def getTypeIn2(typeinput2):
        print("You chose a", typeinput2, "hoodie. Great choice!")
    
    def getNumIn2(numinput2):
        print("You want:", numinput2, "hoodie(s).")

colorinput2 = (input("What color hoodie would you like?: "))
result4 = Hoodies.getColorIn2(colorinput2)

print("") 

print("Next, select the type of hoodie you would like. We offer two types of hoodies, pullover or zip-up.")

typeinput2 = (input("What type of hoodie would you like?: "))
result5 = Hoodies.getTypeIn2(typeinput2)

print("")

numinput2 = int(input("Lastly, decide how many hoodies you would like!: "))
result6 = Hoodies.getNumIn2(numinput2)

print("")

print("Alright, lets recap your order.")

print("")

if colorinput == 3:
    print("Color of shirt: Blue")

elif colorinput == 4:
    print("Color of shirt: Red")

elif colorinput == 5:
    print("Color of shirt: Green")

elif colorinput == 6:
    print("Color of shirt: Yellow")

elif colorinput == 7:
    print("Color of shirt: Orange")

elif colorinput == 8:
    print("Color of shirt: White")

elif colorinput == 9:
    print("Color of shirt: Black")

#print("Color of shirt: " + str(colorinput))

if typeinput == 1:
    print("Type of shirt: Polo")

elif typeinput == 2:
    print("Type of shirt: T-shirt")

#print("Type of shirt: " + str(typeinput))

print("Number of shirt(s): " + str(numinput))

if colorinput2 == 8:
    print("Color of hoodie: White")

elif colorinput2 == 9:
    print("Color of hoodie: Black")

elif colorinput2 == 10:
    print("Color of hoodie: Brown")

#print("Color of hoodie: " + str(colorinput2))

if typeinput2 == 11:
    print("Type of hoodie: Zip-Up")
    
elif typeinput2 == 12:
    print("Type of hoodie: Pullover")

#print("Type of hoodie: " + str(typeinput2))

print("Number of hoodie(s): " + str(numinput2))

print("")

totalcost = (cost*numinput)
totalcost2 = (cost2*numinput2)
finalcost = (totalcost + totalcost2)

disc15 = 0.15
quanDisc = finalcost*disc15

disc10 = 0.10
ageDisc = finalcost*disc10

discPrice = (finalcost - quanDisc) - ageDisc
discPrice2 = (finalcost - quanDisc)
discPrice3 = (finalcost - ageDisc)

def quanElig():
    print("You are eligible for a quantity discount of 15%' off!")
    print("$%.2f off!" % (quanDisc))

def ageElig():
    print("You can be eligible for a discount if you are a senior citizen or student!")
    global age
    age = int(input("Please enter in your age: "))

def ageCalc():
        print("")
        print("Your are eligible for our age discount of 10%' off!")
        print("$%.2f off!" % (ageDisc))
        print("Subtotal: $%.2f" % (finalcost))
        print("Discounted Price: $%.2f" % (discPrice))
        print("Total: $%.2f" % (discPrice * hst))

def noDisc():
        print("")
        print("Sorry, there is no discount for your age range")
        print("Subtotal: $%.2f" % (finalcost))
        print("Total: $%.2f" % (finalcost * hst))

def quanCalc():
        print("")
        print("Sorry, there is no discount for your age range")
        print("Subtotal: $%.2f" % (finalcost))
        print("Discounted Price: $%.2f" % (discPrice2))
        print("Total: $%.2f" % (discPrice2 * hst))


if numinput >= 3 or numinput2 >= 3:
    quanElig()

    print("")

    ageElig()

    if age >= 65:
        ageCalc()

    elif 24 >= age >= 18:
        ageCalc()

    else:
        quanCalc()

elif numinput < 3 and numinput2 < 3:
    ageElig()

    if age >= 65:
        ageCalc()

    elif 24 >= age >= 18:
        ageCalc()

    else:
        noDisc()

else:
    noDisc()

print("")

print("Thank you for choosing Abby's Merchandizing today! We hope you enjoyed your shopping experience with us! ")