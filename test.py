import car as CAR
import os

def setup():
    num = input("Number of cars: \n")
    lanes = input("Number of lanes: \n")
    location = (800, 300)
    speed = 20
    direction = "W"
    size = (20, 20)
    lane_left_to_right = (30, 315 + 30 * int(lanes), 285 + 30 * int(lanes))
    cars = list()
    temp = 0
    for i in range(int(num)):
        tempCar = CAR.Car((location[0] - (int(i) * 100), location[1]), speed, direction, size, i, lane_left_to_right)
        tempCar.setRoute((0, 300))
        cars.append(tempCar)
        tempCar.addCarToAllCars(tempCar)
        print(f"\tStart of car {i}: ", cars[i].getState())
        temp = i
    temp += 1
    # car moving other way:
    # tCar = CAR.Car((0, 300), speed, "E", size, temp)
    # tCar.setRoute((800, 300))
    # cars.append(tCar)
    # tCar.addCarToAllCars(tCar)
    # print(f"\tStart of car {temp}: ", cars[temp].getState())
    updateCars(cars)

def updateCars(cars):
    while len(CAR.Car.allCars) > 0:
        for car in cars:
            temp = car.distAlgo()
            if temp == 69:
                print(f"\tEnd of car {car.key}: ", car.getState())
                break
            
setup()
