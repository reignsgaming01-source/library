def fbook(l1):
    b=input("Enter book name or book number you want to find:")
    for x,y in l1.items():
        if str(x)==b or y==b:
            print("We have the book you are looking for:",y)
            c=input("Enter to continue")