import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

moods = [
    {"text": "Happy 😊", "color": "yellow"},
    {"text": "Tired 😴", "color": "gray"},
    {"text": "Curious 🤔", "color": "lightblue"},
    {"text": "Excited 🎉", "color": "orange"},
    {"text": "Calm 😌", "color": "lightgreen"}
]

mood_counts = [0] * len(moods)
mood_index = 0  

root = tk.Tk()
root.title("Mood Dashboard")
root.geometry("500x500")

def change_mood():
    global mood_index
    mood = moods[mood_index]
    mood_button.config(text=mood["text"], bg=mood["color"])
    mood_counts[mood_index] += 1
    mood_index = (mood_index + 1) % len(moods)
    update_chart()

mood_button = tk.Button(root, text="How do I feel?", command=change_mood, font=("Arial", 14), bg="white")
mood_button.pack(pady=20)


fig, ax = plt.subplots(figsize=(4, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def update_chart():
    ax.clear()
    total = sum(mood_counts)
    labels = [m["text"] for m in moods]
    colors = [m["color"] for m in moods]
    if total == 0:
        ax.text(0.5, 0.5, "No moods recorded", ha="center", va="center", fontsize=12)
        ax.set_title("Mood Distribution")
    else:
        ax.pie(mood_counts, labels=labels, colors=colors, startangle=90, wedgeprops={"edgecolor": "black"})
        ax.set_title("Mood Distribution")
    canvas.draw()


update_chart()

root.mainloop()