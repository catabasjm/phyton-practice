# objects as arguments
class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcycle()

change_color(car_1, 'yellow')
change_color(car_2, 'blue')
change_color(bike_1, 'red')

print(car_1.color)
print(bike_1.color)