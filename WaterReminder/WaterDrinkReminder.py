import tkinter as tk
import time
import threading

def show_popup():
    popup = tk.Tk()
    popup.attributes("-fullscreen", True)
    popup.configure(bg='lightblue')
    popup.attributes('-alpha', 0.85)  # Slight transparency

    canvas = tk.Canvas(popup, width=popup.winfo_screenwidth(), height=popup.winfo_screenheight(), highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_rectangle(0, 0, popup.winfo_screenwidth(), popup.winfo_screenheight(), fill="#b3ecff")

    # Center message
    canvas.create_text(
        popup.winfo_screenwidth() // 2, popup.winfo_screenheight() // 2,
        text="Time to Hydrate! 💧\nGo grab a glass of water!",
        font=("Helvetica", 32, "bold"),
        fill="#004466",
        justify="center"
    )

    # Close the popup when clicked
    popup.bind("<Button-1>", lambda e: popup.destroy())
    popup.mainloop()

def run_reminder_every_hour():
    while True:
        show_popup()
        time.sleep(60 * 60)  # Change to time.sleep(30) for 30-second reminders

# Run the reminder loop in background
threading.Thread(target=run_reminder_every_hour, daemon=True).start()

# Keep the script alive
while True:
    time.sleep(1)
