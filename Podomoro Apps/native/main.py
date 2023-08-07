import time
from plyer import notification

def pomodoro_timer():
    pomodoro_duration = 2 * 60
    break_duration = 1 * 60

    while True:
        #pomodoro session
        notification.notify(
            title= "Pomodoro Title",
            message = "Time to Work! Stay Focus for the next 25 minutes",
            timeout=20 #display the notification for 10 seconds
        )
        time.sleep(pomodoro_duration)

        #short breakk session
        notification.notifiy(
            title="Pomodoro Timer",
            message = "Take a short break. Relax for the next 5 minutes.",
            timeout=10 #display the notification for 10 seconds
        )
        time.sleep(break_duration)

if __name__== "__main__":
    pomodoro_timer()