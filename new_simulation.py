import pygame
import time
import car
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800
dis_height  = 600
dis = pygame.display.set_mode((dis_width, dis_width))

simulation_over = False
global_speed = 60
cars = []
roads = []

font_style = pygame.font.SysFont(None, 50)

def message(msg,color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [x, y])

def create_road(roads, direction, lanes, x, y):
    #road = [x, y, car_size * width_scale, car_size * height_scale]
    #road = [x, 0, 10, dis_width]
    if direction == 'vertical':
        road = [[x, 0], [x, dis_height * 2]]
        roads.append(road)

        for i in range(1, int(lanes / 2) + 1):
            road = [[x - 50 * i, 0], [x - 50 * i, dis_height * 2]]
            roads.append(road)
            road = [[x + 50 * i, 0], [x + 50 * i, dis_height * 2]]
            roads.append(road)
    else:
        road = [[0, y], [dis_width * 2, y]]
        roads.append(road)

        for i in range(1, int(lanes / 2) + 1):
            road = [[0, y - 50 * i], [dis_width * 2, y - 50 * i]]
            roads.append(road)
            road = [[0, y + 50 * i], [dis_width * 2, y + 50 * i]]
            roads.append(road)



def spawn_car(cars, speed, location, lane):
    width_scale = 1
    height_scale = 1
    offset = car_size / 2
    if location == 'bottom':
        speeds = [0, -1 * speed ]
        x = dis_width/2 - offset
        x = x + 25 + (50 * lane)
        y = dis_height - 3
        height_scale = 1.5
    elif location == 'top':
        speeds = [0, speed]
        x = dis_width / 2 - offset
        x = x - 25 - (50 * lane)
        y = 3
        height_scale =  1.5
    elif location == 'left':
        speeds = [speed, 0]
        x = 3
        y = dis_height / 2 - offset
        y = y - 25 - (50 * lane)
        width_scale =  1.5
    elif location == 'right':
        speeds = [-1 * speed, 0]
        x = dis_width - 3
        y = dis_height / 2 - offset
        y = y + 25 + (50 * lane)
        width_scale =  1.5

    color = (random.random() * 255, random.random() * 255, random.random() * 255)

    car = [x, y, speeds, width_scale, height_scale, color]
    cars.append(car)

def update(cars):
    for car in cars:
        update_position(car)
        draw_car(car)
        #draw_text(car)

def update_position(car):
    #car[1] = car[1] + (car[2] / refresh_rate) * 10
    speeds = car[2]
    car[0] = car[0] + (speeds[0]/refresh_rate)*10
    car[1] = car[1] + (speeds[1]/refresh_rate)*10
    #car[0] = car[0] + (car[2] / refresh_rate) * 10

def draw_car(car):
    x = car[0]
    y = car[1]
    width_scale = car[3]
    height_scale = car[4]
    color = car[5]
    pygame.draw.rect(dis, color, [x, y, car_size * width_scale, car_size * height_scale])

def draw_text(car):
    x = car[0] + 40
    y = car[1] - 40
    text = "" + str(abs(car[2][0] + car[2][1]))
    message(text ,red,x ,y)
def draw_roads(roads):
    for road in roads:
        #pygame.draw.rect(dis, black, road)
        a = road[0]
        b = road[1]
        pygame.draw.line(dis, black, a, b, width=5)

def clear_board():
    dis.fill(white)

def update_board():
    pygame.display.update()

directions = ['bottom', 'top', 'right', 'left']

def check_input(pygame_events):
    for event in pygame_events:
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                r = int(random.random() * (4))
                dir = directions[r]
                lane = int(random.random() * (4))
                #spawn_car(cars, global_speed, dir, lane)
                #spawn_car(cars, int(random.random() * (150)) + 20, dir, lane)
            #
            # if event.key == pygame.K_UP:
            #     spawn_car(cars, global_speed, 'bottom', 0)
            # elif event.key == pygame.K_DOWN:
            #     spawn_car(cars, global_speed, 'top', 0)
            # elif event.key == pygame.K_LEFT:
            #     spawn_car(cars, global_speed, 'right', 0)
            # elif event.key == pygame.K_RIGHT:
            #     spawn_car(cars, global_speed, 'left', 0)
    r = int(random.random() * (4))
    dir = directions[r]
    lane = int(random.random() * (4))
    spawn_car(cars, int(random.random() * (150)) + 20, dir, lane)

    return False

car_size=30

clock = pygame.time.Clock()
refresh_rate = 60

create_road(roads, 'vertical', 8,  dis_width/2, dis_height/2)
create_road(roads, 'horizontal', 8,  dis_width/2, dis_height/2)

while not simulation_over:
    simulation_over = check_input(pygame.event.get())

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
