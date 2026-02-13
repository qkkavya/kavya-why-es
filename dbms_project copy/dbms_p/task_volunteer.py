import customtkinter as ctk
from PIL import Image

def show_unassigned_volunteers(result_frame):
    # Static (mock) data of unassigned volunteers
    unassigned = [
        "Tanishq Sachdeva",
        "Ananya Gupta",
        "Rohan Mehta",
        "Simran Kaur"
    ]

    # Clear previous results
    for widget in result_frame.winfo_children():
        widget.destroy()

    # Heading
    heading = ctk.CTkLabel(result_frame, text="assigned Volunteers", font=ctk.CTkFont(size=16, weight="bold"), text_color="#222")
    heading.pack(pady=(10, 10))

    # List each volunteer
    for name in unassigned:
        label = ctk.CTkLabel(result_frame, text=name, text_color="#333", anchor="w")
        label.pack(pady=2, padx=10, anchor="w")

def show_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("assigned Volunteers")

    # Background
    try:
        bg_image = Image.open("images/login.jpg")
        bg_image = bg_image.resize((800, 500))
        bg_ctk = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(800, 500))
        bg_label = ctk.CTkLabel(app, image=bg_ctk, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Background error:", e)
        app.configure(fg_color="#F0F0F0")

    # Main Frame
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="white", width=450, height=350)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    ctk.CTkLabel(frame, text="Check assigned Volunteers", font=ctk.CTkFont(size=18, weight="bold"), text_color="#222").pack(pady=(20, 10))

    # Optional Filter (static)
    ctk.CTkLabel(frame, text="Filter by Category (optional):", text_color="#333").pack(padx=20, fill="x")
    category_entry = ctk.CTkEntry(frame)
    category_entry.pack(padx=20, pady=(0, 10), fill="x")

    # Frame for results
    result_frame = ctk.CTkFrame(frame, fg_color="#F9F9F9", corner_radius=10)
    result_frame.pack(pady=(10, 10), padx=20, fill="both", expand=True)

    # Submit button
    submit_button = ctk.CTkButton(
        frame,
        text="Show assigned Volunteers",
        command=lambda: show_unassigned_volunteers(result_frame),
        fg_color="#1976D2",
        hover_color="#1565C0"
    )
    submit_button.pack(pady=(5, 10))

    app.mainloop()

if __name__ == "__main__":
    show_gui()
