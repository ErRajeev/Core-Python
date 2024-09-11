student = ['Rajeev', 'Aman', 'Pooja']
subject = ['Maths', 'Python']

ziped = list((zip(student, subject)))
print(ziped)
for a, b in ziped:
    print(a, b)
