import customtkinter as ctk
from PIL import Image
import os

# Sample requests for demo
sample_requests = [
    "Need food supplies for 20 families",
    "Urgent medicine for elderly",
    "Require clothes for children",
    "Request for shelter materials",
    "Looking for education support",
    "Need medical assistance for injured person",
    "Clothing and blankets needed",
    "Food required during flood relief",
    "Educational materials required for students"
]

# Define categories and keywords
categories = {
    "Food": ["food", "hunger", "meal", "supplies"],
    "Medicine": ["medicine", "medical", "injured", "doctor", "assistance"],
    "Clothing": ["clothes", "clothing", "blankets", "warm"],
    "Shelter": ["shelter", "tent", "roof", "temporary"],
    "Education": ["education", "school", "student", "study", "materials"]
}

def categorize_requests(requests):
    result = {category: [] for category in categories}
    for request in requests:
        for category, keywords in categories.items():
            if any(word in request.lower() for word in keywords):
                result[category].append(request)
    return result

def show_filtered_requests():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.geometry("900x600")
    app.title("Filtered Beneficiary Requests")

    # Set background image
    try:
        bg_image = Image.open("images/login.jpg")  # Change path if needed
        bg_image = bg_image.resize((900, 600))
        bg_ctk = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(900, 600))
        bg_label = ctk.CTkLabel(app, image=bg_ctk, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Could not load background image:", e)
        app.configure(fg_color="#F1F1F1")

    # Frame
    frame = ctk.CTkFrame(app, corner_radius=15, fg_color="white", width=750, height=500)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Title
    title = ctk.CTkLabel(frame, text="Request Categories", font=ctk.CTkFont(size=22, weight="bold"), text_color="#222")
    title.pack(pady=(15, 5))

    # Categorize
    categorized = categorize_requests(sample_requests)

    # Display
    for category, requests in categorized.items():
        if requests:
            cat_label = ctk.CTkLabel(frame, text=f"{category}:", font=ctk.CTkFont(size=18, weight="bold"), text_color="#2E7D32")
            cat_label.pack(anchor="w", padx=20, pady=(10, 0))

            for r in requests:
                req_label = ctk.CTkLabel(frame, text=f"• {r}", anchor="w", text_color="#333", wraplength=700)
                req_label.pack(anchor="w", padx=30, pady=2)

    app.mainloop()

if __name__ == "__main__":
    show_filtered_requests()
