import customtkinter as ctk
from PIL import Image

def simulate_assignment(category_entry, result_label):
    # Hardcoded category-NGO mapping (simulated logic)
    assignment_map = {
        "Education": "Bright Future Foundation",
        "Medical": "HealthCare Connect",
        "Environment": "Green Earth NGO",
        "Women": "Empower Her Trust"
    }

    category = category_entry.get().strip().title()
    assigned_ngo = assignment_map.get(category, "No matching NGO found.")

    result_label.configure(text=f"Assigned NGO: {assigned_ngo}")

def show_assignment_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Assign Request to NGO")

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
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="white", width=400, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    ctk.CTkLabel(frame, text="Assign Request by Category", font=ctk.CTkFont(size=18, weight="bold"), text_color="#222").pack(pady=(20, 10))

    # Category input
    ctk.CTkLabel(frame, text="Enter Request Category:", anchor="w", text_color="#333").pack(padx=20, fill="x")
    category_entry = ctk.CTkEntry(frame)
    category_entry.pack(padx=20, pady=(0, 15), fill="x")

    # Result label
    result_label = ctk.CTkLabel(frame, text="", text_color="#00695C", font=ctk.CTkFont(size=14, weight="bold"))
    result_label.pack(pady=(5, 10))

    # Submit button
    submit_button = ctk.CTkButton(
        frame,
        text="Assign Request",
        command=lambda: simulate_assignment(category_entry, result_label),
        fg_color="#4CAF50",
        hover_color="#388E3C"
    )
    submit_button.pack(pady=(10, 10))

    app.mainloop()

if __name__ == "__main__":
    show_assignment_gui()
