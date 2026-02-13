import customtkinter as ctk
from PIL import Image

def filter_request(entry_widget, result_label):
    text = entry_widget.get().lower()

    # Static keyword-category mapping
    categories = {
        "medical": ["doctor", "medicine", "hospital", "health", "clinic"],
        "education": ["school", "books", "teacher", "study", "tuition"],
        "food": ["meal", "food", "hunger", "ration"],
        "shelter": ["home", "roof", "shelter", "housing"],
        "clothes": ["clothes", "warm", "jacket", "shirt"]
    }

    # Default category
    matched_category = "Uncategorized"
    for category, keywords in categories.items():
        if any(word in text for word in keywords):
            matched_category = category.capitalize()
            break

    result_label.configure(text=f"Filtered Category: {matched_category}")

def show_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("800x500")
    app.title("Request Category Filter")

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
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="white", width=500, height=300)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    ctk.CTkLabel(frame, text="Filter Request into Category", font=ctk.CTkFont(size=18, weight="bold"), text_color="#222").pack(pady=(20, 10))

    # Input field
    ctk.CTkLabel(frame, text="Enter Request Description:", text_color="#333").pack(padx=20, anchor="w")
    request_entry = ctk.CTkEntry(frame)
    request_entry.pack(padx=20, pady=(0, 15), fill="x")

    # Result label
    result_label = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=14), text_color="#00796B")
    result_label.pack(pady=(10, 10))

    # Button
    ctk.CTkButton(
        frame,
        text="Filter Category",
        command=lambda: filter_request(request_entry, result_label),
        fg_color="#4CAF50",
        hover_color="#388E3C"
    ).pack(pady=(0, 15))

    app.mainloop()

if __name__ == "__main__":
    show_gui()
