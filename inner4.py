
def outer():
    print("inside outer")

    def inner():
        print("inside inner")

    print(id(inner))
    return inner

ret=outer()
print(type(ret))
print(id(ret))
ret()