from threading import *

obj = Semaphore(1) 

class Car:
    allCars = dict()
    
    def __init__(self, location, speed, direction, size, key):
        # format of roadParams: (direction, lowerBound, upperBound)
        # initially: start on right side, middle of lane and road, towards West
        self.key = key
        self.roadParams = ("W", 300, 300)
        self.size = size
        self.context = None
        self.start = location
        self.state = (location, speed, direction)
        self.start = (800, 300)
        self.goal = (800, 600)
        self.inTransition = False
        self.context = (self.inTransition, [[False, False, False], [True, self, True], [False, False, False]])
    
    def getAllCars(self):
        obj.acquire()
        all_cars = self.allCars
        obj.release()
        return all_cars
    
    def addCarToAllCars(self, car):
        obj.acquire()
        self.allCars[self.key] = car
        obj.release()
        
    def getState(self):
        return self.state
    
    def setState(self, location, speed, direction):
        self.state = (location, speed, direction)
        self.addCarToAllCars(self)
    
    def getContext(self):
        return self.context
        
    def setContext(self, neighbors):
        self.context = (self.inTransition, [[False, False, False], [True, self, True], [False, False, False]])
        for neighbor in neighbors:
            # Bottom Right
            if (-2 * self.state[0][1] <= neighbor.state[0][1] <= -self.state[0][1]) and (self.size[0] <= neighbor.state[0][0] <= 2 * self.size[0]):
                self.context[1][2][2] = neighbor
            # Right
            elif (-self.size[1] <= neighbor.state[0][1] <= self.size[1]) and (self.size[0] <= neighbor.state[0][0] <= 2 * self.size[0]):
                self.context[1][2][1] = neighbor
            # Top Right
            elif (self.size[1] < neighbor.state[0][1] <= 2 * self.size[1]) and (self.size[0] <= neighbor.state[0][0] <= 2 * self.size[0]):
                self.context[1][2][0] = neighbor
            # Top
            elif (self.size[1] < neighbor.state[0][1] <= 2 * self.size[1]) and (-self.size[0] <= neighbor.state[0][0] <= self.size[0]):
                self.context[1][1][0] = neighbor
            # Top Left
            elif (self.size[1] <= neighbor.state[0][1] <= 2 * self.size[1]) and (-2 * self.size[0] <= neighbor.state[0][0] <= -self.size[0]):
                self.context[1][0][0] = neighbor
            # Left
            elif (-self.size[1] <= neighbor.state[0][1] <= self.size[1]) and (-2 * self.size[0] <= neighbor.state[0][0] <= -self.size[0]):
                self.context[1][0][1] = neighbor
            # Bottom Left
            elif (-2 * self.size[1] <= neighbor.state[0][1] <= -self.size[1]) and (-2 * self.size[0] <= neighbor.state[0][0] <= -self.size[0]):
                self.context[1][0][2] = neighbor
            # Bottom
            elif (-2 * self.size[1] <= neighbor.state[0][1] <= -self.size[1]) and (-self.size[0] <= neighbor.state[0][0] <= self.size[0]):
                self.context[1][1][2] = neighbor
        self.addCarToAllCars(self)
        print(self.context)
    
    def getRoute(self):
        return (self.start, self.goal)
    
    def setRoute(self, goal):
        self.goal = goal
        self.addCarToAllCars(self)
    
    def inAccident(self):
        neighbors = self.context[1]
        selfX = self.state[0][0]
        selfY = self.state[0][1]
        maxX = selfX - (self.size[0]/2)
        minX = selfX + (self.size[0]/2)
        maxY = selfY - (self.size[1]/2)
        minY = selfY + (self.size[1]/2)
        for i in range(3):
            for j in range(3):
                if i != j:
                    if type(neighbors[i][j]) == type(self):
                        neighbor = neighbors[i][j]
                        neighborX = neighbor.state[0][0]
                        neighborY = neighbor.state[0][i]
                        maxXn = neighborX - (neighbor.size[0]/2)
                        minXn = neighborX + (neighbor.size[0]/2)
                        maxYn = neighborY - (neighbor.size[1]/2)
                        minYn = neighborY + (neighbor.size[1]/2)
                        # check collision
                        # left column
                        if maxX <= minXn and maxY <= minYn and j == 0 and i == 0:
                            return True
                        elif maxX <= minXn and j == 0 and i == 1:
                            return True
                        elif maxX <= minXn and minY >= maxYn and j == 0 and i == 2:
                            return True
                        # middle column
                        elif maxY <= minYn and j == 1 and i == 0:
                            return True
                        elif minY >= maxYn and j == 1 and i == 2:
                            return True
                        # right column
                        elif minX >= maxXn and maxY <= minYn and j == 2 and i == 0:
                            return True
                        elif minX >= maxXn and j == 2 and i == 1:
                            return True
                        elif minX >= maxXn and minY >= maxYn and j == 2 and i == 2:
                            return True
        return False         
    
    def inBounds(self):
        return (self.state[0][0] >= 0 and self.state[0][0] <= 800 and self.state[0][1] >= 0 and self.state[0][1] <= 600)
        
    def atGoal(self):
        x_goal = self.goal[0]
        y_goal = self.goal[1]
        x_loc = self.state[0][0]
        y_loc = self.state[0][1]
        xSize = self.size[0]/2
        ySize = self.size[1]/2
        return (x_loc - xSize <= x_goal <= x_loc + xSize) and (y_loc - ySize <= y_goal <= y_loc + ySize)
    
    def distAlgo(self, /, roadParams = ("W", 300, 300)):
        self.roadParams = roadParams
        while not self.atGoal() and self.inBounds():
            our_matrix = self.getAllCars()
            self.setContext(our_matrix.values())
            if not self.inTransition:
                if self.inAccident():
                    return -1
                else:
                    location = self.state[0]
                    speed = self.state[1]
                    direction = self.state[2]
                    if direction == "N":
                        newLocation = (location[0], location[1] - speed)
                        self.state = (newLocation, speed, direction)
                        self.addCarToAllCars(self)
                    elif direction == "S":
                        newLocation = (location[0], location[1] + speed)
                        self.state = (newLocation, speed, direction)
                        self.addCarToAllCars(self)
                    elif direction == "W":
                        newLocation = (location[0] - speed, location[1])
                        self.state = (newLocation, speed, direction)
                        self.addCarToAllCars(self)
                    elif direction == "E":
                        newLocation = (location[0] + speed, location[1])
                        self.state = (newLocation, speed, direction)
                        self.addCarToAllCars(self)
                    else:
                        print("<!> ERROR <!>\n")
        return 1
