name = 'Zed A. Shaw'
age = 35 # not a lie
height = 75 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

centimeter = 2.54
kilogram = 2.2

print(f"Let's talk about {name}.")
print(f"He's{height} inches tall.")
print(f"He's  {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

#these are for converting the height and weight of the input
conversion1 = kilogram * weight
conversion2 = centimeter * height
round(conversion1)
round(conversion2)

print(f"If I convert {height} to metric, I am {conversion2} centimeters tall!")
print(f"If I convert {weight} to metric, I am {conversion1} kilograms!")