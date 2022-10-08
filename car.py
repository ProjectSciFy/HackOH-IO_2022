class Car:
    def __init__(self, location, speed, direction, size):
        # format of roadParams: (direction, lowerBound, upperBound)
        # initially: start on right side, middle of lane and road, towards West
        self.roadParams = ("W", 300, 300)  
        self.size = size
        self.context = None
        self.state = (location, speed, direction)
        self.start = (800, 300)
        self.goal = (800, 600)
        self.inTransition = False
        self.context = (50, self.inTransition, [[False, False, False], [True, self, True], [False, False, False]])
        
    def getState(self):
        return self.state
    
    def setState(self, location, speed, direction, size):
        self.size = size
        self.state = (location, speed, direction)
    
    def getContext(self):
        return self.context
        
    def setContext(self, speedLimit, neighbors):
        self.context = (speedLimit, self.inTransition, neighbors)
        
    def getRoute(self):
        return (self.start, self.goal)
    
    def setRoute(self, start, goal):
        self.start = start
        self.goal = goal
        
    def inAccident(self):
        neighbors = self.context[2]
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
        
    # fun!
    def distAlgo(self, roadParams):
        self.roadParams = roadParams
        if not self.inTransition:
            if self.inAccident():
                exit
            else:
                location = self.state[0]
                speed = self.state[1]
                direction = self.state[2]
                if direction == "N":
                    newLocation = (location[0], location[1] - speed)
                    self.setState = (newLocation, speed, direction)
                elif direction == "S":
                    newLocation = (location[0], location[1] + speed)
                    self.setState = (newLocation, speed, direction)
                elif direction == "W":
                    newLocation = (location[0] - speed, location[1])
                    self.setState = (newLocation, speed, direction)
                elif direction == "E":
                    newLocation = (location[0] + speed, location[1])
                    self.setState = (newLocation, speed, direction)
                else:
                    print("<!> ERROR <!>\n")
