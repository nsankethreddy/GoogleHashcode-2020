input_file = "input/a_example.txt"

#stores 
with open(input_file,'r') as fileObj:
    book_num,lib_num,scan_days = fileObj.readline().split(" ")
    #keeps scores of books , index is book ID
    scores = fileObj.readline().split(" ")
    scores[len(scores)-1] = scores[len(scores)-1].rstrip('\n')
    #stores  book ID . each index represnts corresponding library in the library multi list
    books = []
    #stores number of books , signup process time in days, and the num of books lib can ship per day
    libraries = []
    a = fileObj.readlines()
    # print(a)
    for i in range(len(a)):
        if(i%2==0):
            x = a[i].rstrip('\n')
            x = x.split(" ")
            for i in range(0,len(x)) : 
                x[i] = int(x[i])
            libraries.append(x)

        else:
            y = (a[i].rstrip('\n'))
            y = y.split(" ")
            for i in range(0,len(y)) : 
                y[i] = int(y[i])
            books.append(y)

print(books)
print(libraries)



