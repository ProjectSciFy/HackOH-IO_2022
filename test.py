import car as CAR
import os

def setup():
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
        tempCar = CAR.Car((location[0] - (int(i) * 100), location[1]), speed, direction, size, i)
        tempCar.setRoute((0, 300))
        cars.append(tempCar)
        CAR.Car.addCarToAllCars(tempCar, tempCar)
        print(f"\tStart of car {i}: ", cars[i].getState())
        temp = i
        # for i in CAR.Car.allCars.keys():
        #     print(i, CAR.Car.allCars[i].getState())
    temp += 1
    # car moving other way:
    # cars.append(CAR.Car((700, 300), 50, "W", size))
    # print(f"\tStart of car {temp + 1}: ", cars[temp].getState())
    updateCars(cars)

def updateCars(cars):
    while len(CAR.Car.allCars) > 0:
        for car in cars:
            temp = car.distAlgo()
            if temp == 69:
                print(f"\tEnd of car {car.key}: ", car.getState())
                break
            
setup()
