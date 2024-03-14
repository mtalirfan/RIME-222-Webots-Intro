"""epuck_go_forward controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor

TIME_STEP = 64

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
# timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    # left_motor.setPosition(10.0)
    # right_motor.setPosition(float(10.0))

    left_motor.setPosition(float("inf"))
    right_motor.setPosition(float("inf"))

    left_motor.setVelocity(0.5 * MAX_SPEED)
    right_motor.setVelocity(0.5 * MAX_SPEED)
    pass

# Enter here exit cleanup code.
