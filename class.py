class rectangle:
    def area(self):
        height = int(input("Hieght"))
        width = int(input("Width"))
        area = height * width
        print(area)

r = rectangle()
r.area()