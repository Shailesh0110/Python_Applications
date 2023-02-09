

def Display(no):
    if no>0:  # condition
        print("Hello")
        no=no-1
        Display(no) # recursive fuction call
Display(4) # fuction call