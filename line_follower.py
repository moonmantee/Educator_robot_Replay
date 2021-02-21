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
while True:
    for i in range(5990):
        if light_sensor.reflection() <= 70:
            robot.drive(100,(light_sensor.reflection() - 35)/1.5)
        else:
            if light_sensor2.reflection() <= 70:
                robot.drive(100,(light_sensor2.reflection() - 35)/-1.5)
            else:
                robot.drive(100,0.0)
        