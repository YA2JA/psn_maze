#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Constants (tune these based on your robot)
WHEEL_DIAMETER = 56    # mm
AXLE_TRACK = 138       # mm
MOVE_DISTANCE = 345    # mm (positive = forward)
TURN_ANGLE = 90        # degrees
GYRO_GAIN = 3        # Correction sensitivity (higher = stronger correction)
TURN_TOLERANCE = 5     # Degrees of error tolerance

# Initialize components
ev3 = EV3Brick()
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)  # Verify directions
right_motor = Motor(Port.B, Direction.CLOCKWISE)
gyro = GyroSensor(Port.S3)
robot = DriveBase(left_motor, right_motor, 
                 wheel_diameter=WHEEL_DIAMETER, 
                 axle_track=AXLE_TRACK)

gyro.reset_angle(0)
wait(500)  # Allow gyro to stabilize

# ---- Improved Movement Functions ----
def move_straight(distance, speed=150):
    """Move straight with gyro correction using PID control"""
    target_angle = gyro.angle()
    robot.reset()
    
    while abs(robot.distance()) < abs(distance):
        error = target_angle - gyro.angle()
        steering = GYRO_GAIN * error
        robot.drive(speed, steering)
        wait(10)
    
    robot.stop()

def turn_to_angle(target_angle, turn_speed=100):
    while abs(gyro.angle() - target_angle) > TURN_TOLERANCE:
        error = target_angle - gyro.angle()
        # Proportional controller with min speed
        speed = max(10, min(100, abs(error) * 0.8)) 
        direction = 1 if error > 0 else -1
        robot.drive(0, direction * speed)
        wait(10)
    robot.stop()

def turn_relative(angle):
    target = gyro.angle() + angle
    turn_to_angle(target)

def move_in_direction(direction_vector):
    current_angle = gyro.angle()
    
    if direction_vector.x != 0:
        target_angle = 0 if direction_vector.x > 0 else 180
    else:
        target_angle = 90 if direction_vector.y > 0 else 270
    
    # Calculate turn needed
    angle_diff = (target_angle - current_angle + 180) % 360 - 180
    turn_relative(angle_diff)
    
    # Move straight after alignment
    move_straight(MOVE_DISTANCE)