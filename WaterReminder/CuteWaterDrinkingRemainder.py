import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

def show_popup():
    popup = tk.Tk()
    popup.attributes("-fullscreen", True)
    popup.configure(bg='lightblue')
    popup.attributes('-alpha', 0.85)

    canvas = tk.Canvas(popup, width=popup.winfo_screenwidth(), height=popup.winfo_screenheight(), highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_rectangle(0, 0, popup.winfo_screenwidth(), popup.winfo_screenheight(), fill="#b3ecff")

    fairy_photo = None
    fairy = None

    # Load the fairy image
    try:
        fairy_img = Image.open("D:/Python313/WaterReminder/cute_water_fairy_character.png.png")
        fairy_img = fairy_img.resize((300, 300), Image.Resampling.LANCZOS)
        fairy_photo = ImageTk.PhotoImage(fairy_img)
        x = popup.winfo_screenwidth() // 2
        y = popup.winfo_screenheight() // 2 - 100
        fairy = canvas.create_image(x, y, image=fairy_photo)
    except Exception as e:
        print("Image load failed:", e)

    canvas.create_text(
        popup.winfo_screenwidth() // 2, popup.winfo_screenheight() // 2 + 200,
        text="Time to Hydrate! 💧\nGo grab a glass of water!",
        font=("Helvetica", 28, "bold"),
        fill="#004466",
        justify="center"
    )

    # Flying animation using after()
    direction = 1
    def animate():
        nonlocal direction
        if fairy:
            canvas.move(fairy, 0, direction)
            coords = canvas.coords(fairy)
            if coords[1] >= popup.winfo_screenheight() // 2 - 70 or coords[1] <= popup.winfo_screenheight() // 2 - 130:
                direction *= -1
            popup.after(50, animate)

    animate()

    # Close on click
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
