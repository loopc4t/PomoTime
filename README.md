# PomoTime - Pomodoro Timer

PomoTime is a simple Pomodoro timer application built using Python's Tkinter library. It provides a graphical user interface to help you manage your work and break intervals efficiently using the Pomodoro Technique.

## Features

- **Start/Pause Timer**: Begin and pause the timer for your work and break sessions.
- **Adjust Time**: Add or reduce 5-minute increments to the work duration.
- **Automatic Phase Switching**: Automatically switches between work and break phases.
- **Visual Timer Display**: Displays the remaining time in a clear format.
- **Sound Notification**: Plays a beep sound when the timer completes a phase.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python)
- playsound module (install via `pip install playsound`)
- A sound file named `beep.mp3` for the notification sound

## Installation

1. **Clone the repository** (or download the script directly):
   ```bash
   git clone https://github.com/yourusername/pomotime.git
   cd pomotime
   ```
2. Install the required Python module:
```bash
pip install playsound
```
    Add the beep sound file: Make sure you have a beep.mp3 file in the same directory as the script for the sound notification.

Usage

    Run the application:
    ```bash
    python pomodoro_timer.py
    ```

    Control the Timer:
        Click Start to begin the timer.
        Click Pause to stop the timer.
        Use Add 5 min and Reduce 5 min buttons to adjust the work duration.

Code Overview

    PomodoroTimer class: Manages the timer's logic, GUI, and phase switching.
    start_timer method: Starts the timer and updates the display.
    stop_timer method: Pauses the timer.
    run_timer method: Updates the remaining time every second.
    switch_phase method: Switches between work and break phases.
    format_time method: Formats the remaining time for display.
    **add_time and reduce_time methods
