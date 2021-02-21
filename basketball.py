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

lift.run_time(100,400,Stop.HOLD)
robot.straight(300)
robot.stop()
robot.turn(49)
robot.stop()
robot.settings(300)
robot.straight(700)
robot.drive_time(-100,0,1000)
lift.run_time(-100,200)
left.run_time(200,1200)
robot.drive_time(100,0,200)
lift.run_time(50,3000)
lift.run_time(-100,1000)
robot.drive_time(-100,0,1000)
left.run_time(200,1000)
robot.drive_time(200,0,3100)