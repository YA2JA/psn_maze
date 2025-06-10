# Initialize devices
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Stop

# Initialize devices
try:
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    gyro = GyroSensor(Port.S3, Direction.CLOCKWISE)
    wheel_diameter = 56
    axle_track = 320
    SPEED = -70
except:
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.B)
    gyro = GyroSensor(Port.S3, Direction.CLOCKWISE)
    wheel_diameter = 48
    axle_track = 230
    SPEED = 70


ev3 = EV3Brick()
robot = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track)
