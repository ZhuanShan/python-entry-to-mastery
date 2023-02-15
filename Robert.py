mylist = {"My":1234, "Name":5678, "is":9000}

test = ""

while test != "q":
    test = input("enter")

    if(test in mylist):

        print(mylist[test])

    else:
        print("no")
           
