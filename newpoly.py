class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")
b=vehicle()
b.start()
a=car()
a.start()

