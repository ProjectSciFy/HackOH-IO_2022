import car as CAR
import os


def runCar(car):
    car.setRoute((0, 300))
    car.distAlgo()

num = input("Number of cars: \n")
location = (800, 300)
speed = 50
direction = "W"
size = (40, 20)
cars = list()
amFather = False
children = []
for i in range(int(num)):
    cars.append(CAR.Car((location[0] - (int(i) * 50), location[1]), speed, direction, size))
    print(f"\tStart of car {i + 1}: ", cars[i].getState())

for car in cars:
    pid = os.fork()
    if pid > 0:
        amFather = True
    else:
        children.append(pid)
        runCar(car)
        print(f"\tEnd state of a car: ", car.getState())
        exit(0)
        

if amFather:
    for child in children:
        os.waitpid(child, 0)
        
