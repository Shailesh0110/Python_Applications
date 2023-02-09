
def main():
    try:
        print("Enter fisrt no:")
        no1=int(input())
        print("Enter Second no:")
        no2 = int(input())

        Ans = no1 / no2
        print("Divison is :", Ans)

    except ZeroDivisionError:
        print("inside zero divison error")

    except ValueError:
        print("value error")

    except Exception:
        print("inside last except block")

    finally:
        print("inside finaly Block")

if __name__=="__main__":
    main()