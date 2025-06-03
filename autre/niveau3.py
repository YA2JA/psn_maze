#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from local_type import Vector

ANGLE = 135
MOVE_CASE = 345

ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, wheel_diameter=43, axle_track=138)

def turn_right():
    robot.turn(ANGLE)

def turn_left():
    robot.turn(-ANGLE)

def turn_around():
    turn_left()
    turn_left()

def move(self, vec:Vector, angle=[0]):
    if vec.x == 1:
        if self.angle == 90:
            turn_right()
        elif self.angle == 180:
            turn_around()
        elif self.angle == 270:
            turn_left()
        angle[0] = 0
    elif vec.x == -1:
        if self.angle == 0:
            turn_around()
        elif self.angle == 90:
            turn_left()
        elif self.angle == 270:
            turn_right()
        angle[0] = 180
    elif vec.y == 1:
        if self.angle == 0:
            turn_left()
        elif self.angle == 180:
            turn_right()
        elif self.angle == 270:
            turn_around()
        angle[0] = 90
    elif vec.y == -1:
        if self.angle == 0:
            turn_right()
        elif self.angle == 90:
            turn_around()
        elif self.angle == 180:
            turn_left()
        angle[0] = 270
    robot.straight(MOVE_CASE)
