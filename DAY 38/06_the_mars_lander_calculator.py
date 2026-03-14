# Check if spacescraft can land smoothly or not
import random
import math

# Initial Velocity
IV = random.randint(100, 500)
# Wind Turbulance
WT = random.randint(-10.5, 10.5)

force = math.sqrt(math.pow(IV, 2) + math.pow(WT, 2))

final_force = math.floor(force)

print(final_force)

if final_force < 200:
    print("Successful Landing 🛰")
elif final_force < 400:
    print("Rough Landing! Damage Sustained ⚠")
elif final_force > 400:
    print("CRITICAL FAILURE! Crater Created 💥")