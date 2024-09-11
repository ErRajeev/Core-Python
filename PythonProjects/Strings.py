            # Strings in Python

name = "Rajeev Ranjan Kumar is a Bad Boy"
print(type(name))
print(name[ : : 1])
# print(name[ : :-1])

             # Python String Method/Function

# len()
print(len(name))

# count()
print(name.count("R"))

# find()   it's Return Index Value of A given String else -1;
f = name.find("B")
print(f)

# upper()    it' Capitalize all chr in a String
print(name.upper())

# lower()
print(name.lower())

# capitalize()      it's Capitalize Only First Letter
print(name.capitalize())

# replace()     it's Replace the Chars with given Args
print(name.replace("Rajeev", "Raj"))

# endswith()    it's Return True or False Based on given Args
print(name.endswith("y"))
