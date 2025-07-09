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
    canvas.create_rectangle(0, 0, popup.winfo_screenwidth(), popup.winfo_screenheight(), fill="#fbccfb")

    # Center message
    canvas.create_text(
        popup.winfo_screenwidth() // 2, popup.winfo_screenheight() // 2,
        text="Time to pause ✨\nStretch, breathe, and refresh!",
        font=("Helvetica", 32, "bold"),
        fill="#92138E",
        justify="center"
    )

    # Close the popup when clicked
    popup.bind("<Button-1>", lambda e: popup.destroy())
    popup.mainloop()

def run_reminder_every_hour():
    while True:
        show_popup()
        time.sleep(60 * 60) 

# Run the reminder loop in background
threading.Thread(target=run_reminder_every_hour, daemon=True).start()

# Keep the script alive
while True:
    time.sleep(1)
