# import customtkinter as ctk
# import os
# from tkinter import messagebox
# from db_config import get_connection  # You already have this
# from volunteer import view_tasks  # type: ignore
# from volunteer import update_info
# from volunteer import view_updated_info
# from PIL import Image, ImageTk  # type: ignore

# ctk.set_appearance_mode("light") 

# ctk.set_default_color_theme("green")  # You can change this theme

# # ---------- Login Checking ----------
# def check_login(role, username, password):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         if role == "volunteer":
#             query = "SELECT * FROM volunteers WHERE Username = %s AND Password = %s"
#             cursor.execute(query, (username, password))
#             result = cursor.fetchone()
#             name = result[0] if result else None

#         elif role == "coordinator":
#             query = "SELECT * FROM coords WHERE coord_username = %s AND Password = %s"
#             cursor.execute(query, (username, password))
#             result = cursor.fetchone()
#             name = f"Coordinator {result[0]}" if result else None

#         elif role == "sponsor":
#             query = "SELECT * FROM sponsors WHERE Name = %s"
#             cursor.execute(query, (username,))
#             result = cursor.fetchone()
#             name = result[2] if result else None

#         elif role == "beneficiary":
#             query = "SELECT * FROM beneficiaries WHERE Name = %s"
#             cursor.execute(query, (username,))
#             result = cursor.fetchone()
#             name = result[1] if result else None

#         else:
#             return False, None

#         cursor.close()
#         conn.close()

#         return (True, name) if result else (False, None)

#     except Exception as err:
#         messagebox.showerror("Database Error", f"Error: {err}")
#         return False, None

# # ---------- Role-Specific Pages ----------
# def open_volunteer_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Volunteer Page")
#     win.geometry("400x300")
#     win.configure(fg_color="#e6ffe6")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="View My Tasks", command=lambda: view_tasks(name)).pack()
#     ctk.CTkButton(win, text="View Events", width=200).pack(pady=5)
#     ctk.CTkButton(win, text="Update Personal Information", width=250, command=lambda: update_info(name)).pack(pady=5)
#     ctk.CTkButton(win, text="View Updated Personal Information", width=250, command=lambda: view_updated_info(name)).pack(pady=5)

# def open_coordinator_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Coordinator Page")
#     win.geometry("400x250")
#     win.configure(fg_color="#e6f2ff")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="Assign Tasks", width=200).pack(pady=10)
#     ctk.CTkButton(win, text="View Events", width=200).pack(pady=10)

# def open_beneficiary_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Beneficiary Page")
#     win.geometry("300x200")
#     win.configure(fg_color="#fff0f5")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="View Rating", width=200).pack(pady=20)

# def open_sponsor_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Sponsor Page")
#     win.geometry("300x200")
#     win.configure(fg_color="#f0fff0")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="Contribute", width=200).pack(pady=20)

# def open_role_page(role, name):
#     if role == "volunteer":
#         open_volunteer_page(name)
#     elif role == "coordinator":
#         open_coordinator_page(name)
#     elif role == "beneficiary":
#         open_beneficiary_page(name)
#     elif role == "sponsor":
#         open_sponsor_page(name)
#     else:
#         messagebox.showerror("Error", f"No page found for role: {role}")

# # ---------- Login GUI ----------
# def show_login():
#     login_root = ctk.CTk()
#     login_root.title("Login Page")
#     login_root.geometry("400x300")

#     # ---- Background Image ----
#     script_dir = os.path.dirname(__file__)
#     img_path = os.path.join(script_dir, "images", "bg.jpg")
#     bg_image = Image.open(img_path).resize((400, 300))
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = ctk.CTkLabel(login_root, image=bg_photo, text="")
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     login_root.configure(fg_color="#e6e6e6")

#     ctk.CTkLabel(login_root, text="Role:").pack(pady=(20, 5))
#     role_var = ctk.StringVar(value="volunteer")
#     ctk.CTkOptionMenu(login_root, variable=role_var, values=["volunteer", "coordinator", "beneficiary", "sponsor"]).pack(pady=5)

#     ctk.CTkLabel(login_root, text="Username / ID / Name:").pack()
#     username_entry = ctk.CTkEntry(login_root)
#     username_entry.pack(pady=5)

#     ctk.CTkLabel(login_root, text="Password (if required):").pack()
#     password_entry = ctk.CTkEntry(login_root, show="*")
#     password_entry.pack(pady=5)

#     def on_login():
#         role = role_var.get()
#         username = username_entry.get().strip()
#         password = password_entry.get().strip()

#         if not username:
#             messagebox.showerror("Error", "Please enter a username or name.")
#             return

#         if role in ["volunteer", "coordinator"] and not password:
#             messagebox.showerror("Error", "Password is required for this role.")
#             return

#         success, name = check_login(role, username, password)

#         if success:
#             open_role_page(role, name)
#         else:
#             messagebox.showerror("Login Failed", "Invalid credentials.")

#     ctk.CTkButton(login_root, text="Login", width=100, command=on_login).pack(pady=20)

#     login_root.mainloop()

# # ---------- Run the App ----------
# if __name__ == "__main__":
#     show_login()


# MANSI RIRI CODE 

# import tkinter as tk
# from tkinter import messagebox
# from db_config import get_connection  # You already have this
# from volunteer import view_tasks # type: ignore
# from volunteer import update_info
# from volunteer import view_updated_info
# from volunteer import view_events
# from sponsor import view_all_events
# from sponsor import view_top_sponsors
# from sponsor import update_sponsor_contribution

# # ---------- Login Checking ----------
# def check_login(role, username, password):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         if role == "volunteer":
#             query = "SELECT * FROM volunteers WHERE Username = %s AND Password = %s"
#             cursor.execute(query, (username, password))
#             result = cursor.fetchone()
#             name = result[0] if result else None  # Username as name

#         elif role == "coordinator":
#             query = "SELECT * FROM coords WHERE coordID = %s AND Password = %s"
#             cursor.execute(query, (username, password))
#             result = cursor.fetchone()
#             name = f"Coordinator {result[0]}" if result else None

#         elif role == "sponsor":
#             query = "SELECT * FROM sponsors WHERE Name = %s"
#             cursor.execute(query, (username,))
#             result = cursor.fetchone()
#             name = result[2] if result else None  # Name

#         elif role == "beneficiary":
#             query = "SELECT * FROM beneficiaries WHERE Name = %s"
#             cursor.execute(query, (username,))
#             result = cursor.fetchone()
#             name = result[1] if result else None  # Name

#         else:
#             return False, None

#         cursor.close()
#         conn.close()

#         return (True, name) if result else (False, None)

#     except Exception as err:
#         messagebox.showerror("Database Error", f"Error: {err}")
#         return False, None

# # ---------- Role-Specific Pages ----------
# def open_volunteer_page(name):
#     win = tk.Toplevel()
#     win.title("Volunteer Page")
#     win.geometry("400x300")
#     win.configure(bg="#e6ffe6")
#     tk.Label(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     tk.Button(win, text="View My Tasks", command=lambda: view_tasks(name)).pack()
#     tk.Button(win, text="View Events", width=20 ).pack(pady=5)
#     tk.Button(win, text="Update Personal Information", width=25,command=lambda: update_info(name)).pack(pady=5)
#     tk.Button(win, text= "view Updated Personal Information", width=25,command=lambda: view_updated_info(name)).pack(pady=5)
#     tk.Button(win, text= "view events near you", width=25,command=lambda: view_events(name)).pack(pady=5)

# def open_coordinator_page(name):
#     win = tk.Toplevel()
#     win.title("Coordinator Page")
#     win.geometry("400x250")
#     win.configure(bg="#e6f2ff")
#     tk.Label(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     tk.Button(win, text="Assign Tasks", width=20).pack(pady=10)
#     tk.Button(win, text="View Events", width=20).pack(pady=10)

# def open_beneficiary_page(name):
#     win = tk.Toplevel()
#     win.title("Beneficiary Page")
#     win.geometry("300x200")
#     win.configure(bg="#fff0f5")
#     tk.Label(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     tk.Button(win, text="View Rating", width=20).pack(pady=20)

# def open_sponsor_page(name):
#     win = tk.Toplevel()
#     win.title("Sponsor Page")
#     win.geometry("300x200")
#     win.configure(bg="#f0fff0")
#     tk.Label(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     tk.Button(win, text="Contribute", width=20,command=lambda: update_sponsor_contribution()).pack(pady=20)
#     tk.Button(win, text="View Events", width=20,command=lambda: view_all_events()).pack(pady=20)
#     tk.Button(win, text="View top spnosors ", width=20,command=lambda: view_top_sponsors()).pack(pady=20)
#     tk.Button(win, text="View top spno", width=20,command=lambda: view_top_sponsors()).pack(pady=20)


# def open_role_page(role, name):
#     if role == "volunteer":
#         open_volunteer_page(name)
#     elif role == "coordinator":
#         open_coordinator_page(name)
#     elif role == "beneficiary":
#         open_beneficiary_page(name)
#     elif role == "sponsor":
#         open_sponsor_page(name)
#     else:
#         messagebox.showerror("Error", f"No page found for role: {role}")

# # ---------- Login GUI ----------
# def show_login():
#     login_root = tk.Tk()
#     login_root.title("Login Page")
#     login_root.geometry("400x300")
#     login_root.configure(bg="#ccccff")

#     tk.Label(login_root, text="Role:").pack(pady=(20, 5))
#     role_var = tk.StringVar(login_root)
#     role_var.set("volunteer")
#     roles = ["volunteer", "coordinator", "beneficiary", "sponsor"]
#     tk.OptionMenu(login_root, role_var, *roles).pack(pady=5)

#     tk.Label(login_root, text="Username / ID / Name:").pack()
#     username_entry = tk.Entry(login_root)
#     username_entry.pack(pady=5)

#     tk.Label(login_root, text="Password (if required):").pack()
#     password_entry = tk.Entry(login_root, show="*")
#     password_entry.pack(pady=5)

#     def on_login():
#         role = role_var.get()
#         username = username_entry.get().strip()
#         password = password_entry.get().strip()

#         if not username:
#             messagebox.showerror("Error", "Please enter a username or name.")
#             return

#         if role in ["volunteer", "coordinator"] and not password:
#             messagebox.showerror("Error", "Password is required for this role.")
#             return

#         success, name = check_login(role, username, password)

#         if success:
#             open_role_page(role, name)
#         else:
#             messagebox.showerror("Login Failed", "Invalid credentials.")


#     tk.Button(login_root, text="Login", width=10, command=on_login).pack(pady=20)

#     login_root.mainloop()

# # ---------- Run the App ----------
# if __name__ == "__main__":
#     show_login()

# KAVYA CODE

# import customtkinter as ctk
# import os
# from tkinter import messagebox
# from db_config import get_connection  # You already have this
# from volunteer import view_tasks  # type: ignore
# from volunteer import update_info
# from volunteer import view_updated_info
# from PIL import Image, ImageTk  # type: ignore

# ctk.set_appearance_mode("light") 

# ctk.set_default_color_theme("green")  # You can change this theme

# # ---------- Login Checking ----------
# def check_login(role, username, password):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         if role == "volunteer":
#             query = "SELECT * FROM volunteers WHERE Username = %s AND Password = %s"
#             cursor.execute(query, (username, password))
#             result = cursor.fetchone()
#             name = result[0] if result else None

#         elif role == "coordinator":
#             query = "SELECT * FROM coords WHERE coord_username = %s AND Password = %s"
#             cursor.execute(query, (username, password))
#             result = cursor.fetchone()
#             name = f"Coordinator {result[0]}" if result else None

#         elif role == "sponsor":
#             query = "SELECT * FROM sponsors WHERE Name = %s"
#             cursor.execute(query, (username,))
#             result = cursor.fetchone()
#             name = result[2] if result else None

#         elif role == "beneficiary":
#             query = "SELECT * FROM beneficiaries WHERE Name = %s"
#             cursor.execute(query, (username,))
#             result = cursor.fetchone()
#             name = result[1] if result else None

#         else:
#             return False, None

#         cursor.close()
#         conn.close()

#         return (True, name) if result else (False, None)

#     except Exception as err:
#         messagebox.showerror("Database Error", f"Error: {err}")
#         return False, None

# # ---------- Role-Specific Pages ----------
# def open_volunteer_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Volunteer Page")
#     win.geometry("400x300")
#     win.configure(fg_color="#e6ffe6")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="View My Tasks", command=lambda: view_tasks(name)).pack()
#     ctk.CTkButton(win, text="View Events", width=200).pack(pady=5)
#     ctk.CTkButton(win, text="Update Personal Information", width=250, command=lambda: update_info(name)).pack(pady=5)
#     ctk.CTkButton(win, text="View Updated Personal Information", width=250, command=lambda: view_updated_info(name)).pack(pady=5)

# def open_coordinator_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Coordinator Page")
#     win.geometry("400x250")
#     win.configure(fg_color="#e6f2ff")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="Assign Tasks", width=200).pack(pady=10)
#     ctk.CTkButton(win, text="View Events", width=200).pack(pady=10)

# def open_beneficiary_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Beneficiary Page")
#     win.geometry("300x200")
#     win.configure(fg_color="#fff0f5")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="View Rating", width=200).pack(pady=20)

# def open_sponsor_page(name):
#     win = ctk.CTkToplevel()
#     win.title("Sponsor Page")
#     win.geometry("300x200")
#     win.configure(fg_color="#f0fff0")
#     ctk.CTkLabel(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
#     ctk.CTkButton(win, text="Contribute", width=200).pack(pady=20)

# def open_role_page(role, name):
#     if role == "volunteer":
#         open_volunteer_page(name)
#     elif role == "coordinator":
#         open_coordinator_page(name)
#     elif role == "beneficiary":
#         open_beneficiary_page(name)
#     elif role == "sponsor":
#         open_sponsor_page(name)
#     else:
#         messagebox.showerror("Error", f"No page found for role: {role}")

# # ---------- Login GUI ----------
# def show_login():
#     login_root = ctk.CTk()
#     login_root.title("Login Page")
#     login_root.geometry("400x300")

#     # ---- Background Image ----
#     script_dir = os.path.dirname(__file__)
#     img_path = os.path.join(script_dir, "images", "bg.jpg")
#     bg_image = Image.open(img_path).resize((400, 300))
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = ctk.CTkLabel(login_root, image=bg_photo, text="")
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     login_root.configure(fg_color="#e6e6e6")

#     ctk.CTkLabel(login_root, text="Role:").pack(pady=(20, 5))
#     role_var = ctk.StringVar(value="volunteer")
#     ctk.CTkOptionMenu(login_root, variable=role_var, values=["volunteer", "coordinator", "beneficiary", "sponsor"]).pack(pady=5)

#     ctk.CTkLabel(login_root, text="Username / ID / Name:").pack()
#     username_entry = ctk.CTkEntry(login_root)
#     username_entry.pack(pady=5)

#     ctk.CTkLabel(login_root, text="Password (if required):").pack()
#     password_entry = ctk.CTkEntry(login_root, show="*")
#     password_entry.pack(pady=5)

#     def on_login():
#         role = role_var.get()
#         username = username_entry.get().strip()
#         password = password_entry.get().strip()

#         if not username:
#             messagebox.showerror("Error", "Please enter a username or name.")
#             return

#         if role in ["volunteer", "coordinator"] and not password:
#             messagebox.showerror("Error", "Password is required for this role.")
#             return

#         success, name = check_login(role, username, password)

#         if success:
#             open_role_page(role, name)
#         else:
#             messagebox.showerror("Login Failed", "Invalid credentials.")

#     ctk.CTkButton(login_root, text="Login", width=100, command=on_login).pack(pady=20)

#     login_root.mainloop()

# # ---------- Run the App ----------
# if __name__ == "__main__":
#     show_login()
import tkinter as tk
from tkinter import messagebox
from db_config import get_connection  
from volunteer import view_tasks 
from volunteer import update_info
from volunteer import view_updated_info
from volunteer import view_events
from sponsor import view_all_events
from sponsor import view_top_sponsors
from sponsor import update_sponsor_contribution
from sponsor import openPayment
from coordinator import view_volunteer_details
from coordinator import view_beneficiaries
from coordinator import assign_task_to_volunteer
from PIL import Image, ImageTk 
def assign_ngos_to_reqs():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE reqs r
        JOIN (
            SELECT n1.ID, n1.Category
            FROM ngos n1
            JOIN (
                SELECT Category, MIN(ID) AS min_id FROM ngos GROUP BY Category
            ) n2 ON n1.Category = n2.Category AND n1.ID >= n2.min_id
            ORDER BY RAND()
        ) selected_ngos ON r.Category = selected_ngos.Category
        SET r.NGOID = selected_ngos.ID;
        """
        cursor.execute(query)
        conn.commit()
        messagebox.showinfo("Success", "NGOs assigned to requests successfully.")
        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Failed to assign NGOs.\nError: {e}")
# ---------- Login Checking ----------
def check_login(role, username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if role == "volunteer":
            query = "SELECT * FROM volunteers WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            name = result[0] if result else None  # Username as name

        elif role == "coordinator":
            query = "SELECT * FROM coords WHERE coordID = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            name = f"Coordinator {result[0]}" if result else None

        elif role == "sponsor":
            query = "SELECT * FROM sponsors WHERE Name = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            name = result[2] if result else None  # Name

        elif role == "beneficiary":
            query = "SELECT * FROM beneficiaries WHERE Name = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            name = result[1] if result else None  # Name

        else:
            return False, None

        cursor.close()
        conn.close()

        return (True, name) if result else (False, None)

    except Exception as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return False, None

# ---------- Role-Specific Pages ----------
def open_volunteer_page(name):
    win = tk.Toplevel()
    win.title("Volunteer Page")
    win.geometry("500x500")  # Match login size

    try:
        bg_image = Image.open("images/login.jpg")
        bg_image = bg_image.resize((500, 500))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(win, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Could not load background image: {e}")
        win.configure(bg="#ccffcc")

    # White form-style frame
    form_frame = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
    form_frame.place(relx=0.5, rely=0.5, anchor="center", width=320, height=350)

    tk.Label(form_frame, text=f"Welcome, {name}!", font=("Arial", 16, "bold"), bg="white").pack(pady=15)

    tk.Button(form_frame, text="View My Tasks", width=25, command=lambda: view_tasks(name)).pack(pady=5)
    tk.Button(form_frame, text="View Events", width=25, command=lambda: view_events(name)).pack(pady=5)
    tk.Button(form_frame, text="Update Info", width=25, command=lambda: update_info(name)).pack(pady=5)
    tk.Button(form_frame, text="View Updated Info", width=25, command=lambda: view_updated_info(name)).pack(pady=5)

def open_coordinator_page(name):
    win = tk.Toplevel()
    win.title("Coordinator Page")
    win.geometry("400x350")
    try:
        bg_image = Image.open("images/login.jpg")
        bg_image = bg_image.resize((500, 500))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(win, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Could not load background image: {e}")
        win.configure(bg="#ccffcc")
    

    form_frame = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
    form_frame.place(relx=0.5, rely=0.5, anchor="center", width=280, height=280)

    tk.Label(form_frame, text=f"Welcome, {name}!", font=("Arial", 16, "bold"), bg="white").pack(pady=15)

    tk.Button(form_frame, text="Assign Tasks", width=25, command=assign_task_to_volunteer).pack(pady=5)
    tk.Button(form_frame, text="View Volunteer Details", width=25, command=view_volunteer_details).pack(pady=5)
    tk.Button(form_frame, text="View Beneficiaries", width=25, command=view_beneficiaries).pack(pady=5)
    tk.Button(form_frame, text="Assign NGOs to Requests", width=25, command=assign_ngos_to_reqs).pack(pady=5)

def open_beneficiary_page(name):
    win = tk.Toplevel()
    win.title("Beneficiary Page")
    win.geometry("300x200")
    win.configure(bg="#fff0f5")
    tk.Label(win, text=f"Welcome, {name}!", font=("Arial", 16)).pack(pady=10)
    tk.Button(win, text="View Rating", width=20).pack(pady=20)

def open_sponsor_page(name):
    win = tk.Toplevel()
    win.title("Sponsor Page")
    win.geometry("400x350")

    try:
        bg_image = Image.open("images/login.jpg")
        bg_image = bg_image.resize((500, 500))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(win, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Could not load background image: {e}")
        win.configure(bg="#ccffcc")
    

    form_frame = tk.Frame(win, bg="white", bd=0, highlightthickness=0)
    form_frame.place(relx=0.5, rely=0.5, anchor="center", width=250, height=210)
    form_frame.pack_propagate(False) 

    tk.Label(form_frame, text=f"Welcome, {name}!", font=("Arial", 16, "bold"), bg="white").pack(pady=15)

    tk.Button(form_frame, text="Contribute", width=25, command=lambda: update_sponsor_contribution()).pack(pady=5)
    tk.Button(form_frame, text="View Events", width=25, command=lambda: view_all_events()).pack(pady=5)
    tk.Button(form_frame, text="View Top Sponsors", width=25, command=lambda: view_top_sponsors()).pack(pady=5)
    tk.Button(form_frame, text="Payment Portal", width=25, command=lambda: openPayment()).pack(pady=5)
    

def open_role_page(role, name):
    if role == "volunteer":
        open_volunteer_page(name)
    elif role == "coordinator":
        open_coordinator_page(name)
    elif role == "beneficiary":
        open_beneficiary_page(name)
    elif role == "sponsor":
        open_sponsor_page(name)
    else:
        messagebox.showerror("Error", f"No page found for role: {role}")

# ---------- Login GUI ----------
def show_login():
    login_root = tk.Tk()
    login_root.title("Login Page")
    login_root.geometry("500x500")
    login_root.resizable(False, False)

    # Load background image
    try:
        bg_image = Image.open("images/login.jpg")
        bg_image = bg_image.resize((500, 500))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(login_root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Could not load background image: {e}")
        login_root.configure(bg="#ccffcc")

    # Main white form frame
    form_frame = tk.Frame(login_root, bg="white", bd=0, highlightthickness=0)
    form_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=370)

    # Heading
    tk.Label(form_frame, text="Login Form", font=("Arial", 18, "bold"), bg="white").pack(pady=(20, 5))
    tk.Label(form_frame, text="Welcome back!", font=("Arial", 12), fg="gray", bg="white").pack(pady=(0, 15))

    # Role
    tk.Label(form_frame, text="Role", bg="white", anchor="w").pack(fill="x", padx=38)
    role_var = tk.StringVar()
    role_var.set("volunteer")
    role_dropdown = tk.OptionMenu(form_frame, role_var, "volunteer", "coordinator", "sponsor")
    role_dropdown.config(width=25)
    role_dropdown.pack(pady=5, padx=(40, 0), anchor="w")  # Adjust X here for alignment under the label

    # Username
    tk.Label(form_frame, text="Username / ID / Name", bg="white", anchor="w").pack(fill="x", padx=30, pady=(10, 0))
    username_entry = tk.Entry(form_frame, width=30)
    username_entry.pack(pady=5)

    # Password
    tk.Label(form_frame, text="Password (if required)", bg="white", anchor="w").pack(fill="x", padx=30, pady=(10, 0))
    password_entry = tk.Entry(form_frame, width=30, show="*")
    password_entry.pack(pady=5)
    def on_login():
        role = role_var.get()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Please enter a username or name.")
            return

        if role in ["volunteer", "coordinator"] and not password:
            messagebox.showerror("Error", "Password is required for this role.")
            return

        success, name = check_login(role, username, password)

        if success:
            open_role_page(role, name)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")


    tk.Button(
    form_frame, 
    text="Login", 
    width=10, 
    command=on_login,
    bg="green",       # Background color
    fg="black",       # Text color
    activebackground="darkgreen",  # Optional: color when pressed
    activeforeground="white"       # Optional: text color when pressed
).pack(pady=20)


    login_root.mainloop()

# ---------- Run the App ----------
if __name__ == "__main__":
    show_login()
