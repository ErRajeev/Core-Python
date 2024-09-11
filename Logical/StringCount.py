def reverseWord(Sentence):
    words = Sentence.split(" ")
    newWords = [word[::-1]for word in words]
    newSentence = "".join(newWords)
    return newSentence


def reverseLine(Sentence):
    word = Sentence.split(" ")
    print("REVERSE ORDER IN EACH LINE : ")
    for i in range(len(word)-1, -1, -1):
        print(word[i], end='')


def WithoutSpace(Sentence):
    word = Sentence.split(" ")
    print("DISPLAY FILE CONTENT WITHOUT SPACE")
    for i in range(0, len(word)):
        print(word[i], end='')


def Concatenation(filename):
    with open("new-file.txt", "w")as new_file:
        for name in filenames:
            with open(name)as f:
                for line in f:
                    new_file.write(line)
    file2 = open("new-file.txt", "r")
    print("CONCATENATION TEXT FILE CONTENT : ", file2.readline())


def FileCreate(name):
    file = open(name, "w")
    a = input("ENTER THE SENTENCE : ")
    file.write(a)
    file.close()


File_name1 = input("ENTER THE FILE NAME :")
FileCreate(File_name1)
print(''' FILE OPERATIONS
    1. PRINT EACH WORD OF A FILE IN REVERSE ORDER. 
    2. PRINT EACH LINE OF A FILE IN REVERSE ORDER. 
        SAMPLE INPUT: PYTHON PROGRAMMING 
        SAMPLE OUTPUT: PROGRAMMING PYTHON 
    3.  DISPLAY THE CONTENT OF FILE A WITHOUT WHITESPACES. 
    4. CONCATENATION OF TWO FILES
    5. EXIT ''')
while True:
    file = open(File_name1, "r")
    a = file.readline()
    b = int(input("ENTER YOUR CHOICE : "))
    if b == 1:
        print("REVERSE ORDER IN EACH WORD : ", reverseWord(a))
    elif b == 2:
        reverseLine(a)
        print()
    elif b == 3:
        WithoutSpace(a)
        print()
    elif b == 4:
        File_name2 = input("ENTER THE FILE NAME : ")
        FileCreate(File_name2)
        file = open(File_name1, "r")
        print("SECOND TEXT FILE CONTENT : ", file.readline())
        filenames = [File_name1, File_name2]
        Concatenation(filenames)
    elif b == 5:
        exit(0)
    else:
        break
