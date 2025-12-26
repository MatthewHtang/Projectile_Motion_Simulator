#Projectile Motion Simulator

import math

#user inputs
initial_height = float (input("Enter Initial Height (m): "))
initial_velocity = float (input("Enter Initial Velocity (m/s): "))
launch_angle = float (input("Enter launch angle (degrees): "))

#Gravity
earth_gravity = 9.8

#Converting angle
angle_rad = math.radians(launch_angle)

#Velocity Components
vx = initial_velocity * math.cos(launch_angle)
vy = initial_velocity * math.sin(launch_angle)

#Calculating Time of Flight
# We gonna use the equation: y = y0 + vy*t - 0.5*g*t^2
#This one is for finding t when y = 0

a = -0.5 * earth_gravity
b = vy
c = initial_height

discriminant = b ** 2 - 4*a*c
time_of_flight = (-b -math.sqrt(discriminant)) / (2 * a)

# ----- FINAL HORIZONTAL POSITION -----
final_position = vx * time_of_flight

# ----- MAXIMUM HEIGHT -----
max_height = initial_height + (vy**2) / (2 * earth_gravity)

# ----- OUTPUT -----
print("\n--- RESULTS ---")
print(f"Time of flight: {time_of_flight:.2f} s")
print(f"Final horizontal position: {final_position:.2f} m")
print(f"Maximum height: {max_height:.2f} m")
