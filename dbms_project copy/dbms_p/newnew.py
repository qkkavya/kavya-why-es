import customtkinter as ctk
from PIL import Image

def find_unassigned(entry_widget, result_label):
    input_text = entry_widget.get().strip()
    if not input_text:
        result_label.configure(text="Please enter volunteer names.")
        return

    # Example: comma-separated names
    input_names = [name.strip().capitalize() for name in input_text.split(",")]

    # Static data
    assigned_volunteers = {"Alice", "David", "Meena"}  # example assigned
    unassigned = [name for name in input_names if name not in assigned_volunteers]

    if unassigned:
        result_label.configure(text="Unassigned Volunteers:\n" + "\n".join(unassigned))
    else:
        result_label.configure(text="All volunteers are assigned to tasks.")

def show_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Unassigned Volunteers")

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

    # Frame
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="white", width=500, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    ctk.CTkLabel(frame, text="Check Unassigned Volunteers", font=ctk.CTkFont(size=18, weight="bold"), text_color="#222").pack(pady=(20, 10))

    # Entry
    ctk.CTkLabel(frame, text="Enter Volunteer Names (comma-separated):", text_color="#333").pack(padx=20, anchor="w")
    volunteer_entry = ctk.CTkEntry(frame)
    volunteer_entry.pack(padx=20, pady=(0, 15), fill="x")

    # Result label
    result_label = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=14), text_color="#00796B", justify="left")
    result_label.pack(pady=(10, 10))

    # Button
    ctk.CTkButton(
        frame,
        text="Check",
        command=lambda: find_unassigned(volunteer_entry, result_label),
        fg_color="#1976D2",
        hover_color="#0D47A1"
    ).pack(pady=(0, 15))

    app.mainloop()

if __name__ == "__main__":
    show_gui()
