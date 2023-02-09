#import Numbers
#from Numbers import Displayfactor
import Numbers as NUM

def Main():
    print("Enter no: ")
    No=int(input())

    NUM.Displayfactor(No)

if __name__=="__main__":
    Main()