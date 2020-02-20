input_file = "input/a_example.txt"

#stores 
with open(input_file,"r") as fileObj:
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
            x_int = [int(i/2), int(x[0]), int(x[1]), int(x[2])]
            libraries.append(x_int)
        else:
            x = a[i].split()
            y = []
            for i in x:
                y.append(int(i))
            books.append(y)

    print(libraries)
    print(books)

def algorithm(book_num,lib_num,scan_days,libraries,books,book_scores) : 
    #only book_num of books can be sent
    #book_num is length of book_scores
    #get total book score for all books in each library, order by them
    




    #returns a list of lists op_libs containing lib_index, num of books for scanning. op_books contains books sent for scanning
    return op_libs,op_books




def write(filename,num_libs,libraries,books): 
    with open(filename,'w') as fileObj : 
        fileObj.write(str(num_libs)+"\n")

        for i in range(len(libraries)) : 
            if(i%2==0):
                fileObj.write(str(libraries[i][0]) +" "+ str(libraries[1]+"\n"))
            else:
                for j in range(0,len(books[i])):
                    if(j==len(books[i])-1):
                        fileObj.write(str(books[i][j]+"\n"))
                    else:
                        fileObj.write(str(books[i][j]+" "))


