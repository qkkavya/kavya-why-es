import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

def simulate_status_update(event_entry, contribution_entry, required_entry):
    try:
        event_name = event_entry.get()
        total_contribution = float(contribution_entry.get())
        amount_required = float(required_entry.get())

        if not event_name.strip():
            messagebox.showwarning("Missing Info", "Please enter the event name.")
            return

        if total_contribution >= amount_required:
            status = "Successful"
        else:
            status = "Unsuccessful"

        messagebox.showinfo("Status Updated", f"Event '{event_name}' marked as '{status}'.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for contribution and required amount.")

def show_event_update_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Update Event Status (Static)")

    # Background image
    try:
        bg_image = Image.open("images/login.jpg")  # Adjust if necessary
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
    title_label = ctk.CTkLabel(frame, text="Update Event Status", font=ctk.CTkFont(size=20, weight="bold"), text_color="#222")
    title_label.pack(pady=(20, 10))

    # Event Name
    event_label = ctk.CTkLabel(frame, text="Event Name:", text_color="#333", anchor="w")
    event_label.pack(padx=20, fill="x")
    event_entry = ctk.CTkEntry(frame)
    event_entry.pack(padx=20, pady=(0, 10), fill="x")

    # Total Contribution
    contribution_label = ctk.CTkLabel(frame, text="Total Contribution (₹):", text_color="#333", anchor="w")
    contribution_label.pack(padx=20, fill="x")
    contribution_entry = ctk.CTkEntry(frame)
    contribution_entry.pack(padx=20, pady=(0, 10), fill="x")

    # Amount Required
    required_label = ctk.CTkLabel(frame, text="Amount Required (₹):", text_color="#333", anchor="w")
    required_label.pack(padx=20, fill="x")
    required_entry = ctk.CTkEntry(frame)
    required_entry.pack(padx=20, pady=(0, 20), fill="x")

    # Button
    update_button = ctk.CTkButton(
        frame,
        text="Simulate Status Update",
        command=lambda: simulate_status_update(event_entry, contribution_entry, required_entry),
        fg_color="#4CAF50",
        hover_color="#388E3C"
    )
    update_button.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    show_event_update_gui()
