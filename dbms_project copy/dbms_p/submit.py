import customtkinter as ctk
from PIL import Image
import os

def show_beneficiary_request():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    request_window = ctk.CTk()
    request_window.title("Beneficiary Request")
    request_window.geometry("800x600")

    # Load background image
    try:
        bg_image = Image.open("images/login.jpg")  # Update path if needed
        bg_image = bg_image.resize((800, 600))
        bg_ctk = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(800, 600))
        bg_label = ctk.CTkLabel(request_window, image=bg_ctk, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Could not load background: {e}")
        request_window.configure(fg_color="#F1F1F1")

    # Form frame
    # Form frame with width and height passed during construction
    # Increase the width of the form frame
    form_frame = ctk.CTkFrame(request_window, corner_radius=15, fg_color="white", width=600, height=450)  # Increased width
    form_frame.place(relx=0.5, rely=0.5, anchor="center")

# Update the create_labeled_entry function to set fixed width for entries and labels
    def create_labeled_entry(label_text):
        label = ctk.CTkLabel(form_frame, text=label_text, anchor="w", text_color="#333", width=400)  # Fixed width for labels
        label.pack(padx=20, fill="x")
        entry = ctk.CTkEntry(form_frame, width=400)  # Fixed width for entries
        entry.pack(padx=20, pady=(0, 15), fill="x")
        return entry


    # Title
    title_label = ctk.CTkLabel(form_frame, text="Beneficiary Request Form", font=ctk.CTkFont(size=20, weight="bold"), text_color="#222")
    title_label.pack(pady=(20, 10))

    def create_labeled_entry(label_text):
        label = ctk.CTkLabel(form_frame, text=label_text, anchor="w", text_color="#333")
        label.pack(padx=20, fill="x")
        entry = ctk.CTkEntry(form_frame)
        entry.pack(padx=20, pady=(0, 15), fill="x")
        return entry

    beneficiary_id_entry = create_labeled_entry("Beneficiary ID:")
    ngo_id_entry = create_labeled_entry("NGO ID:")
    req_entry = create_labeled_entry("Request:")
    date_entry = create_labeled_entry("Request Date (YYYY-MM-DD):")
    status_entry = create_labeled_entry("Status (TRUE/FALSE):")

    def submit():
        print("Submitted:", beneficiary_id_entry.get(), ngo_id_entry.get(), req_entry.get(), date_entry.get(), status_entry.get())
        # Add your DB submission code here

    submit_button = ctk.CTkButton(form_frame, text="Submit Request", command=submit, fg_color="#4CAF50", hover_color="#388E3C")
    submit_button.pack(pady=(10, 20))

    request_window.mainloop()

if __name__ == "__main__":
    show_beneficiary_request()
