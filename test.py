import car as CAR
import random

def setup():
    with open("1c_1l.txt") as f:
        input = f.readlines()
    num = int(input[0])
    lanes = int(input[1])
    location = (800, 300)
    speed = 20
    direction = "W"
    size = (20, 20)
    lane_left_to_right = (30, 315 + 30 * (int(lanes) - 1), 285 - 30 * (int(lanes) - 1))
    cars = list()
    temp = 0
    for i in range(num):
        lane = random.randrange(int(lanes))
        tempCar = CAR.Car((location[0], location[1] - (lane * 30)), speed, direction, lane, size, i, lanes, lane_left_to_right)
        tempCar.setRoute((0, 300 - lane_left_to_right[0] * lane))
        cars.append(tempCar)
        tempCar.addCarToAllCars(tempCar)
        print(f"\tStart of car {i}: ", cars[i].getState())
        temp = i
    temp += 1
    # car moving other way:
    tCar = CAR.Car((500, 300), 0, "E", 0, size, temp, lanes, lane_left_to_right)
    tCar.setRoute((800, 300))
    cars.append(tCar)
    tCar.addCarToAllCars(tCar)
    print(f"\tStart of car {temp}: ", cars[temp].getState())
    updateCars(cars, lanes)

def updateCars(cars, lanes):
    iter = 0
    while len(CAR.Car.allCars) > 0 and iter < 50:
        for car in cars:
            temp = car.distAlgo("W", 300, 300, lanes)
            if temp == 69:
                print(f"\tEnd of car {car.key}: ", car.getState())
                break
            elif temp == 10:
                print(f"\tCar {car.key} detected a stopped object on road and stopped at: ", car.getState())
                exit(1)
        iter += 1
            
setup()
