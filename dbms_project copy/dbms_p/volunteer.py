# import tkinter as tk
# import tkinter as tk
# from tkinter import ttk
# from db_config import get_connection

# def view_tasks(username):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         query = '''
#         SELECT t.ID AS task_id, v.VolunteerUsername AS volunteer_name, t.coordID AS Coord_ID
#         FROM Volunteer_Tasks v
#         JOIN tasks t ON t.ID = v.TaskID
#         WHERE v.VolunteerUsername = %s;
#         '''
#         cursor.execute(query, (username,))
#         results = cursor.fetchall()

#         cursor.close()
#         conn.close()

#         # Open a new window to show tasks
#         task_window = tk.Toplevel()
#         task_window.title(f"{username}'s Tasks")
#         task_window.geometry("500x400")

#         heading = tk.Label(task_window, text=f"Tasks for {username}", font=("Arial", 16, "bold"))
#         heading.pack(pady=10)

#         if results:
#             # Using Treeview for a tabular layout
#             tree = ttk.Treeview(task_window, columns=("Task ID", "Volunteer", "Coord ID"), show='headings')
#             tree.heading("Task ID", text="Task ID")
#             tree.heading("Volunteer", text="Volunteer")
#             tree.heading("Coord ID", text="Coord ID")
            
#             for row in results:
#                 tree.insert('', 'end', values=row)
            
#             tree.pack(expand=True, fill='both', padx=10, pady=10)
#         else:
#             msg = tk.Label(task_window, text="No tasks found.", fg="red", font=("Arial", 12))
#             msg.pack(pady=20)

#     except Exception as e:
#         error_win = tk.Toplevel()
#         error_win.title("Error")
#         tk.Label(error_win, text=f"Error viewing tasks:\n{e}", fg="red").pack(padx=20, pady=20)
# def update_info(username):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()

#         # Fetch current user data
#         cursor.execute("SELECT Username, Email, Password, Category FROM volunteers WHERE Username = %s", (username,))
#         user_data = cursor.fetchone()

#         if not user_data:
#             tk.messagebox.showerror("Error", "User not found.")
#             return

#         current_username, current_mail, current_password, current_category = user_data

#         # Create update window
#         update_win = tk.Toplevel()
#         update_win.title("Update Personal Info")
#         update_win.geometry("400x350")

#         tk.Label(update_win, text="Update Your Information", font=("Arial", 14, "bold")).pack(pady=10)

#         # Email
#         tk.Label(update_win, text="Email").pack()
#         mail_entry = tk.Entry(update_win)
#         mail_entry.insert(0, current_mail)
#         mail_entry.pack()

#         # Password
#         tk.Label(update_win, text="Password").pack()
#         password_entry = tk.Entry(update_win, show="*")
#         password_entry.insert(0, current_password)
#         password_entry.pack()

#         # Category Dropdown
#         tk.Label(update_win, text="Category").pack()
#         category_entry = ttk.Combobox(update_win, values=["Medical", "Teaching", "Cleaning"], state="readonly")
#         category_entry.set(current_category)
#         category_entry.pack()

#         def submit_update():
#             new_mail = mail_entry.get()
#             new_password = password_entry.get()
#             new_category = category_entry.get()

#             try:
#                 if not conn.is_connected():
#                     conn.reconnect()
#                 cursor.execute("""
#                     UPDATE volunteers
#                     SET Email = %s, Password = %s, Category = %s
#                     WHERE Username = %s
#                 """, (new_mail, new_password, new_category, username))
#                 conn.commit()

#                 tk.messagebox.showinfo("Success", "Information updated successfully.")
#                 update_win.destroy()

#             except Exception as e:
#                 tk.messagebox.showerror("Update Failed", str(e))

#         tk.Button(update_win, text="Update", command=submit_update, bg="blue", fg="white").pack(pady=20)

#         # Proper cleanup on window close
#         update_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), update_win.destroy()])

#     except Exception as e:
#         tk.messagebox.showerror("Error", str(e))
        
# def view_updated_info(username):
#     try:
#         conn = get_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT Username, Email, Password, Category FROM volunteers WHERE Username = %s", (username,))
#         result = cursor.fetchone()

#         if result:
#             info_text = f"""
#             Username: {result[0]}
#             Email: {result[1]}
#             Password: {result[2]}
#             Category: {result[3]}
#             """
#             tk.messagebox.showinfo("Updated Info", info_text)
#         else:
#             tk.messagebox.showerror("Error", "User not found.")

#         cursor.close()
#         conn.close()
#     except Exception as e:
#         tk.messagebox.showerror("Error", str(e))

# def view_events():
#         print("Events list loading...")
import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from db_config import get_connection
from PIL import Image, ImageTk

def view_tasks(username):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = '''
        SELECT t.ID AS task_id,t.Name as task_name, v.VolunteerUsername AS volunteer_name, t.coordID AS Coord_ID
        FROM Volunteer_Tasks v
        JOIN tasks t ON t.ID = v.TaskID
        WHERE v.VolunteerUsername = %s;
        '''
        cursor.execute(query, (username,))
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        # Open a new window to show tasks
        task_window = tk.Toplevel()
        task_window.title(f"{username}'s Tasks")
        task_window.geometry("500x400")
        task_window.configure(bg="white")

        # Title Label with green background
        heading_frame = tk.Frame(task_window, bg="#5CAD8A")
        heading_frame.pack(fill='x')
        heading = tk.Label(
            heading_frame,
            text=f"Tasks for {username}",
            font=("Arial", 16, "bold"),
            bg="#5CAD8A",
            fg="white"
        )
        heading.pack(pady=10)

        if results:
            # Style Treeview to mimic black gridlines
            style = ttk.Style()
            style.theme_use("default")

            style.configure("Treeview",
                            background="white",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="white",
                            bordercolor="black",
                            borderwidth=1,
                            relief="solid")

            style.configure("Treeview.Heading",
                            font=("Arial", 12, "bold"),
                            background="black",
                            foreground="white",
                            relief="raised",
                            borderwidth=1)

            tree = ttk.Treeview(task_window, columns=("Task ID", "Task Name", "Coord ID"), show='headings')

            # Headings
            tree.heading("Task ID", text="Task ID")
            tree.heading("Task Name", text="Task Name")
            tree.heading("Coord ID", text="Coord ID")

            # Columns
            tree.column("Task ID", anchor="center", width=100)
            tree.column("Task Name", anchor="center", width=180)
            tree.column("Coord ID", anchor="center", width=120)

            # Insert data with alternating tag styles
            for index, row in enumerate(results):
                tag = "oddrow" if index % 2 == 0 else "evenrow"
                tree.insert('', 'end', values=(row[0],row[1],row[3]), tags=(tag,))

            tree.tag_configure('oddrow', background='white')
            tree.tag_configure('evenrow', background='#f0f0f0')  # Light gray for striping

            tree.pack(expand=True, fill='both', padx=10, pady=10)

        else:
            msg = tk.Label(task_window, text="No tasks found.", fg="red", font=("Arial", 12), bg="white")
            msg.pack(pady=20)

    except Exception as e:
        error_win = tk.Toplevel()
        error_win.title("Error")
        tk.Label(error_win, text=f"Error viewing tasks:\n{e}", fg="red").pack(padx=20, pady=20)

def update_info(username):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch current user data
        cursor.execute("SELECT Username, Email, Password, Category FROM volunteers WHERE Username = %s", (username,))
        user_data = cursor.fetchone()

        if not user_data:
            tk.messagebox.showerror("Error", "User not found.")
            return

        current_username, current_mail, current_password, current_category = user_data

        # Create update window
        update_win = tk.Toplevel()
        update_win.title("Update Personal Info")
        update_win.geometry("500x500")
        update_win.resizable(False, False)

        # Background Image
        try:
            bg_image = Image.open("images/login.jpg")
            bg_image = bg_image.resize((500, 500))
            bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(update_win, image=bg_photo)
            bg_label.image = bg_photo
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Could not load background image: {e}")
            update_win.configure(bg="#ccffcc")

        # Form frame
        form_frame = tk.Frame(update_win, bg="white", bd=0)
        form_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

        tk.Label(form_frame, text="Update Your Information", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

        # Email
        tk.Label(form_frame, text="Email", bg="white").pack()
        mail_entry = tk.Entry(form_frame)
        mail_entry.insert(0, current_mail)
        mail_entry.pack()

        # Password
        tk.Label(form_frame, text="Password", bg="white").pack()
        password_entry = tk.Entry(form_frame, show="*")
        password_entry.insert(0, current_password)
        password_entry.pack()

        # Category Dropdown
        tk.Label(form_frame, text="Category", bg="white").pack()
        category_entry = ttk.Combobox(form_frame, values=["Medical", "Teaching", "Cleaning"], state="readonly")
        category_entry.set(current_category)
        category_entry.pack()

        def submit_update():
            new_mail = mail_entry.get()
            new_password = password_entry.get()
            new_category = category_entry.get()

            try:
                if not conn.is_connected():
                    conn.reconnect()
                cursor.execute("""
                    UPDATE volunteers
                    SET Email = %s, Password = %s, Category = %s
                    WHERE Username = %s
                """, (new_mail, new_password, new_category, username))
                conn.commit()

                tk.messagebox.showinfo("Success", "Information updated successfully.")
                update_win.destroy()

            except Exception as e:
                tk.messagebox.showerror("Update Failed", str(e))

                # Submit Button inside the form_frame
        tk.Button(form_frame, text="Update", command=submit_update,
          bg="#007BFF", fg="black", font=("Arial", 11, "bold"),
          activebackground="#0056b3", activeforeground="white").pack(pady=10)



        # Proper cleanup on window close
        update_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), update_win.destroy()])

    except Exception as e:
        tk.messagebox.showerror("Error", str(e))

        
def view_updated_info(username):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Username, Email, Password, Category FROM volunteers WHERE Username = %s", (username,))
        result = cursor.fetchone()

        if result:
            info_text = f"""
            Username: {result[0]}
            Email: {result[1]}
            Password: {result[2]}
            Category: {result[3]}
            """
            tk.messagebox.showinfo("Updated Info", info_text)
        else:
            tk.messagebox.showerror("Error", "User not found.")

        cursor.close()
        conn.close()
    except Exception as e:
        tk.messagebox.showerror("Error", str(e))

def view_events(username):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Execute the JOIN query to get events in the same city as the volunteer
        cursor.execute("""
            SELECT v.Username, v.Address, 
                   e.Name AS Event_Name, e.Location, e.Date
            FROM volunteers v
            JOIN events e ON v.Address = e.Location
            WHERE v.Username = %s
        """, (username,))

        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("No Events", "No events found in your location.")
            return

        # Create a new window to display the events
        view_win = tk.Toplevel()
        view_win.title("Events in Your Location")
        view_win.geometry("600x350")
        view_win.configure(bg="white")

        # Title Label
        title_label = tk.Label(
            view_win,
            text="View Events Near You",
            font=("Arial", 16, "bold"),
            bg="#5CAD8A",
            fg="white",
            pady=10
        )
        title_label.pack(fill="x")

        # Subtitle with location
        tk.Label(view_win, text=f"Events in {rows[0][1]}", font=("Arial", 12)).pack(pady=(10, 5))

        # Frame for Treeview
        frame = tk.Frame(view_win)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Scrollbars
        y_scroll = tk.Scrollbar(frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        x_scroll = tk.Scrollbar(frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        # Treeview for event display
        tree = ttk.Treeview(frame, columns=("username", "event_name", "location", "date"), show="headings",
                            yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        tree.heading("username", text="Username")
        tree.heading("event_name", text="Event Name")
        tree.heading("location", text="Location")
        tree.heading("date", text="Date")

        tree.column("username", width=100)
        tree.column("event_name", width=150)
        tree.column("location", width=120)
        tree.column("date", width=100)

        for row in rows:
            tree.insert("", tk.END, values=(row[0], row[2], row[3], row[4]))

        tree.pack(fill="both", expand=True)
        y_scroll.config(command=tree.yview)
        x_scroll.config(command=tree.xview)

        view_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), view_win.destroy()])

    except Exception as e:
        messagebox.showerror("Error", str(e))