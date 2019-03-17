class Sea_Food:
    def swim(self):
        print("\nCan Swim Very Fast")

class rohu(Sea_Food):
    pass

class katla(Sea_Food):
    def jump(self):
        print("Can Jump a Way High The Ground")

r = rohu()
r.swim()

k = katla()
k.jump()
k.swim()