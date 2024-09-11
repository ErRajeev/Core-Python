import re

# nameage = ''' Rajeev is 21 Pooja is 24
#             Aman is 23 Kumar is 32 and Khan is 54 year old'''

# ages = re.findall(r'\d{1,3}', nameage)
# names = re.findall(r'[A-Z][a-z]*', nameage)

# data = {}
# temp = 0

# for i in ages:
#     data[i] = names[temp]
#     temp += 1

# print(data)




# ex = "mat cat ra hat chat bat"

# res = re.findall(r'[a-z]*[t]', ex)
# for i in res:

#     print(i)





# animal = "cow dog monkey donkey bull"
# rep = re.compile(r"[d]onkey")
# animal = rep.sub('Lions', animal)
# print(animal)




para = '''hi, every one
this is Rajeev Ranjan
i'm from Bihar
and i currently persuing mac
from kongu Engineering College '''

print(para)
newPara = re.compile("\n")
para = newPara.sub(" ", para)

print(para)
