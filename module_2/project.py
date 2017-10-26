# CODE CELL
#
# Write the park function so that it actually parks your vehicle.
from Car import Car
import time
from collections import namedtuple


Maneuver = namedtuple('Maneuver', ['steer', 'gas', 'sleep'])


def execute_maneuver(car, maneuver):
    """Executes the specified maneuver on a car.

    A maneuver consists of a steer, the gas pressure, and a sleep
    time before the next maneuver is executed.

    """
    car.steer(maneuver.steer)
    car.gas(maneuver.gas)
    time.sleep(maneuver.sleep)


def park(car):
    """Parks a car in parallel"""
    maneuvers = [
        Maneuver(steer=23, gas=-0.5, sleep=3.0),
        Maneuver(steer=-23, gas=-0.25, sleep=3.0),
        Maneuver(steer=15, gas=0.2, sleep=0.8),
        Maneuver(steer=0, gas=0, sleep=0),
    ]

    for maneuver in maneuvers:
        execute_maneuver(car, maneuver)


car = Car()
park(car)
