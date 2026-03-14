# Date time module 
import datetime

now = datetime.datetime.now()

# Now we will format is
formatted_now = now.strftime("%d-%m-%Y %H:%M:%S")

print(f"Current Date and Time: {formatted_now}")