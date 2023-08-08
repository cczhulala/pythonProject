class Duck:
    speed = 30

    def fly(self):
        return "Flying at {} kmph".format(self.speed)


class MallardDuck(Duck):
    speed = 20


if __name__ == "__main__":
    duck = Duck()
    print(duck.fly())

    mallard = MallardDuck()
    print(mallard.fly())
