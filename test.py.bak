import car as CAR
import os

def runCar(car):
    car.setRoute((0, 300))
    car.distAlgo()

num = input("Number of cars: \n")
location = (800, 300)
speed = 20
direction = "W"
size = (20, 20)
cars = list()
amFather = False
children = []
temp = 0
for i in range(int(num)):
    tempCar = CAR.Car((location[0] - (int(i) * 80), location[1]), speed, direction, size, i)
    cars.append(tempCar)
    CAR.Car.addCarToAllCars(tempCar, tempCar)
    print(f"\tStart of car {i + 1}: ", cars[i].getState())
    temp = i
    # for i in CAR.Car.allCars.keys():
    #     print(i, CAR.Car.allCars[i].getState())
temp += 1
# car moving other way:
# cars.append(CAR.Car((700, 300), 50, "W", size))
# print(f"\tStart of car {temp + 1}: ", cars[temp].getState())

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
        
