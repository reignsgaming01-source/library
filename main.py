from show import slib
from find import fbook
from issue import ibook
from ret import dbook
from donate import dobook
from data import l1,l3
while True:
    print("Book number 1-100")
    if l3!=[]:
        print("list of doanted books:",l3)
    print("Enter\n1:Show all books \n2:Find a book\n3:Issue book\n4:Return book\n5:Donate book\n6:Exit")
    a=int(input("Enter your choice: "))
    if a ==1:
        slib(l1)
    elif a==2:
        fbook(l1)
    elif a==3:
        ibook(l1)
    elif a==4:
        dbook(l1)
    elif a==5:
        dobook(l1)
    elif a==6:
        break
print("Thank you")
