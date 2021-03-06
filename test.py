#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                    SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time
lift=Motor(Port.A)
left=Motor(Port.C)
right=Motor(Port.B)
axle_track=114
diameter=54
light_sensor = ColorSensor(Port.S1)
light_sensor2 = ColorSensor(Port.S2)
robot = DriveBase(left,right,diameter,axle_track)

# ev3.speaker.beep()
# left.run_angle(200,270,Stop.HOLD)
# lift.run_time(200,1000,Stop.HOLD)
# robot.straight(58)
# robot.stop()
# lift.run_time(-200,1500,Stop.HOLD)
# robot.turn(45)
# robot.straight(-30)
# robot.stop()
#robot.drive_time(100,90,1000)
# lift.run_time(200,1000,Stop.HOLD)
# robot.drive_time(-100,0,8000)
# lift.run_time(200,1000,Stop.HOLD)
lift.run_time(-200,850,Stop.HOLD)


