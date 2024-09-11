            # Dictionary in Python

dic = {1: "Aman", 2: "Shubham", 3: 'Rajeev', 4: "Puja", 5: '''Rajavbabu'''}
print(type(dic))
print(dic)
print(dic[5])

            # Nested Dictionary & Function

di = {"Shubham": "Chiken", "Amna":"Chaumin", "Rajeev": "Paneer", "Puja": {"Ice-Creem", "Pizza", "Burger"}}
di["Rajababu"]= "Cake"      # Add in Dictionary
print(di)
print(di["Puja"])

# len()     it's Return the Key Number in Dictiomary

print(len(di))

# items()   it's Returns All Items in Dictionary

print(di.items())

# delelet

del di["Rajeev"]
print(di)

# cupy()

di1 = di.copy()
del di1["Puja"]
print(di)
print(di1)

# update
di.update({"Tiwari": "Aam"})
print(di)

