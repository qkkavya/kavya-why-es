import customtkinter as ctk
from PIL import Image

def simulate_show_events(frame):
    # Sample static data (hardcoded)
    event_data = [
        ("Event A", "2 tasks"),
        ("Event C", "3 tasks"),
        ("Event F", "2 tasks")
    ]

    # Clear old dynamic labels (below y=100)
    for widget in frame.winfo_children():
        if isinstance(widget, ctk.CTkLabel) and widget.winfo_y() >= 100:
            widget.destroy()

    y_offset = 110
    for event, task_count in event_data:
        event_label = ctk.CTkLabel(frame, text=event, text_color="#333", anchor="w")
        event_label.place(x=40, y=y_offset)
        task_label = ctk.CTkLabel(frame, text=task_count, text_color="#333", anchor="e")
        task_label.place(x=260, y=y_offset)
        y_offset += 30

def show_unassigned_event_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Events with Unassigned Tasks")

    # Background
    try:
        bg_image = Image.open("images/login.jpg")  # Adjust as needed
        bg_image = bg_image.resize((800, 500))
        bg_ctk = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(800, 500))
        bg_label = ctk.CTkLabel(app, image=bg_ctk, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Background error:", e)
        app.configure(fg_color="#F0F0F0")

    # Frame
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="white", width=400, height=350)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    title_label = ctk.CTkLabel(frame, text="Unassigned Task Report", font=ctk.CTkFont(size=20, weight="bold"), text_color="#222")
    title_label.place(x=80, y=20)

    # Column Headings
    heading_font = ctk.CTkFont(weight="bold", size=14)
    ctk.CTkLabel(frame, text="Event Name", text_color="#000", font=heading_font).place(x=40, y=80)
    ctk.CTkLabel(frame, text="Unassigned Tasks", text_color="#000", font=heading_font).place(x=260, y=80)

    # Button to simulate query
    check_button = ctk.CTkButton(
        frame,
        text="Show Events",
        command=lambda: simulate_show_events(frame),
        fg_color="#FF5722",
        hover_color="#E64A19"
    )
    check_button.place(relx=0.5, rely=1.0, anchor="s", y=-20)

    app.mainloop()

if __name__ == "__main__":
    show_unassigned_event_gui()
