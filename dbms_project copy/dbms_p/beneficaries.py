# # import customtkinter as ctk
# # from tkinter import messagebox
# # import mysql.connector
# # import datetime
# # from PIL import Image, ImageTk
# # import os
# # # MySQL connection
# # conn = mysql.connector.connect(
# #     host="127.0.0.1",
# #     user="root",          # Replace with your username
# #     password="Tendu@123", # Replace with your password
# #     database="ngos"       # Replace with your DB name
# # )
# # cursor = conn.cursor()

# # # Set appearance
# # ctk.set_appearance_mode("light")  # or "dark"
# # ctk.set_default_color_theme("green")

# # # App Window
# # app = ctk.CTk()
# # app.title("Beneficiary Page")
# # app.geometry("800x600")

# # # ----------- Function to Load Data -----------  
# # def load_data():
# #     for widget in table_frame.winfo_children():
# #         widget.destroy()

# #     cursor.execute("SELECT * FROM beneficiaries")
# #     rows = cursor.fetchall()

# #     headings = ["ID", "Name", "Age", "Gender", "Contact"]
# #     for i, heading in enumerate(headings):
# #         lbl = ctk.CTkLabel(table_frame, text=heading, font=ctk.CTkFont(size=14, weight="bold"))
# #         lbl.grid(row=0, column=i, padx=10, pady=5)

# #     for idx, row in enumerate(rows):
# #         for j, val in enumerate(row):
# #             cell = ctk.CTkLabel(table_frame, text=str(val))
# #             cell.grid(row=idx+1, column=j, padx=10, pady=2)

# # # ----------- Add Beneficiary ----------- 
# # def add_beneficiary():
# #     name = name_entry.get()
# #     age = age_entry.get()
# #     gender = gender_menu.get()
# #     contact = contact_entry.get()

# #     if not (name and age and gender and contact):
# #         messagebox.showerror("Error", "Please fill all fields")
# #         return
# #     try:
# #         cursor.execute(
# #             "INSERT INTO beneficiaries (Name, Age, Gender, Contact) VALUES (%s, %s, %s, %s)",
# #             (name, int(age), gender, contact)
# #         )
# #         conn.commit()
# #         messagebox.showinfo("Success", "Beneficiary added successfully!")
# #         load_data()
# #         name_entry.delete(0, 'end')
# #         age_entry.delete(0, 'end')
# #         gender_menu.set("Select Gender")
# #         contact_entry.delete(0, 'end')
# #     except Exception as e:
# #         messagebox.showerror("Database Error", str(e))


# # # ----------- Submit Beneficiary Request -----------  



# # # ---------- Submit Request Logic ----------
# # def submit_request():
# #     beneficiary_id = entry_beneficiary_id.get()
# #     ngoid = entry_ngoid.get()
# #     req_text = entry_req.get()
# #     request_date = entry_date.get()
# #     status = 'Pending'

# #     if not (beneficiary_id and ngoid and req_text and request_date):
# #         messagebox.showerror("Missing Info", "Please fill in all fields.")
# #         return

# #     try:
# #         cursor.execute(
# #             "INSERT INTO reqs (BeneficiaryID, NGOid, Req, Date, Status) VALUES (%s, %s, %s, %s, %s)",
# #             (beneficiary_id, ngoid, req_text, request_date, status)
# #         )
# #         conn.commit()
# #         messagebox.showinfo("Success", "Request submitted successfully!")
# #         app.destroy()
# #         import main  # Assuming your main screen is in main.py
# #         main.main()

# #     except Exception as e:
# #         messagebox.showerror("Error", str(e))

# # # ---------- Go Back Logic ----------
# # def go_back():
# #     app.destroy()
# #     import main
# #     main.main()

# # # ---------- Main App Window ----------
# # app = ctk.CTk()
# # app.title("Beneficiary Request Form")
# # app.geometry("800x600")

# # # ---------- Try Loading Background Image ----------
# # try:
# #     image_path = "/mnt/data/image.png"  # Update if your path is different
# #     if not os.path.exists(image_path):
# #         raise FileNotFoundError("Background image not found.")

# #     bg_image = Image.open(image_path)
# #     bg_photo = ImageTk.PhotoImage(bg_image)
# #     bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
# #     bg_label.place(relwidth=1, relheight=1)

# # except Exception as e:
# #     print(f"[Warning] Could not load background image: {e}")
# #     app.configure(fg_color="#F0F4F8")  # fallback background color

# # # ---------- Form Container ----------
# # # ---------- Form Container ----------
# # form_container = ctk.CTkFrame(
# #     app,
# #     corner_radius=20,
# #     fg_color="white",
# #     border_width=1,
# #     border_color="#B2E5B2",
# #     width=450,
# #     height=450
# # )
# # form_container.place(relx=0.5, rely=0.5, anchor="center")


# # # ---------- Form Entries ----------
# # entry_beneficiary_id = ctk.CTkEntry(form_container, placeholder_text="Beneficiary ID")
# # entry_beneficiary_id.pack(pady=8, padx=20, fill="x")

# # entry_ngoid = ctk.CTkEntry(form_container, placeholder_text="NGO ID")
# # entry_ngoid.pack(pady=8, padx=20, fill="x")

# # entry_req = ctk.CTkEntry(form_container, placeholder_text="Request")
# # entry_req.pack(pady=8, padx=20, fill="x")

# # entry_date = ctk.CTkEntry(form_container, placeholder_text="Request Date (YYYY-MM-DD)")
# # entry_date.pack(pady=8, padx=20, fill="x")

# # # ---------- Submit Button ----------
# # submit_btn = ctk.CTkButton(form_container, text="Submit Request", fg_color="#3FA34D", hover_color="#338A3E", command=submit_request)
# # submit_btn.pack(pady=20)

# # # ---------- Back Button ----------
# # back_btn = ctk.CTkButton(app, text="Back", command=go_back)
# # back_btn.place(relx=0.5, rely=0.95, anchor="s")

# # app.mainloop()
# import customtkinter as ctk
# from tkinter import messagebox
# import mysql.connector
# import datetime
# from PIL import Image

# # MySQL connection
# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",          # Replace with your username
#     password="Tendu@123", # Replace with your password
#     database="ngos"       # Replace with your DB name
# )
# cursor = conn.cursor()

# # Set appearance
# ctk.set_appearance_mode("light")  # or "dark"
# ctk.set_default_color_theme("green")

# # App Window
# app = ctk.CTk()
# app.title("Beneficiary Page")
# app.geometry("800x600")

# # ----------- Function to Load Data -----------  
# def load_data():
#     for widget in table_frame.winfo_children():
#         widget.destroy()

#     cursor.execute("SELECT * FROM beneficiaries")
#     rows = cursor.fetchall()

#     headings = ["ID", "Name", "Age", "Gender", "Contact"]
#     for i, heading in enumerate(headings):
#         lbl = ctk.CTkLabel(table_frame, text=heading, font=ctk.CTkFont(size=14, weight="bold"))
#         lbl.grid(row=0, column=i, padx=10, pady=5)

#     for idx, row in enumerate(rows):
#         for j, val in enumerate(row):
#             cell = ctk.CTkLabel(table_frame, text=str(val))
#             cell.grid(row=idx+1, column=j, padx=10, pady=2)

# # ----------- Add Beneficiary ----------- 
# def add_beneficiary():
#     name = name_entry.get()
#     age = age_entry.get()
#     gender = gender_menu.get()
#     contact = contact_entry.get()

#     if not (name and age and gender and contact):
#         messagebox.showerror("Error", "Please fill all fields")
#         return
#     try:
#         cursor.execute(
#             "INSERT INTO beneficiaries (Name, Age, Gender, Contact) VALUES (%s, %s, %s, %s)",
#             (name, int(age), gender, contact)
#         )
#         conn.commit()
#         messagebox.showinfo("Success", "Beneficiary added successfully!")
#         load_data()
#         name_entry.delete(0, 'end')
#         age_entry.delete(0, 'end')
#         gender_menu.set("Select Gender")
#         contact_entry.delete(0, 'end')
#     except Exception as e:
#         messagebox.showerror("Database Error", str(e))


# # ----------- Submit Beneficiary Request -----------  
# def submit_beneficiary_request(beneficiary_id, ngo_id, req, request_date, status):
#     if not beneficiary_id or not ngo_id or not req or not request_date or status is None:
#         messagebox.showerror("Error", "Please fill all fields.")
#         return

#     try:
#         # Insert request data into the reqs table
#         cursor.execute("""
#             INSERT INTO reqs (BeneficiaryID, NGOid, Req, Date, Status) 
#             VALUES (%s, %s, %s, %s, %s)
#         """, (beneficiary_id, ngo_id, req, request_date, status))
#         conn.commit()
#         messagebox.showinfo("Success", "Beneficiary request submitted successfully!")
#     except Exception as e:
#         messagebox.showerror("Database Error", str(e))

# # ----------- Request Form -----------  
# def show_beneficiary_request():
#     import customtkinter as ctk
#     import main  # Assuming this is where your welcome page function is

#     request_window = ctk.CTk()
#     request_window.title("Beneficiary Request")
#     request_window.geometry("500x400")

#     beneficiary_id_label = ctk.CTkLabel(request_window, text="Beneficiary ID:")
#     beneficiary_id_label.pack(pady=10)
#     beneficiary_id_entry = ctk.CTkEntry(request_window)
#     beneficiary_id_entry.pack(pady=10)

#     ngo_id_label = ctk.CTkLabel(request_window, text="NGO ID:")
#     ngo_id_label.pack(pady=10)
#     ngo_id_entry = ctk.CTkEntry(request_window)
#     ngo_id_entry.pack(pady=10)

#     req_label = ctk.CTkLabel(request_window, text="Request:")
#     req_label.pack(pady=10)
#     req_entry = ctk.CTkEntry(request_window)
#     req_entry.pack(pady=10)

#     date_label = ctk.CTkLabel(request_window, text="Request Date (YYYY-MM-DD):")
#     date_label.pack(pady=10)
#     date_entry = ctk.CTkEntry(request_window)
#     date_entry.pack(pady=10)

#     status_label = ctk.CTkLabel(request_window, text="Status (TRUE/FALSE):")
#     status_label.pack(pady=10)
#     status_entry = ctk.CTkEntry(request_window)
#     status_entry.pack(pady=10)

#     submit_button = ctk.CTkButton(request_window, text="Submit Request",
#                                   command=lambda: submit_beneficiary_request(
#                                       beneficiary_id_entry.get(),
#                                       ngo_id_entry.get(),
#                                       req_entry.get(),
#                                       date_entry.get(),
#                                       status_entry.get()
#                                   ))
#     submit_button.pack(pady=20)

#     def go_back():
#         request_window.destroy()  # Close the current window (request_window)
#         welcome_root.deiconify()  # Show the main window (welcome_root) again
#         welcome_root.lift()  # Ensure the main window is in the foreground

#     back_btn = ctk.CTkButton(request_window, text="Back", command=go_back)
#     back_btn.pack(pady=20)

#     request_window.mainloop()
  


# def submit_request():
#     beneficiary_id = entry_beneficiary_id.get()
#     ngoid = entry_ngoid.get()
#     req_text = entry_req.get()
#     date_today = datetime.date.today()
#     status = 'Pending'

#     if not (beneficiary_id and ngoid and req_text):
#         messagebox.showerror("Missing Info", "Please fill in all fields.")
#         return

#     try:
#         # Insert request into DB
#         cursor.execute(
#             "INSERT INTO reqs (BeneficiaryID, NGOid, Req, Date, Status) VALUES (%s, %s, %s, %s, %s)",
#             (beneficiary_id, ngoid, req_text, date_today, status)
#         )
#         conn.commit()
#         messagebox.showinfo("Success", "Request submitted successfully!")

#         # ❌ Close previous request window if it exists
#         request_window.destroy()

#         # ✅ Create a new frame with a background image
#         result_frame = ctk.CTkFrame(app, width=800, height=600, corner_radius=0)
#         result_frame.pack(fill="both", expand=True)

#         # Try loading background image
#         try:
#             bg_image = ctk.CTkImage(light_image=Image.open("images/login.jpg"), size=(800, 600))
#             bg_label = ctk.CTkLabel(result_frame, image=bg_image, text="")
#             bg_label.place(relx=0.5, rely=0.5, anchor="center")
#         except Exception as img_err:
#             print("Couldn't load background image:", img_err)
#             fallback_label = ctk.CTkLabel(result_frame, text="Request Submitted!", font=ctk.CTkFont(size=20, weight="bold"))
#             fallback_label.pack(pady=40)

#         # Add a Back button on top of image
#         back_btn = ctk.CTkButton(result_frame, text="Back", command=lambda: [result_frame.destroy(), app.deiconify()])
#         back_btn.place(relx=0.5, rely=0.85, anchor="center")

#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# # ----------- Entry Form Frame -----------  
# form_frame = ctk.CTkFrame(app, corner_radius=10)
# form_frame.pack(pady=20, padx=20, fill="x")

# name_label = ctk.CTkLabel(form_frame, text="Name:")
# name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
# name_entry = ctk.CTkEntry(form_frame, width=200)
# name_entry.grid(row=0, column=1, padx=10, pady=5)

# age_label = ctk.CTkLabel(form_frame, text="Age:")
# age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
# age_entry = ctk.CTkEntry(form_frame, width=200)
# age_entry.grid(row=1, column=1, padx=10, pady=5)

# gender_label = ctk.CTkLabel(form_frame, text="Gender:")
# gender_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
# gender_menu = ctk.CTkOptionMenu(form_frame, values=["Male", "Female", "Other"])
# gender_menu.set("Select Gender")
# gender_menu.grid(row=2, column=1, padx=10, pady=5)

# contact_label = ctk.CTkLabel(form_frame, text="Contact:")
# contact_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
# contact_entry = ctk.CTkEntry(form_frame, width=200)
# contact_entry.grid(row=3, column=1, padx=10, pady=5)

# submit_btn = ctk.CTkButton(form_frame, text="Add Beneficiary", command=add_beneficiary)
# submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

# # ----------- Table Display Frame -----------  
# # table_frame = ctk.CTkScrollableFrame(app, width=700, height=300)
# # table_frame.pack(pady=20)

# # Add the Back button
# # back_btn = ctk.CTkButton(app, text="Back", command=go_back)
# # back_btn.pack(pady=10)

# def go_back():
#     app.destroy()  # Close current page
#     import main    # Assuming main.py has a main() function
#     main.main()

# table_frame = ctk.CTkScrollableFrame(app, width=700, height=300)
# table_frame.pack(pady=20)

# # ✅ Now this button will work, since go_back is defined above
# back_btn = ctk.CTkButton(app, text="Back", command=go_back)
# back_btn.pack(pady=10)

# load_data()

# app.mainloop()

# # if __name__ == "__main__":
# #     show_beneficiary_request()
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import datetime

# MySQL connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",          # Replace with your username
    password="mysql@123", # Replace with your password
    database="ngos"       # Replace with your DB name
)
cursor = conn.cursor()

# Set appearance
ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("green")

# App Window
app = ctk.CTk()
app.title("Beneficiary Page")
app.geometry("800x600")

# ----------- Function to Load Data -----------  
def load_data():
    for widget in table_frame.winfo_children():
        widget.destroy()

    cursor.execute("SELECT * FROM beneficiaries")
    rows = cursor.fetchall()

    headings = ["ID", "Name", "Age", "Gender", "Contact"]
    for i, heading in enumerate(headings):
        lbl = ctk.CTkLabel(table_frame, text=heading, font=ctk.CTkFont(size=14, weight="bold"))
        lbl.grid(row=0, column=i, padx=10, pady=5)

    for idx, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = ctk.CTkLabel(table_frame, text=str(val))
            cell.grid(row=idx+1, column=j, padx=10, pady=2)

# ----------- Add Beneficiary ----------- 
def add_beneficiary():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_menu.get()
    contact = contact_entry.get()

    if not (name and age and gender and contact):
        messagebox.showerror("Error", "Please fill all fields")
        return
    try:
        cursor.execute(
            "INSERT INTO beneficiaries (Name, Age, Gender, Contact) VALUES (%s, %s, %s, %s)",
            (name, int(age), gender, contact)
        )
        conn.commit()
        messagebox.showinfo("Success", "Beneficiary added successfully!")
        load_data()
        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        gender_menu.set("Select Gender")
        contact_entry.delete(0, 'end')
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


# ----------- Submit Beneficiary Request -----------  
def submit_beneficiary_request(beneficiary_id, ngo_id, req, request_date, status):
    if not beneficiary_id or not ngo_id or not req or not request_date or status is None:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        # Insert request data into the reqs table
        cursor.execute("""
            INSERT INTO reqs (BeneficiaryID, NGOid, Req, Date, Status) 
            VALUES (%s, %s, %s, %s, %s)
        """, (beneficiary_id, ngo_id, req, request_date, status))
        conn.commit()
        messagebox.showinfo("Success", "Beneficiary request submitted successfully!")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# ----------- Request Form -----------  
def show_beneficiary_request():
    import customtkinter as ctk
    import main  # Assuming this is where your welcome page function is

    request_window = ctk.CTk()
    request_window.title("Beneficiary Request")
    request_window.geometry("500x400")

    beneficiary_id_label = ctk.CTkLabel(request_window, text="Beneficiary ID:")
    beneficiary_id_label.pack(pady=10)
    beneficiary_id_entry = ctk.CTkEntry(request_window)
    beneficiary_id_entry.pack(pady=10)

    ngo_id_label = ctk.CTkLabel(request_window, text="NGO ID:")
    ngo_id_label.pack(pady=10)
    ngo_id_entry = ctk.CTkEntry(request_window)
    ngo_id_entry.pack(pady=10)

    req_label = ctk.CTkLabel(request_window, text="Request:")
    req_label.pack(pady=10)
    req_entry = ctk.CTkEntry(request_window)
    req_entry.pack(pady=10)

    date_label = ctk.CTkLabel(request_window, text="Request Date (YYYY-MM-DD):")
    date_label.pack(pady=10)
    date_entry = ctk.CTkEntry(request_window)
    date_entry.pack(pady=10)

    status_label = ctk.CTkLabel(request_window, text="Status (TRUE/FALSE):")
    status_label.pack(pady=10)
    status_entry = ctk.CTkEntry(request_window)
    status_entry.pack(pady=10)

    submit_button = ctk.CTkButton(request_window, text="Submit Request",
                                  command=lambda: submit_beneficiary_request(
                                      beneficiary_id_entry.get(),
                                      ngo_id_entry.get(),
                                      req_entry.get(),
                                      date_entry.get(),
                                      status_entry.get()
                                  ))
    submit_button.pack(pady=20)

    def go_back():
        request_window.destroy()  # Close the current window (request_window)
        welcome_root.deiconify()  # Show the main window (welcome_root) again
        welcome_root.lift()  # Ensure the main window is in the foreground

    back_btn = ctk.CTkButton(request_window, text="Back", command=go_back)
    back_btn.pack(pady=20)

    request_window.mainloop()
  


def submit_request():
    beneficiary_id = entry_beneficiary_id.get()
    ngoid = entry_ngoid.get()
    req_text = entry_req.get()
    date_today = datetime.date.today()
    status = 'Pending'

    if not (beneficiary_id and ngoid and req_text):
        messagebox.showerror("Missing Info", "Please fill in all fields.")
        return

    try:
        cursor.execute(
            "INSERT INTO reqs (BeneficiaryID, NGOid, Req, Date, Status) VALUES (%s, %s, %s, %s, %s)",
            (beneficiary_id, ngoid, req_text, date_today, status)
        )
        conn.commit()
        messagebox.showinfo("Request Submitted", "Your request has been submitted successfully!")

        messagebox.showinfo("Success", "Request submitted!")

        request_window.destroy()
        def go_back():
            app.destroy()  # Close current page
            import main    # Assuming main.py has a main() function
            main.main()

        table_frame = ctk.CTkScrollableFrame(app, width=700, height=300)
        table_frame.pack(pady=20)

        # ✅ Now this button will work, since go_back is defined above
        back_btn = ctk.CTkButton(app, text="Back", command=go_back)
        back_btn.pack(pady=10)
        show_main_menu()  # or your previous screen

        submit_btn = ctk.CTkButton(request_window, text="Submit", command=submit_request)
        submit_btn.pack(pady=10)

        def go_back():
            app.destroy()  # Close the current window
            import main  # Replace with your main file/module
            main.main()  # Call the main function from your main module

    # Create the Back button
        back_btn = ctk.CTkButton(app, text="Back", command=go_back)
        back_btn.pack(pady=10)
    

        app.mainloop()

        request_window.mainloop()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ----------- Entry Form Frame -----------  
form_frame = ctk.CTkFrame(app, corner_radius=10)
form_frame.pack(pady=20, padx=20, fill="x")

name_label = ctk.CTkLabel(form_frame, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = ctk.CTkEntry(form_frame, width=200)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = ctk.CTkLabel(form_frame, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
age_entry = ctk.CTkEntry(form_frame, width=200)
age_entry.grid(row=1, column=1, padx=10, pady=5)

gender_label = ctk.CTkLabel(form_frame, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
gender_menu = ctk.CTkOptionMenu(form_frame, values=["Male", "Female", "Other"])
gender_menu.set("Select Gender")
gender_menu.grid(row=2, column=1, padx=10, pady=5)

contact_label = ctk.CTkLabel(form_frame, text="Contact:")
contact_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
contact_entry = ctk.CTkEntry(form_frame, width=200)
contact_entry.grid(row=3, column=1, padx=10, pady=5)

submit_btn = ctk.CTkButton(form_frame, text="Add Beneficiary", command=add_beneficiary)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

# ----------- Table Display Frame -----------  
# table_frame = ctk.CTkScrollableFrame(app, width=700, height=300)
# table_frame.pack(pady=20)

# Add the Back button
# back_btn = ctk.CTkButton(app, text="Back", command=go_back)
# back_btn.pack(pady=10)

def go_back():
    app.destroy()  # Close current page
    import main    # Assuming main.py has a main() function
    main.main()

table_frame = ctk.CTkScrollableFrame(app, width=700, height=300)
table_frame.pack(pady=20)

# ✅ Now this button will work, since go_back is defined above
back_btn = ctk.CTkButton(app, text="Back", command=go_back)
back_btn.pack(pady=10)

load_data()

app.mainloop()

# if __name__ == "__main__":
#     show_beneficiary_request()