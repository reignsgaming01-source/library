from data import l3
def dobook(l1):
    b=int(input("Enter number of the book:"))
    c=input("Enter name of the book:")
    if b not in l1:
        l1[b]=c
        l3.append(c)
    else:
        print("Sorry the same book number already exist!")
    n=input("Enter to continue")