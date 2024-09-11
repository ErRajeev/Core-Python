# "start = int(input("Enter a Starting Range\n"))
# end = int(input("Enter End Range\n"))
# for num in range(start, end + 1):
#     for i in range(2, num):
#         if(num%i) == 0:
#             break
#     else:
#         print(num)


num = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda n: n%2 ==0, num)))