
# import customtkinter as ctk
# from PIL import Image, ImageTk
# from login import show_login
# from signup import show_signup
# import time

# def welcome_screen():
#     # Set up theme and appearance
#     ctk.set_appearance_mode("light")
#     ctk.set_default_color_theme("green")

#     # Create root window
#     root = ctk.CTk()
#     root.title("NGO Database System")
#     root.geometry("1000x700")
#     root.minsize(600, 400)
    
    
#     try:
#     # Use the full path if needed
#         bg_image = Image.open("images/bg.jpg")
#         bg_image = bg_image.resize((1000, 700))  # Match initial window size
#         bg_img = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(1000, 700))
#         bg_label = ctk.CTkLabel(root, image=bg_img, text="")
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#     except Exception as e:
#       print(f"Could not load background image: {e}")
#     # Fallback solid color background
#       root.configure(fg_color=("#e0f2e9", "#2b3a2d"))
    
#     content_frame = ctk.CTkFrame(root, 
#                                 corner_radius=15, 
#                                 fg_color=("#f1f1f1", "#333333"),  # Light and dark mode colors
#                                 border_width=2,
#                                 border_color="#4CAF50")
#     content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.6)
    
    
#     title_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
#     title_frame.pack(pady=(20, 30))
    
#     title = ctk.CTkLabel(title_frame, 
#                          text="Khadya Daanam",
#                          font=ctk.CTkFont(family="Arial", size=40, weight="bold"),
#                          text_color=("#2E7D32", "#66BB6A"))  # Different colors for light/dark mode
#     title.pack()
    
#     subtitle = ctk.CTkLabel(title_frame, 
#                            text="Charity begins with you! <3",
#                            font=ctk.CTkFont(family="Arial", size=23),
#                            text_color=("#555555", "#BBBBBB"))
#     subtitle.pack(pady=(25, 0))
    
#     # Create button frame for better layout
#     button_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
#     button_frame.place(relx=0.5, rely=0.5, anchor="center")
    
#     # Enhanced buttons with hover effects
#     login_button = ctk.CTkButton(button_frame, 
#                                 text="Login", 
#                                 width=200, 
#                                 height=50,
#                                 corner_radius=10,
#                                 font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
#                                 fg_color="#4CAF50",
#                                 hover_color="#2E7D32",
#                                 command=lambda: [root.destroy(), show_login()])
#     login_button.pack(pady=10)
    
#     signup_button = ctk.CTkButton(button_frame, 
#                                  text="Sign Up", 
#                                  width=200, 
#                                  height=50,
#                                  corner_radius=10,
#                                  font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
#                                  fg_color="#66BB6A",
#                                  hover_color="#43A047",
#                                  command=lambda: [root.destroy(), show_signup()])
#     signup_button.pack(pady=10)
    
#     # Footer text
    
    
#     # Simple animation at startup
    
#     root.mainloop()

# if __name__ == "__main__":
#     welcome_screen()

## hiiiii
import customtkinter as ctk
from PIL import Image, ImageTk
from login import show_login
from signup import show_signup
from beneficaries import show_beneficiary_request  # Handles Submit Request
import request 

 # Ensure request.py has show_requests_page()

def welcome_screen():
    # Set up theme and appearance
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.title("NGO Database System")
    root.geometry("1000x700")
    root.minsize(600, 400)

    try:
        bg_image = Image.open("images/bg.jpg")  # Adjust path if needed
        bg_image = bg_image.resize((1000, 700))
        bg_img = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(1000, 700))
        bg_label = ctk.CTkLabel(root, image=bg_img, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Could not load background image: {e}")
        root.configure(fg_color=("#e0f2e9", "#2b3a2d"))

    content_frame = ctk.CTkFrame(root, 
                                 corner_radius=15, 
                                 fg_color=("#f1f1f1", "#333333"),
                                 border_width=2,
                                 border_color="#4CAF50")
    content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.7)

    title_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    title_frame.pack(pady=(20, 30))

    title = ctk.CTkLabel(title_frame, 
                         text="KindRoot Foundation",
                         font=ctk.CTkFont(family="Arial", size=40, weight="bold"),
                         text_color=("#2E7D32", "#66BB6A"))
    title.pack()

    subtitle = ctk.CTkLabel(title_frame, 
                            text="Charity begins with you! <3",
                            font=ctk.CTkFont(family="Arial", size=17),
                            text_color=("#555555", "#BBBBBB"))
    subtitle.pack(pady=(10, 0))

    # Buttons frame
    button_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    button_frame.place(relx=0.5, rely=0.5, anchor="center")

    login_button = ctk.CTkButton(button_frame, 
                                 text="Login", 
                                 width=200, 
                                 height=50,
                                 corner_radius=10,
                                 font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
                                 fg_color="#4CAF50",
                                 hover_color="#2E7D32",
                                 command=lambda: [root.destroy(), show_login()])
    login_button.pack(pady=10)

    signup_button = ctk.CTkButton(button_frame, 
                                  text="Sign Up", 
                                  width=200, 
                                  height=50,
                                  corner_radius=10,
                                  font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
                                  fg_color="#66BB6A",
                                  hover_color="#43A047",
                                  command=lambda: [root.destroy(), show_signup()])
    signup_button.pack(pady=10)

    request_button = ctk.CTkButton(button_frame, 
                                   text="Submit Request", 
                                   width=200, 
                                   height=50,
                                   corner_radius=10,
                                   font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
                                   fg_color="#A5D6A7",
                                   hover_color="#81C784",
                                   command=lambda: [root.destroy(), show_beneficiary_request()])
    request_button.pack(pady=10)

    def open_requests_with_password():
        def check_password():
            if password_entry.get() == "12345":
                pwd_window.destroy()
                request.show_requests_page()
            else:
                ctk.CTkMessagebox(title="Access Denied", message="Incorrect Password", icon="cancel")

        pwd_window = ctk.CTkToplevel(root)
        pwd_window.title("NGO Access - Enter Password")
        pwd_window.geometry("300x150")

        label = ctk.CTkLabel(pwd_window, text="Enter NGO Password:")
        label.pack(pady=10)

        password_entry = ctk.CTkEntry(pwd_window, show="*")
        password_entry.pack(pady=5)

        submit_btn = ctk.CTkButton(pwd_window, text="Submit", command=check_password)
        submit_btn.pack(pady=10)

    view_requests_button = ctk.CTkButton(button_frame, 
                                         text="View Requests", 
                                         width=200, 
                                         height=50,
                                         corner_radius=10,
                                         font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
                                         fg_color="#AED581",
                                         hover_color="#9CCC65",
                                         command=open_requests_with_password)
    view_requests_button.pack(pady=10)

    top_ngos_button = ctk.CTkButton(root, text="Top NGOs (by Rating)", 
                                width=200, 
                                height=50,
                                corner_radius=10,
                                font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
                                fg_color="#AED400",
                                hover_color="#9CCC65",
                                command=lambda: [root.destroy(), __import__("top_ngos").show_top_ngos()])

    top_ngos_button.place(relx=0.5, rely=0.745, anchor="center")  # perfectly spaced below View Requests
    # top_ngos_button.pack(pady=450)





    root.mainloop()

    root.mainloop()

if __name__ == "__main__":
    welcome_screen()
