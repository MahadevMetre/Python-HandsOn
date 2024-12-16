import time

# Get the current hour
current_hour = int(time.strftime('%H'))

# Determine the greeting
if 5 <= current_hour < 12:
    greeting = "Good Morning"
elif 12 <= current_hour < 17:
    greeting = "Good Afternoon"
elif 17 <= current_hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

# Print the greeting
print(f"{greeting}! The current time is {time.strftime('%H:%M:%S')}.")
