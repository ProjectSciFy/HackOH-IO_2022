'''
NOTE THAT THIS FILE DOES NOT RUN THE MOST CURRENT CODE--LOOK AT 'sim.py'.
'''


import car as CAR
import random

def setup():
    with open("1c_1l_N.txt") as f:
        input = f.readlines()
    num = int(input[0])
    lanes = int(input[1])
    direction1 = str(input[2])
    location = (800, 300)
    if direction1 == "N":
        location = (400, 600)
    speed = 6
    size = (20, 20)
    lane_left_to_right = (30, 315 + 30 * (int(lanes) - 1), 285 - 30 * (int(lanes) - 1))
    cars = list()
    for i in range(num):
        lane = random.randrange(int(lanes))
        tempCar = CAR.Car((location[0], location[1] - (i * 180)), speed/2, direction1, lane, size, i, lanes, lane_left_to_right)
        if direction1 == "W":
            tempCar.setRoute((0, 300 - lane_left_to_right[0] * lane))
        if direction1 == "N":
            tempCar.setRoute((400 + lane_left_to_right[0] * lane, 0))
        cars.append(tempCar)
        tempCar.addCarToAllCars(tempCar)
        print(f"\tStart of car {i} heading {direction1}: ", cars[i].getState())
    temp = num
    # car stopped in West lane:
    tCar = CAR.Car((100, 300), 0, "W", 0, size, temp, lanes, lane_left_to_right)
    tCar.setRoute((0, 300))
    cars.append(tCar)
    tCar.addCarToAllCars(tCar)
    print(f"\tStart of car {temp} heading W: ", cars[temp].getState())

    with open("1c_1l_W.txt") as f:
        input = f.readlines()
    num = int(input[0])
    lanes = int(input[1])
    direction2 = str(input[2])
    location = (800, 300)
    if direction2 == "N":
        location = (400, 600)
    i = temp + 1
    while i < num + temp + 1:
        lane = random.randrange(int(lanes))
        tempCar = CAR.Car((location[0] - 80 * (i - 1), location[1] - (lane * 30)), int(speed / int(i/2)), direction2, lane, size, i, lanes, lane_left_to_right)
        if direction2 == "W":
            tempCar.setRoute((0, 300 - lane_left_to_right[0] * lane))
        if direction2 == "N":
            tempCar.setRoute((400 + lane_left_to_right[0] * lane, 0))
        cars.append(tempCar)
        tempCar.addCarToAllCars(tempCar)
        print(f"\tStart of car {i} heading {direction2}: ", cars[i].getState())
        i += 1
    updateCars(cars, lanes)

def updateCars(cars, lanes):
    iter = 0
    while len(CAR.Car.allCars) > 0 and iter < 1000:
        for car in cars:
            temp = car.distAlgo(car.getState()[2], 300, 300, lanes)
            if temp == 69:
                print(f"\tEnd of car {car.key}: ", car.getState())
                break
            elif temp == 10:
                print(f"\tCar {car.key} detected a stopped object on road and stopped at: ", car.getState())
                break
        iter += 1
            
setup()
