import car

location = (800, 300)
speed = 50
direction = "W"
size = (40, 20)
first = car.Car(location, speed, direction, size)
first.setRoute((0, 300))
first.distAlgo()
first.setRoute((500,300))
print(first.getState()[0])
print(first.state[0])
first.state[0] = (500,300)
print(first.getState()[0])
print(first.state[0])
print("end")
