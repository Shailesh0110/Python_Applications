from sys import *


def add(A,B):
    ans=0
    ans=A+B
    return  ans

def main():
    print('application Name: ', argv[0])

    if (len(argv)!=3):
        print('invalied sentance')
        exit()
    else:
        Ret=add(int(argv[1]),int(argv[2]))
        print(Ret)
print("Application is devloped by Shailesh Nikam")
if __name__ == "__main__":
        main()