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
    num = input("Number of cars: \n")
    lanes = input("Number of lanes: \n")
    location = (800, 300)
    speed = 5
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

    create_roads('horizotal', int(lanes), location[0], location[1] + size[1] / 2, 40)
    updateCars(cars)

def updateCars(cars):
    while len(CAR.Car.allCars) > 0:
        for car in cars:
            temp = car.distAlgo()
            if temp == 69:
                print(f"\tEnd of car {car.key}: ", car.getState())
                break




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
