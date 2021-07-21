def decorator(func):
    def decorated(width, heigth):
        func(width, heigth)
        if width > 0 and heigth >0:
            return func(width, heigth)
        else:
            print('error')
    return decorated


@decorator
def triangle(width, heigth):
    print(width*heigth/2)
@decorator
def square(width, heigth):
    print(width*heigth)


triangle(5,4)

