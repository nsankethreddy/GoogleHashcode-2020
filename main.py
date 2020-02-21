input_file = "input/b_read_on.txt"

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
    # print(a)
    x = []
    y =[]
    for i in range(len(a)-1):
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


    # print(libraries)
    # print(books)
    # print(scores)

def algorithm(book_num,lib_num,scan_days,libraries,books,book_scores) : 
    #only book_num of books can be sent
    #book_num is length of book_scores
    #get total book score for all books in each library, order by them
    # print(libraries)
    lib_old1 = libraries
    lib_old2 = libraries

    libraries.sort(key = book_score_func)
    lib_sorted_score = libraries
    lib_old1.sort(key = signup_func)
    lib_sorted_signup = lib_old1
    # print(lib_sorted_score)
    # print(lib_sorted_signup)

    #get half of the libraries based on signup time in asc
    lib_sorted_signup_half = []
    for i in range(0,len(lib_sorted_signup)/2) : 
        lib_sorted_signup_half.append(lib_sorted_signup[i])
    
    lib_sorted_signup_half.sort(key = signup_density,reverse = True)
    # print(lib_sorted_signup_half)

    op_libs = []
    op_books = []
    #lib_index will be ordered by signup density factor
    for i in range(0,len(lib_sorted_signup_half)):
        op_libs.append([lib_sorted_signup_half[i][0],2])
        book_list = [int(scores[i]) for i in books[lib_sorted_signup_half[i][0]]]
        book_list.sort(reverse = True)             

        op_books.append([book_list[0],book_list[1]])

    print(op_libs)
    print(op_books)
    write("asf.txt",len(lib_sorted_signup_half),op_libs,op_books)
    #returns a list of lists op_libs containing lib_index, num of books for scanning. op_books contains books sent for scanning
    return op_libs,op_books

#takes every element in library as argument
def book_score_func(elem) : 
    l = [int(scores[i]) for i in books[elem[0]]]
    # print(sum(l))
    return sum(l)

def signup_func(elem):
    return elem[2]

def signup_density(elem) : 
    l = [int(scores[i]) for i in books[elem[0]]]
    m = sum(l)*elem[3]/elem[2]
    return m
    # m = m/

def write(filename,num_libs,libraries,books): 
    with open(filename,'w') as fileObj : 
        fileObj.write(str(num_libs)+"\n")

        for i in range(len(libraries)) : 
            # print(libraries)
            if(i%2==0):
                fileObj.write(str(libraries[i][0]) +" "+ str(libraries[i][1])+"\n")
            else:
                for j in range(0,len(books[i])):
                    if(j==len(books[i])-1):
                        fileObj.write(str(books[i][j])+"\n")
                    else:
                        fileObj.write(str(books[i][j])+" ")


algorithm(book_num,lib_num,scan_days,libraries,books,scores)