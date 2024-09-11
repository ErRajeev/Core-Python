# def add(a,b):
#     return a + b
# res = add(5,9)
# print(res)
#
#
# f = (lambda a,b: a+b)
# rest = f(132,8)
# print(rest)
#
# f = (lambda : print("This is Lamda Function"))
# f()



        # filter

num = [12,37,49,86,289,16,38,36, 31,25,65,46]
even=list(filter(lambda n: n%2==0,num))
print(even)


        # map

num = [66,54,5,3,9,6,2,3]
res = list(map(lambda a: a*a, num))
print(res)


        # reduce

# from functools import reduce
# num = [66,54,5,3,9,6,2,3]
# res = reduce(lambda a,b: a+b, num)
# print(res)


