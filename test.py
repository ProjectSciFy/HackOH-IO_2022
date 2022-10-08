import car

location = (800, 300)
speed = 50
direction = "W"
size = (40, 20)
first = car.Car(location, speed, direction, size)
first.setRoute((0, 300))
first.distAlgo()
print("end")
print(first.getState())
