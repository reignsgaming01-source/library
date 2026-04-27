from data import l2
def dbook(l1):
    b=input("Enter number of the book you want to return:")
    c=input("Enter name of the book you want to return:")
    if int(b) in l2:
        l1[int(b)]=c
        d=l2.pop(int(b))
        print("Thank you for returning book")
    else:
        print("Sorry sir, but you have not issued this book from us")
    c=input("Enter to continue")