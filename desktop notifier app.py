import time
from plyer import notification

while True:
    notification.notify(
        title="Water Reminder 💧",
        message="Time to drink water and stretch!",
        timeout=10
    )
    time.sleep(3600)  # wait for 1 hour (3600 seconds)
