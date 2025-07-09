# Reminders

This repository contains two simple Python-based desktop reminder scripts created using `tkinter`. These scripts help promote healthier daily habits through on-screen reminders.

## 🥤 Water Reminder

**Location:** `WaterReminder/WaterDrinkReminder.py`

Displays a full-screen pop-up every hour encouraging the user to drink water.  
A cuter version (`CuteWaterDrinkingRemainder.py`) includes an animated fairy character floating up and down.

### Features:
- Full-screen semi-transparent overlay
- Friendly hydration message
- Click anywhere to close the reminder
- Runs continuously in the background

## 🖥️ Screen Break Reminder

**Location:** `ScreenTimeReminder/RestReminder.py`

Encourages users to take regular breaks from screen time by popping up every hour with a gentle message.

### Features:
- Light red background to gently signal screen fatigue
- Encouraging message to take a short rest
- Auto-closes on click
- Background looping every hour

---

## 🛠 Requirements

- Python 3.x
- [`Pillow`](https://python-pillow.org) (for image support in `CuteWaterDrinkingRemainder.py`)

Install required packages using:

```bash
pip install pillow
