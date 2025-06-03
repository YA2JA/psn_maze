#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

obstacle_sensor = UltrasonicSensor(Port.S4)
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=43, axle_track=138)

def detect_obstacle():
    distance = obstacle_sensor.distance()
    if distance < 300:
        ev3.screen.draw_text(50, 50, "Obstacle!")
        return True
    return False

def move_safe(distance):
    if not detect_obstacle():
        robot.straight(distance)
    else:
        robot.stop()
