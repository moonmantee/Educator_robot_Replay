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

lift.run_time(200,1000,Stop.HOLD,False)
robot.straight(1290)
robot.stop()
left.run_time(200,500,Stop.HOLD)
robot.drive_time(100,0,2200)
left.run_time(600,4000,Stop.HOLD)
robot.drive_time(-100,0,1000)
right.run_time(-200,2000,Stop.HOLD)
robot.drive_time(-400,0,1000)
robot.straight(50)
while light_sensor2.color() != Color.YELLOW:
    robot.drive(200,0)
robot.stop()
right.run_time(200,1000)
robot.drive_time(100,0,1000)
lift.run_time(-200,4000,Stop.HOLD)
time.sleep(1)
lift.run_time(50,90)
robot.drive_time(-100,0,1350)
robot.drive_time(100,0,150)
left.run_time(200,1000,Stop.HOLD)
lift.run_time(100,1000,Stop.HOLD)