# Team: the bois
# Authors: Abhishek Das, Bhargav SNV, N Sanketh Reddy, Rama Krishna Siddharth V
# Final Score: 21,465,662

path = "./" #Change path accordingly
filenames = ["a_example", "b_read_on", "c_incunabula", "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]

for X in filenames:
    file = path + "/input/" + X
    with open(file + ".txt", "r") as fileObj:
        B,L,D = fileObj.readline().split()
        B = int(B)
        L = int(L)
        D = int(D)
        s = fileObj.readline().split()
        print(B,L,D)
        scores = [int(i) for i in s]
        books = []

        libraries = []
        a = fileObj.readlines()
        x = []
        y =[]
        for i in range(len(a)):
            if(i%2==0):
                x = a[i].split()
                x_int = [int(i)/2, int(x[0]), int(x[1]), int(x[2])]
                libraries.append(x_int)
            else:
                x = a[i].split()
                y = []
                for i in x:
                    y.append(int(i))
                books.append(y)

    def takeSecond(elem):
        return elem[2]

    libraries.sort(key=takeSecond)

    sum = 0
    for i in range(len(libraries)):
        sum+=libraries[i][2]
        if(sum > D):
            last_lib_id = i - 1
            break
        last_lib_id = i

    libraries = libraries[:last_lib_id+1:]
    num_libs = len(libraries)


    books_to_scan = []
    cumulative_days = 0


    def bookScore(elem):
        return scores[elem]

    for i in libraries:
        cumulative_days += i[2]
        days_left = D - cumulative_days
        max_books = days_left * i[3]
        books_in_lib = books[i[0]]
        books_in_lib.sort(key=bookScore, reverse=True)

        if(len(books_in_lib) <= max_books):
            books_to_scan.append(books_in_lib)
        else:
            temp = []
            for j in range(0,len(books_in_lib)):
                if(j <= max_books):
                    temp.append(books_in_lib[j])
            books_to_scan.append(temp)

    file = path + "/output/" + X
    with open(file + "_output.txt","w") as f:
        f.write(str(num_libs)+"\n")
        for i in range(len(libraries)):
            f.write(str(libraries[i][0])+" "+str(len(books_to_scan[i]))+"\n")
            s = ""
            for j in books_to_scan[i]:
                s = s + str(j) + " "
            f.write(s + "\n")
