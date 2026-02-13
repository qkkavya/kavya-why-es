import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

def run_update_demo(username_entry, category_entry):
    username = username_entry.get()
    category = category_entry.get()

    if username.strip() == "" or category.strip() == "":
        messagebox.showwarning("Missing Info", "Please fill in all fields.")
        return

    # Simulated update
    messagebox.showinfo("Success", f"Task updated to 'Provide Health Care' for volunteer '{username}' in '{category}' category.")

def show_update_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Update Volunteer Tasks (Static)")

    # Background image
    try:
        bg_image = Image.open("images/login.jpg")  # Change path if needed
        bg_image = bg_image.resize((800, 500))
        bg_ctk = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(800, 500))
        bg_label = ctk.CTkLabel(app, image=bg_ctk, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Background error:", e)
        app.configure(fg_color="#F0F0F0")

    # Frame
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="white", width=500, height=350)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    title_label = ctk.CTkLabel(frame, text="Update Volunteer Task", font=ctk.CTkFont(size=20, weight="bold"), text_color="#222")
    title_label.pack(pady=(20, 10))

    # Username
    user_label = ctk.CTkLabel(frame, text="Volunteer Username:", text_color="#333", anchor="w")
    user_label.pack(padx=20, fill="x")
    username_entry = ctk.CTkEntry(frame)
    username_entry.pack(padx=20, pady=(0, 10), fill="x")

    # Category
    category_label = ctk.CTkLabel(frame, text="Volunteer Category:", text_color="#333", anchor="w")
    category_label.pack(padx=20, fill="x")
    category_entry = ctk.CTkEntry(frame)
    category_entry.pack(padx=20, pady=(0, 20), fill="x")

    # Button
    update_button = ctk.CTkButton(
        frame,
        text="Simulate Update",
        command=lambda: run_update_demo(username_entry, category_entry),
        fg_color="#1976D2",
        hover_color="#1565C0"
    )
    update_button.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    show_update_gui()
