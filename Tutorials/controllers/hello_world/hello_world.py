from controller import Robot

robot = Robot()

while robot.step(32) != -1:
    print("Hello World!")
   