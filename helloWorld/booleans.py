# boolean expressions

"""
statement that is either True or False.

Today is a weekday. -> can only be True or False

Friday is the best day. -> opinion

My dog is the cutest dog in the world -> no
Dogs are mammals -> yes
My dog is named Pavel -> yes
Dogs make the best pets -> no
Cats are female dogs -> yes
"""

# Relational Operators (==), (!=)

"""
1 == 1 -> True
2 != 4 -> True
3 == 5 -> False
'7' == 7 -> False
"""

"""
(5 * 2) - 1 == 8 + 1 -> True
13 - 6 != (3 * 2) + 1 -> False
3 * (2 - 1) == 4 - 1 -> True
"""

# Boolean variables

var1 = True
var2 = False

bool_one = (5 * 2) - 1 == 8 + 1
print(bool_one)

my_bool = "true"
print(type(my_bool))
my_bool2 = True
print(type(my_bool2))

# If Statements

# conditional statements are statements in the form if [it is raining], then [bring an umbrella]
is_raining = True
if is_raining:
    print("bring an umbrella")

user_name = "Dave"
if user_name == "Dave":
    print("Get off my computer Dave!")

# Other relational operators: >=, > , <, <=

x = 20
y = 20
credits = 120
gpa = 3.4

if x == y:
    print("These numbers are the same.")


if credits >= 120 and gpa >= 2.0:
    print("You can graduate!")

else:
    print("you cannot graduate.")

# Boolean opertors (and, or, not)
"""
boolean operators combines two boolean expressions into a larger boolean expression

Oranges are a fruit or carrots are a vegetable.
"""

var = (1 + 1 == 2) and (2 + 2 == 4) # True
(1 > 9) and (5 != 6) # False
(1 + 1 == 2) and (2 < 1) # False
(0 == 10) and (1 + 1 == 1) # False

# "BEDMAS" ordering (precedence) -> (), func(), ==, !=, <, >, <=, >=, not, and, or
if not credits >= 120:
    print("you cannot graduate.")
if not gpa >= 2.0:
    print("you cannot graduate")
if not credits >= 120 and not gpa >= 2.0:
    print("you do not meet either requirements")

donation = 1100

if donation >= 1000:
    print("platnimum status")
elif donation >= 500:
    print("gold status")
elif donation >= 100:
    print("silver status")
else:
    print("bronze status")

grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")