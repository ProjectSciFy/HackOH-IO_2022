class Car:
    def __init__(self, location, speed, direction, size):
        self.size = size
        self.context = None
        self.state = (location, speed, direction)
        self.start = (0, 0)
        self.goal = (800,600)
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
