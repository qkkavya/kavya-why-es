# top_ngos.py
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@123",
    database="ngos"
)
cursor = conn.cursor()

def show_top_ngos():
    window = ctk.CTk()
    window.title("Top NGOs by Feedback Rating")
    window.geometry("800x600")

    heading = ctk.CTkLabel(window, text="Top NGOs (Based on Average Feedback Rating)",
                           font=("Arial", 20, "bold"))
    heading.pack(pady=20)

    try:
        cursor.execute("""
            SELECT n.Name, AVG(f.Rating) as avg_rating
            FROM feedback f
            JOIN ngos n ON f.NGOid = n.id
            GROUP BY f.NGOid
            ORDER BY avg_rating DESC
        """)
        data = cursor.fetchall()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return

    if not data:
        ctk.CTkLabel(window, text="No feedback available to show rankings.", font=("Arial", 14)).pack(pady=20)
    else:
        # Text view
        for i, (ngo_name, rating) in enumerate(data, start=1):
            line = f"{i}. {ngo_name} - ⭐ {round(rating, 2)}/5"
            ctk.CTkLabel(window, text=line, font=("Arial", 14)).pack(anchor="w", padx=40, pady=2)

        # Bar Graph
        ngo_names = [name for name, _ in data]
        ratings = [rating for _, rating in data]

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(ngo_names[::-1], ratings[::-1], color="skyblue")
        ax.set_xlabel("Average Rating")
        ax.set_title("NGO Ratings Based on Feedback")
        ax.set_xlim(0, 5)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    # Back Button
    def go_back():
        window.destroy()
        from main import welcome_screen
        welcome_screen()

    back_btn = ctk.CTkButton(window, text="Back to Home", command=go_back)
    back_btn.pack(pady=10)

    window.mainloop()
