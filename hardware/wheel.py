from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

from .conf import left_motor, right_motor

# Reset angles
left_motor.reset_angle(0)
right_motor.reset_angle(0)

# Move both motors forward 360 degrees
left_motor.run_target(100, 360, wait=False)
right_motor.run_target(100, 360)