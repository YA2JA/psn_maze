from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from pybricks.robotics import DriveBase
from local_type import Vector

from .conf import left_motor, right_motor, gyro

# Initialize devices
ev3 = EV3Brick()
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=320)

# Calibration
gyro.reset_angle(0)

# Constants
SQUARE_LENGTH_MM = 300  # Length of one square in mm

# Global state
current_angle = 0  # In degrees, 0 = North, 90 = East, etc.

def go_straight_smart(distance_mm, speed=-100):
    """Goes straight using gyro for correction"""
    target_angle = gyro.angle()
    robot.reset()
    print("target angle:", target_angle, "current_angle:", current_angle)
    while abs(robot.distance()) < abs(distance_mm):
        print("distance ", robot.distance(),  distance_mm)
        error = target_angle - gyro.angle()
        correction = error * 50  # Tunable coefficient
        robot.drive(speed, correction)
        wait(20)
    robot.stop(Stop.BRAKE)

def turn_to(target_direction):
    """Turns robot to absolute target angle (0 = North, 90 = East, etc.)"""
    global current_angle
    diff = (target_direction - current_angle) % 360
    if diff > 180:
        diff -= 360  # Choose shortest rotation
    robot.turn(diff)
    current_angle = target_direction

def move(vec:Vector):
    """Moves to target coordinate (x, y) in grid."""
    dx = vec.x
    dy = vec.y
    # Move in X direction
    if dx != 0:
        target_angle = 90 if dx > 0 else 270
        turn_to(target_angle)
        go_straight_smart(abs(dx) * SQUARE_LENGTH_MM)

    # Move in Y direction
    if dy != 0:
        target_angle = 0 if dy > 0 else 180
        turn_to(target_angle)
        go_straight_smart(abs(dy) * SQUARE_LENGTH_MM)