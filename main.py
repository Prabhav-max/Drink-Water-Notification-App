import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title='Please drink Water.Now!',
            message='A healthy human need 3.7 litres of water a day.',
            app_icon="C:\\Users\\Prabhav\\Python\\Python_Projects\\Drink Water\\glass.ico",
            timeout=10
        )
        time.sleep(60*60)