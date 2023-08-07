import time
from tkinter import Tk, Label, Button, StringVar
from plyer import notification

class PomodoroTimer:
    def __init__(self):
        self.pomodoro_duration = 25 * 60  # 25 minutes in seconds
        self.break_duration = 5 * 60  # 5 minutes in seconds
        self.current_duration = self.pomodoro_duration
        self.running = False
        self.root = Tk()
        self.root.title("Pomodoro Timer")
        self.timer_var = StringVar()
        self.timer_var.set(self.format_time(self.current_duration))
        self.timer_label = Label(self.root, textvariable=self.timer_var, font=("Arial", 50))
        self.start_button = Button(self.root, text="Start", command=self.start_timer)
        self.stop_button = Button(self.root, text="Stop", command=self.stop_timer)
        self.timer_label.pack(pady=50)
        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.root.mainloop()

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def show_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            timeout=10
        )

    def update_timer(self):
        while self.running and self.current_duration > 0:
            self.timer_var.set(self.format_time(self.current_duration))
            self.root.update()
            time.sleep(1)
            self.current_duration -= 1

        if self.running:
            if self.current_duration == 0:
                if self.timer_var.get() == self.format_time(self.pomodoro_duration):
                    self.show_notification("Pomodoro Timer", "Time to take a break!")
                    self.current_duration = self.break_duration
                else:
                    self.show_notification("Pomodoro Timer", "Time to work!")
                    self.current_duration = self.pomodoro_duration

            self.update_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False
        self.timer_var.set(self.format_time(self.pomodoro_duration))
        self.current_duration = self.pomodoro_duration

if __name__ == "__main__":
    PomodoroTimer()
