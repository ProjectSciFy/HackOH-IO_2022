class Car:
    def __init__(self, location, speed, direction, size):
        self.location = location
        self.speed = speed
        self.direction = direction
        self.size = size
        self.context = None
        self.state = (self.location, self.speed, self.direction, self.size)
        self.speedLimit = 50
        self.start = (0, 0)
        self.goal = (800,600)
        self.inTransition = False
        self.neighbors = [[False, False, False], [True, self, True], [False, False, False]]
        self.context = (self.speedLimit, self.start, self.goal, self.inTransition, self.neighbors)
        
    def getState(self):
        return self.state
    
    def setState(self, location, speed, direction, size):
        self.location = location
        self.speed = speed
        self.direction = direction
        self.size = size
        self.state = (self.location, self.speed, self.direction, self.size)
    
    def getContext(self):
        return self.context
        
    def setContext(self, speedLimit, start, goal, neighbors):
        self.speedLimit = speedLimit
        self.start = start
        self.goal = goal
        self.inTransition = False
        self.neighbors = neighbors
        self.context = (self.speedLimit, self.start, self.goal, self.inTransition, self.neighbors)
        
    def getSpeedLimit(self):
        return self.speedLimit
