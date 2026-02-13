import customtkinter as ctk
from PIL import Image

def show_tasks(event_entry, result_frame):
    # Sample static task data for events
    task_data = {
        "Health Camp": ["Set up tents", "Distribute flyers", "Medical check-up", "Record attendance"],
        "Tree Plantation": ["Dig holes", "Plant saplings", "Water plants"],
        "Food Drive": ["Collect food", "Pack items", "Distribute at shelters"]
    }

    # Clear previous results
    for widget in result_frame.winfo_children():
        widget.destroy()

    event = event_entry.get().strip().title()
    tasks = task_data.get(event, [])

    heading = ctk.CTkLabel(result_frame, text=f"Tasks for: {event}", font=ctk.CTkFont(size=16, weight="bold"), text_color="#222")
    heading.pack(pady=(10, 10))

    if tasks:
        for task in tasks:
            task_label = ctk.CTkLabel(result_frame, text="• " + task, text_color="#333", anchor="w")
            task_label.pack(padx=10, anchor="w")
    else:
        ctk.CTkLabel(result_frame, text="No tasks found for this event.", text_color="#888").pack(pady=5)

def show_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Tasks Performed at Event")

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
    ctk.CTkLabel(frame, text="View Tasks for an Event", font=ctk.CTkFont(size=18, weight="bold"), text_color="#222").pack(pady=(20, 10))

    # Event input
    ctk.CTkLabel(frame, text="Enter Event Name:", text_color="#333").pack(padx=20, anchor="w")
    event_entry = ctk.CTkEntry(frame)
    event_entry.pack(padx=20, pady=(0, 15), fill="x")

    # Result frame
    result_frame = ctk.CTkFrame(frame, fg_color="#F8F8F8", corner_radius=10)
    result_frame.pack(padx=20, pady=(0, 10), fill="both", expand=True)

    # Button
    ctk.CTkButton(
        frame,
        text="Show Tasks",
        command=lambda: show_tasks(event_entry, result_frame),
        fg_color="#00796B",
        hover_color="#004D40"
    ).pack(pady=(5, 15))

    app.mainloop()

if __name__ == "__main__":
    show_gui()
