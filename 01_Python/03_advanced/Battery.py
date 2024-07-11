

from pynotifier import notification # type: ignore
import psutil
import time

# Get the battery status
battery = psutil.sensors_battery()
percent = battery.percent

# Send the notification
print(percent)

notification.notify(
    title = "Battery Percentage",
    message = f"{percent}% percent remaining",
    timeout = 10
)

# Create a new thread to monitor the battery status
# import threading

# def monitor_battery():
#     while True:
#         battery = psutil.sensors_battery()
#         percent = battery.percent
#         if percent < 10:
#             notification.notify(
#                 title = "Battery Warning",
#                 message = f"{percent}% percent remaining, please charge!",
#                 timeout = 5
#             )
#         time.sleep(60)




