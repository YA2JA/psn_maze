# Initialize devices
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Stop

try:
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    gyro = GyroSensor(Port.S3, Direction.CLOCKWISE)
except:
    left_motor = Motor(Port.A)
    right_motor = Motor(Port.B)
    gyro = GyroSensor(Port.S1)