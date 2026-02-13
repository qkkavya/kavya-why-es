import customtkinter as ctk
from PIL import Image
from db_config import get_connection  # Assuming you have a separate config for DB

ctk.set_appearance_mode("System")  # Light, Dark, or System
ctk.set_default_color_theme("green")

# def setup_form_window(window, image_path="images/login.jpg"):
#     # Set window size to match background
#     window.geometry("500x500")
#     window.title("Volunteer Sign Up")

#     # Load and place background image
#     bg_image = ctk.CTkImage(light_image=Image.open(image_path), size=(500, 500))
#     bg_label = ctk.CTkLabel(window, image=bg_image, text="")
#     bg_label.place(relx=0.5, rely=0.5, anchor="center")

#     # Create form frame with padding
#     form_frame = ctk.CTkFrame(window, width=400, height=400, corner_radius=15, fg_color="white")
#     form_frame.place(relx=0.5, rely=0.5, anchor="center")

#     # Add form elements
#     entries = {}
#     fields = ["Username", "Email", "Contact Number", "Password", "Category", "Address"]
#     for i, field in enumerate(fields):
#         entry = ctk.CTkEntry(form_frame, placeholder_text=field, width=240)
#         entry.pack(pady=(10 if i == 0 else 5, 5))
#         entries[field.lower().replace(" ", "_")] = entry

#     # Submit button
#     submit_btn = ctk.CTkButton(form_frame, text="Submit", width=240, fg_color="#57cc99", hover_color="#38a169")
#     submit_btn.pack(pady=15)

#     return entries, submit_btn


def open_signup_window(role):
    window = ctk.CTkToplevel()
    window.title(f"{role} Sign Up")
    window.geometry("400x550")
    window.configure(bg_color="#b3e6ff")

    # Load and set background image
    bg_image = ctk.CTkImage(light_image=Image.open("images/bg3.jpg"), size=(400, 550))
    bg_label = ctk.CTkLabel(window, image=bg_image, text="")  # text="" makes it only show image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    heading_label = ctk.CTkLabel(window, text=f"{role} Sign Up", font=("Arial", 24, "bold"), text_color="black")
    heading_label.place(x=100, y=100)

    if role.lower() == "volunteer":
        username_entry = ctk.CTkEntry(window, placeholder_text="Username")
        username_entry.place(x=100,y=160)

        email_entry = ctk.CTkEntry(window, placeholder_text="Email")
        email_entry.place(x=100,y=200)

        contact_entry = ctk.CTkEntry(window, placeholder_text="Contact Number")
        contact_entry.place(x=100,y=240)

        password_entry = ctk.CTkEntry(window, placeholder_text="Password", show="*")
        password_entry.place(x=100,y=280)

        category_entry = ctk.CTkEntry(window, placeholder_text="Category")
        category_entry.place(x=100,y=320)

        address_entry = ctk.CTkEntry(window, placeholder_text="Address")
        address_entry.place(x=100,y=360)

        def submit_volunteer():
            username = username_entry.get()
            email = email_entry.get()
            contact = contact_entry.get()
            password = password_entry.get()
            category = category_entry.get()
            address = address_entry.get()

            try:
                conn = get_connection()
                cursor = conn.cursor()

                insert_query = """
                    INSERT INTO Volunteers (Username, Email, contact_no, Password, Category, address, NGOID)
                    VALUES (%s, %s, %s, %s, %s, %s, NULL)
                """
                cursor.execute(insert_query, (username, email, contact, password, category, address))
                conn.commit()

                cursor.close()
                conn.close()

                ctk.CTkLabel(window, text="Volunteer sign up successful!", text_color="green").place(x=100,y=440)

            except Error as e:
                ctk.CTkLabel(window, text=f"Error: {e}", text_color="red").pack(pady=10)

        submit_btn = ctk.CTkButton(window, text="Submit", command=submit_volunteer)
        submit_btn.place(x=100,y=400)

    elif role.lower() == "sponsor":
        name_entry = ctk.CTkEntry(window, placeholder_text="Name")
        name_entry.place(x=120,y=160)

        def submit_sponsor():
            name = name_entry.get()

            try:
                conn = get_connection()
                cursor = conn.cursor()

                insert_query = """
                    INSERT INTO sponsors (Name)
                    VALUES (%s)
                """
                cursor.execute(insert_query, (name,))
                conn.commit()

                cursor.close()
                conn.close()

                ctk.CTkLabel(window, text="Sponsor sign up successful!", text_color="green").pack(pady=10)

            except Error as e:
                ctk.CTkLabel(window, text=f"Error: {e}", text_color="red").pack(pady=10)

        submit_btn = ctk.CTkButton(window, text="Submit", command=submit_sponsor)
        submit_btn.place(x=120,y=210)

    elif role.lower() == "beneficiary":
        name_entry = ctk.CTkEntry(window, placeholder_text="Name")
        name_entry.place(x=120,y=160)

        age_entry = ctk.CTkEntry(window, placeholder_text="Age")
        age_entry.place(x=120,y=200)

        gender_entry = ctk.CTkEntry(window, placeholder_text="Gender")
        gender_entry.place(x=120,y=240)

        contact_entry = ctk.CTkEntry(window, placeholder_text="Contact Number")
        contact_entry.place(x=120,y=280)

        def submit_beneficiary():
            name = name_entry.get()
            age = age_entry.get()
            gender = gender_entry.get()
            contact = contact_entry.get()

            try:
                conn = get_connection()
                cursor = conn.cursor()

                insert_query = """
                    INSERT INTO beneficiaries (Name, Age, Gender, Contact)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (name, age, gender, contact))
                conn.commit()

                cursor.close()
                conn.close()

                ctk.CTkLabel(window, text="Beneficiary sign up successful!", text_color="green").pack(pady=10)

            except Error as e:
                ctk.CTkLabel(window, text=f"Error: {e}", text_color="red").pack(pady=10)
    
        submit_btn = ctk.CTkButton(window, text="Submit", command=submit_beneficiary)
        submit_btn.place(x=120,y=320)

    elif role.lower() == "coordinator":
        username_entry = ctk.CTkEntry(window, placeholder_text="Username")
        username_entry.place(x=120,y=160)

        email_entry = ctk.CTkEntry(window, placeholder_text="Email")
        email_entry.place(x=120,y=200)

        coordID_entry = ctk.CTkEntry(window, placeholder_text="Coord ID")
        coordID_entry.place(x=120,y=240)

        contact_entry = ctk.CTkEntry(window, placeholder_text="Contact Number")
        contact_entry.place(x=120,y=280)

        password_entry = ctk.CTkEntry(window, placeholder_text="Password", show="*")
        password_entry.place(x=120,y=320)

        ngoid_entry = ctk.CTkEntry(window, placeholder_text="NGO ID")
        ngoid_entry.place(x=120,y=360)

        def submit_coordinator():
            username = username_entry.get()
            email = email_entry.get()
            coordID=coordID_entry.get()
            contact = contact_entry.get()
            password = password_entry.get()
            ngoid = ngoid_entry.get()

            try:
                conn = get_connection()
                cursor = conn.cursor()

                insert_query = """
                    INSERT INTO coords (NGOID, coord_username, Email, contact_no, Password, coordID)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (ngoid, username, email, contact, password,coordID))
                conn.commit()

                cursor.close()
                conn.close()

                ctk.CTkLabel(window, text="Coordinator sign up successful!", text_color="green").pack(pady=10)

            except Error as e:
                ctk.CTkLabel(window, text=f"Error: {e}", text_color="red").pack(pady=10)

        submit_btn = ctk.CTkButton(window, text="Submit", command=submit_coordinator)
        submit_btn.place(x=120,y=400)

    else:
        ctk.CTkLabel(window, text=f"Sign-up form for {role} coming soon!", font=("Arial", 16)).pack(pady=20)


def show_signup():
    root = ctk.CTk()
    root.title("Sign Up")
    root.geometry("900x600")
    root.resizable(False, False)

    # Load full-size image
    image = ctk.CTkImage(light_image=Image.open("signup.png"), size=(900, 600))
    image_label = ctk.CTkLabel(root, image=image, text="")
    image_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Transparent-ish frame on the left side for signup
    signup_frame = ctk.CTkFrame(root, width=300, height=600, fg_color="#ffffff", corner_radius=15)  # semi-transparent
    signup_frame.place(x=570, y=100)  # adjust x/y as needed to fit nicely into the blank area of the image

    role_label = ctk.CTkLabel(signup_frame, text="Select Role", font=("Arial", 32, "bold"))
    role_label.pack(pady=(30, 10))

    roles = ["Volunteer", "Sponsor", "Beneficiary", "Coordinator"]
    for role in roles:
        btn = ctk.CTkButton(
            signup_frame,
            text=role,
            width=230,
            height=35,
            command=lambda r=role: open_signup_window(r)
        )
        btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    show_signup()

