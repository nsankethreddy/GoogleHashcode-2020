print("Hello")
path = "/root/docs/GoogleHashcode-2020/"
with open(path + "a_example.txt","r") as fileObj:
    '''
    print("Opened")
    first_line = f.readline()
    first_line = first_line.split()
    B = int(first_line[0])
    L = int(first_line[1])
    D = int(first_line[2])
    second_line = f.readline()
    second_line = second_line.split()
    '''
    book_num,lib_num,scan_days = fileObj.readline().split(" ")
    #keeps scores of books , index is book ID
    scores = fileObj.readline().split(" ")
    scores[len(scores)-1] = scores[len(scores)-1].rstrip('\n')
    #stores  book ID . each index represnts corresponding library in the library multi list
    books = []
    #stores number of books , signup process time in days, and the num of books lib can ship per day
    libraries = []
    a = fileObj.readlines()
    print(a)
    x = []
    y =[]
    for i in range(len(a)):
        if(i%2==0):
            x = a[i].split()
            x_int = [int(i), int(x[0]), int(x[1]), int(x[2])]
            libraries.append(x_int)
        else:
            x = a[i].split()
            y = []
            for i in x:
                y.append(int(i))
            books.append(y)

print(books)
print(libraries)
