import car as CAR
import os
import pygame
import time
import car
import random

def runCar(car):
    car.setRoute((0, 300))
    car.distAlgo()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

cars = list()
roads = []
simulation_over = False

dis_width = 800
dis_height  = 600
global_speed = 60

pygame.init()
dis = pygame.display.set_mode((dis_width, dis_width))
font_style = pygame.font.SysFont(None, 50)

def create_roads(direction, lanes, x, y, width):
    if direction == 'vertical':
        if lanes % 2 == 1:
            create_single_road(direction, x, y, width)
            for i in range(1, int(lanes / 2) + 1):
                create_single_road(direction, x + width * i, y, width)
                create_single_road(direction, x - width * i, y, width)
        else:
            for i in range(1, int(lanes / 2) + 1):
                create_single_road(direction, x + width * i - width/2, y, width)
                create_single_road(direction, x - width * i + width/2, y, width)

    else:
        if lanes % 2 == 1:
            create_single_road(direction, x, y, width)
            for i in range(1, int(lanes / 2) + 1):
                create_single_road(direction, x, y + width * i, width)
                create_single_road(direction, x, y - width * i, width)
        else:
            for i in range(1, int(lanes / 2) + 1):
                create_single_road(direction, x, y + width * i - width/2, width)
                create_single_road(direction, x, y - width * i + width/2, width)
                #create_single_road(direction, x + width * i - width/2, y, width)
                ##create_single_road(direction, x - width * i + width/2, y, width)

def create_single_road(direction, x, y, width):
    if direction == 'vertical':
        create_line([x - width/2, 0], [x - width/2, dis_height * 2])
        create_line([x + width/2, 0], [x + width/2, dis_height * 2])
    else:
        create_line([0, y - width/2], [dis_width * 2, y - width/2])
        create_line([0, y + width/2], [dis_width * 2, y + width/2])

def create_line(point_a, point_b):
    roads.append([point_a, point_b])

def draw_roads(roads):
    for road in roads:
        #pygame.draw.rect(dis, black, road)
        a = road[0]
        b = road[1]
        pygame.draw.line(dis, black, a, b, width=5)

def message(msg,color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])

def update(cars):
    for car in cars:
        draw_car(car)

def draw_car(car):
    state = car.getState();
    x = state[0][0]
    y = state[0][1]
    width_scale = 1.5
    height_scale = 1
    color = black
    car_width = car.size[0]
    car_height = car.size[1]
    #pygame.draw.rect(dis, color, [x, y, car_size * width_scale, car_size * height_scale])
    pygame.draw.rect(dis, color, [x, y, car_width, car_height])
def clear_board():
    dis.fill(white)

def update_board():
    pygame.display.update()

def check_input(pygame_events):
    for event in pygame_events:
        if event.type == pygame.QUIT:
            return True

    return False

car_size=30

clock = pygame.time.Clock()
refresh_rate = 60
simulation_over = False



def setup():
    with open("1c_1l_N.txt") as f:
        input = f.readlines()
    num = int(input[0])
    lanes = int(input[1])
    direction1 = str(input[2])
    location = (800, 300)
    if direction1 == "N":
        location = (400, 600)
    speed = 2
    size = (20, 20)
    lane_left_to_right = (30, 315 + 30 * (int(lanes) - 1), 285 - 30 * (int(lanes) - 1))
    cars = list()
    for i in range(num):
        lane = random.randrange(int(lanes))
        tempCar = CAR.Car((location[0], location[1] - (lane * 30)), speed, direction1, lane, size, i, lanes, lane_left_to_right)
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
        tempCar = CAR.Car((location[0], location[1] - (lane * 30)), speed, direction2, lane, size, i, lanes, lane_left_to_right)
        if direction2 == "W":
            tempCar.setRoute((0, 300 - lane_left_to_right[0] * lane))
        if direction2 == "N":
            tempCar.setRoute((400 + lane_left_to_right[0] * lane, 0))
        cars.append(tempCar)
        tempCar.addCarToAllCars(tempCar)
        print(f"\tStart of car {i} heading {direction2}: ", cars[i].getState())
        i += 1
    create_roads('horizotal', int(lanes), location[0], location[1] + size[1] / 2, 40)
    create_roads('vertical', int(lanes), 400 + size[1]/2, location[1] + size[1] / 2, 40)

    updateCars(cars, lanes)

def updateCars(cars, lanes):
    iter = 0
    while len(CAR.Car.allCars) > 0 and iter < 800:
        for car in cars:
            temp = car.distAlgo(car.getState()[2], 300, 300, lanes)
            if temp == 69:
                print(f"\tEnd of car {car.key}: ", car.getState())
                break
            elif temp == 10:
                print(f"\tCar {car.key} detected a stopped object on road and stopped at: ", car.getState())
                exit(1)
        iter += 1


        # while not simulation_over:
        #simulation_over = check_input(pygame.event.get())

        clear_board()
        update(cars)
        draw_roads(roads)
        update_board()

        clock.tick(refresh_rate)

    message("Simulation Over",red, 200, 200)
    pygame.display.update()
    time.sleep(0.2)
    pygame.quit()
    quit()


setup()
