
def Display(no):
    if no>0:
        no=no-1
        Display(no)
        print(no)

Display(4)