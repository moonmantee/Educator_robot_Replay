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
left=Motor(Port.C)
right=Motor(Port.B)
lift=Motor(Port.A)
axle_track=114
diameter=54
light_sensor = ColorSensor(Port.S1)
light_sensor2 = ColorSensor(Port.S2)
robot = DriveBase(left,right,diameter,axle_track)

lift.run_time(300,1000,Stop.BRAKE)
robot.straight(480)
while light_sensor.reflection() > 7 and light_sensor2.reflection() > 7:
    robot.drive(100,0)
robot.stop()
robot.drive_time(25,0,10000)
robot.drive_time(-100,0,1000)
while light_sensor.reflection() > 7 and light_sensor2.reflection() > 7:
    robot.drive(-100,0)
robot.stop()
robot.drive_time(-100,0,1000)
while light_sensor.reflection() > 7 and light_sensor2.reflection() > 7:
    robot.drive(-100,0)
robot.stop()
left.run_angle(100,150,Stop.HOLD)
robot.drive_time(200,0,700)
while light_sensor2.reflection() > 7:
    robot.drive(100,0)
robot.stop()
left.run_time(100,1850,Stop.HOLD)
robot.straight(200)
while light_sensor.reflection() > 7 and light_sensor2.reflection() > 7:
    robot.drive(150,0)
robot.stop()
left.run_time(100,800,Stop.HOLD)
robot.straight(235)
lift.run_time(-200,850,Stop.HOLD)
time.sleep(2)
lift.run_time(200,1000)
robot.drive_time(-100,0,2000)
left.run_time(75,1500,Stop.HOLD)
robot.drive_time(100,0,1600)

robot.turn(45)
robot.straight(292)
robot.turn(180)
while True:
    robot.turn(90)
    time.sleep(1)
    robot.turn(-90)