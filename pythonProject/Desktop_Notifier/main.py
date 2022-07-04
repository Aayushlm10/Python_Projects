import time
import datetime
from plyer import notification
#now=(datetime.datetime.now())
#current_time=now.strftime("%H:%M:%S")
while True:
    notification.notify(
        title="Hello Aayush",
        message=datetime.datetime.now().strftime("%H:%M:%S")+"\nYou should drink water!",
        app_name="YOUR HEALTH NOTIFIER",
        #app_icon="C:\Users\Aayush\Downloads\icon.ico",
        timeout=30,
        ticker="New Notification",
        toast=False
    )
    print(datetime.datetime.now().strftime("%H:%M:%S") + "\nYou have just improved your body's functioning")
    time.sleep(60*60*2)