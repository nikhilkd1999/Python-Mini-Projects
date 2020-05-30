
from plyer import notification

import time

if __name__ == "__main__":
    while True:
        notification.notify(

            title = " HI ",
            message = "HELLO",
            #app_icon = "",
            timeout = 5
        )
        time.sleep(2)
        break