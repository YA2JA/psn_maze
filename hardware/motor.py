#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

from local_type import Vector

ANGLE = 140
MOVE_CASE = 350

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

robot = DriveBase(
                    left_motor, 
                    right_motor, 
                    wheel_diameter = 43,
                    axle_track=138
                )

def turn_right():
    robot.turn(ANGLE)

def turn_left():
    robot.turn(-ANGLE)

def turn_around():
    turn_left()
    turn_left()

class RobotMovement:
    
    def __init__(self, angle:int):
        self.angle = angle

    def set_angle(self, vec:Vector):
        # Handle x-axis movement
        if vec.x == 1:  # Move right
            if self.angle == 90:
                turn_right()
            elif self.angle == 180:
                turn_around()
            elif self.angle == 270:
                turn_left()
            self.angle = 0
        
        elif vec.x == -1:  # Move left
            if self.angle == 0:
                turn_around()
            elif self.angle == 90:
                turn_left()
            elif self.angle == 270:
                turn_right()
            self.angle = 180
        
        # Handle y-axis movement
        elif vec.y == 1:  # Move up
            if self.angle == 0:
                turn_left()
            elif self.angle == 180:
                turn_right()
            elif self.angle == 270:
                turn_around()
            self.angle = 90
        
        elif vec.y == -1:  # Move down
            if self.angle == 0:
                turn_right()
            elif self.angle == 90:
                turn_around()
            elif self.angle == 180:
                turn_left()
            self.angle = 270
    
    def move_forward(self):
        robot.straight(MOVE_CASE)