import tkinter as tk
from tkinter import messagebox
import time
from playsound import playsound

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("PomoTime")
        self.master.geometry("300x300")
        self.master.configure(bg="#2E2E2E")
        self.is_running = False
        self.work_duration = 45 * 60  # 45 minutes for work cycle
        self.break_duration = 10 * 60  # 10 minutes for break cycle
        self.current_phase = "work"  # Start with work phase
        self.time_remaining = self.work_duration  # Initialize time remaining for current phase

        # Update the label to look like a calculator display
        self.label = tk.Label(self.master, text="", font=("Courier New", 24), bg="black", fg="lime", height=2, width=10, bd=10, relief=tk.SUNKEN)
        self.label.pack(pady=20)

        self.button_frame = tk.Frame(self.master, bg="#2E2E2E")
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_timer, bg="#4CAF50", fg="white", width=10)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(self.button_frame, text="Pause", command=self.stop_timer, state=tk.DISABLED, bg="#F44336", fg="white", width=10)
        self.stop_button.grid(row=0, column=1, padx=5, pady=5)

        self.adjustment_frame = tk.Frame(self.master, bg="#2E2E2E")
        self.adjustment_frame.pack(pady=10)

        button_width = 10

        self.add_time_button = tk.Button(self.adjustment_frame, text="Add 5 min", command=self.add_time, bg="#2196F3", fg="white", width=button_width)
        self.add_time_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.reduce_time_button = tk.Button(self.adjustment_frame, text="Reduce 5 min", command=self.reduce_time, bg="#FF9800", fg="white", width=button_width)
        self.reduce_time_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.run_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def run_timer(self):
        if self.is_running:
            if self.time_remaining > 0:
                self.label.config(text=self.format_time(self.time_remaining))
                self.time_remaining -= 1
                self.master.after(1000, self.run_timer)
            else:
                playsound("beep.mp3")
                self.switch_phase()

    def switch_phase(self):
        if self.current_phase == "work":
            self.current_phase = "break"
            self.time_remaining = self.break_duration
        else:
            self.current_phase = "work"
            self.time_remaining = self.work_duration
        self.run_timer()

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def add_time(self):
        self.work_duration += 5 * 60
        if self.current_phase == "work":
            self.time_remaining += 5 * 60
        self.label.config(text=self.format_time(self.time_remaining))

    def reduce_time(self):
        if self.work_duration > 5 * 60:
            self.work_duration -= 5 * 60
            if self.current_phase == "work":
                self.time_remaining -= 5 * 60
            self.label.config(text=self.format_time(self.time_remaining))

def main():
    root = tk.Tk()
    pomodoro_timer = PomodoroTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
