# This is ignoring any air resistance
import math
import sys

g = 9.81

def get_float_input(value):
    while True:
        num = input(value)
        if num.lower() == "exit":
            sys.exit()
        try:
            return float(num)
        except ValueError:
            print("SYSTEM: Invalid input")

def find_initial_height(t) -> float:
    return  0.5 * g * t ** 2

def final_velocity_with_height(h) -> float:
    return math.sqrt(2 * g * h)

def final_velocity_with_time(t) -> float:
    return g * t