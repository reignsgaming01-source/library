from data import l2
def ibook(l1):
    b=input("Enter book name or book number you want to issue:")
    for x,y in l1.items():
        if x==int(b) or y==b:
            d=l1.pop(x)
            print("Here is your book:",d)
            l2[x]=y
            break
    else:
        print("Sorry sir we don't have that book")
    c=input("Enter to continue")
