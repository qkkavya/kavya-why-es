import customtkinter as ctk
from tkinter import messagebox
from db_config import get_connection
from tkcalendar import DateEntry
import datetime
import tkinter.ttk as ttk
import tkinter as tk

def view_volunteer_details():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Username, Email, contact_no, Category, Address, NGOID FROM volunteers")
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("No Volunteers", "There are no volunteer records.")
            return

        # Create window
        win = ctk.CTkToplevel()
        win.title("Volunteer Details")
        win.geometry("900x500")
        win.configure(bg="white")

        # Green banner header
        header = ctk.CTkFrame(win, fg_color="#5CAD8A")
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="Volunteer Details",
            font=("Arial", 18, "bold"),
            text_color="white"
        ).pack(pady=12)

        # Frame for Treeview + Scrollbars
        frame = ctk.CTkFrame(win)
        frame.pack(padx=10, pady=10, expand=True, fill="both")

        columns = ("Username", "Email", "contact_no", "Category", "Address", "NGO ID")

        # Scrollbars
        y_scroll = ttk.Scrollbar(frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        x_scroll = ttk.Scrollbar(frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        # Treeview
        tree = ttk.Treeview(frame, columns=columns, show="headings",
                            yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=140, anchor="center")

        # Insert rows with alternating tag styles
        for index, row in enumerate(rows):
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            tree.insert("", "end", values=row, tags=(tag,))

        tree.pack(fill="both", expand=True)
        y_scroll.config(command=tree.yview)
        x_scroll.config(command=tree.xview)

        # Style for Treeview
        style = ttk.Style()
        style.theme_use("default")

        # Column heading style
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="black",
                        foreground="white",
                        relief="raised")

        # Main Treeview style
        style.configure("Treeview",
                        rowheight=30,
                        font=('Arial', 11),
                        bordercolor="black",
                        borderwidth=1)

        # Row color tags
        tree.tag_configure('evenrow', background="#f0f0f0")  # light gray
        tree.tag_configure('oddrow', background="white")

        win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), win.destroy()])

    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch volunteers.\n{str(e)}")
def view_beneficiaries():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT ID, Name, Age, Gender, Contact FROM beneficiaries")
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("No Beneficiaries", "No beneficiary records found.")
            return

        # Create window
        win = ctk.CTkToplevel()
        win.title("Beneficiaries")
        win.geometry("700x400")
        win.configure(bg="white")

        # Green header banner for title
        header = ctk.CTkFrame(win, fg_color="#5CAD8A")  # Custom green background
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="Beneficiaries",
            font=("Arial", 18, "bold"),
            text_color="white"
        ).pack(pady=12)

        # Frame for Treeview + Scrollbars
        frame = ctk.CTkFrame(win)
        frame.pack(padx=10, pady=10, expand=True, fill="both")

        columns = ("ID", "Name", "Age", "Gender", "Contact")

        # Scrollbars
        y_scroll = ttk.Scrollbar(frame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        x_scroll = ttk.Scrollbar(frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        # Treeview
        tree = ttk.Treeview(frame, columns=columns, show="headings", yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=130, anchor="center")

        # Insert rows with alternating colors
        for index, row in enumerate(rows):
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            tree.insert("", "end", values=row, tags=(tag,))

        tree.pack(expand=True, fill="both")
        y_scroll.config(command=tree.yview)
        x_scroll.config(command=tree.xview)

        # Treeview Style
        style = ttk.Style()
        style.theme_use("default")

        # Column heading style
        style.configure("Treeview.Heading",
                        font=('Arial', 12, 'bold'),
                        background="black",  # Column heading background black
                        foreground="white",
                        relief="raised")

        # Main Treeview style (for rows)
        style.configure("Treeview",
                        rowheight=30,
                        font=('Arial', 11),
                        bordercolor="black",
                        borderwidth=1)

        # Row color tags
        tree.tag_configure('evenrow', background="#f0f0f0")  # light gray for even rows
        tree.tag_configure('oddrow', background="white")  # white for odd rows

        win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), win.destroy()])

    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch beneficiaries.\n{str(e)}")

def assign_task_to_volunteer():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        assign_win = ctk.CTkToplevel()
        assign_win.title("Assign Task")
        assign_win.geometry("600x500")
        assign_win.configure(fg_color="white")

        # Header
        header_frame = ctk.CTkFrame(assign_win, fg_color="white")
        header_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(header_frame, text="Task Assignment", font=("Arial", 20, "bold"), text_color="#333").pack(anchor="w", padx=30)
        ctk.CTkLabel(header_frame, text="Create and assign a new task", font=("Arial", 12), text_color="#888").pack(anchor="w", padx=30)

        form_frame = ctk.CTkFrame(assign_win, fg_color="white")
        form_frame.pack(padx=40, pady=10, fill="both", expand=True)

        # Title
        ctk.CTkLabel(form_frame, text="Title", anchor="w", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 2))
        task_desc_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter task title")
        task_desc_entry.pack(fill="x", pady=5)

        # Description (optional, but removed as per code logic — if needed, add back)
        # ctk.CTkLabel(form_frame, text="Description", anchor="w").pack(anchor="w", pady=(10, 2))
        # task_description_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter task description")
        # task_description_entry.pack(fill="x", pady=5)

        # Due Date
                # Deadline Label
        ctk.CTkLabel(form_frame, text="Deadline", anchor="w", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 2))

        deadline_container = ctk.CTkFrame(form_frame, fg_color="white")
        deadline_container.pack(fill="x", pady=5)

        # Entry to show selected date
        deadline_entry = ctk.CTkEntry(deadline_container, placeholder_text="YYYY-MM-DD")
        deadline_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        def open_calendar():
            # Temporary top-level window for calendar
            top = tk.Toplevel(assign_win)
            top.title("Select Date")
            top.geometry("250x220")
            top.transient(assign_win)  # Attach to parent window
            top.grab_set()             # Make it modal so it grabs all focus


            cal = DateEntry(top, width=12, background='darkblue',
                            foreground='white', borderwidth=2, year=2025, date_pattern='yyyy-mm-dd')
            cal.pack(pady=20)

            def select_date():
                deadline_entry.delete(0, tk.END)
                deadline_entry.insert(0, cal.get_date().strftime("%Y-%m-%d"))
                top.destroy()

            ttk.Button(top, text="Select", command=select_date).pack(pady=10)

                # Calendar Button
        calendar_button = ctk.CTkButton(deadline_container, text="📅", width=40, command=open_calendar)
        calendar_button.pack(side="right")


        # Assign To
        ctk.CTkLabel(form_frame, text="Assign To", anchor="w", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 2))
        volunteer_id_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter volunteer username")
        volunteer_id_entry.pack(fill="x", pady=5)

        # Optional Event ID
        ctk.CTkLabel(form_frame, text="Event ID (optional)", anchor="w", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 2))
        event_id_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Event ID (if any)")
        event_id_entry.pack(fill="x", pady=5)

        # Button Frame
        button_frame = ctk.CTkFrame(form_frame, fg_color="white")
        button_frame.pack(pady=20)

        def submit_task():
            try:
                vid = volunteer_id_entry.get()
                task_name = task_desc_entry.get()
                deadline = deadline_entry.get()
                eid = event_id_entry.get() if event_id_entry.get().isdigit() else None

                if not vid or not task_name or not deadline:
                    messagebox.showerror("Invalid Input", "Fill all required fields correctly.")
                    return

                cursor.execute("""
                    INSERT INTO tasks (Name, Deadline, EventsID)
                    VALUES (%s, %s, %s)
                """, (task_name, deadline, eid))
                task_id = cursor.lastrowid

                cursor.execute("""
                    INSERT INTO volunteer_tasks (VolunteerUsername, TaskID, task_name)
                    VALUES (%s, %s, %s)
                """, (vid, task_id, task_name))

                conn.commit()
                messagebox.showinfo("Success", f"Task '{task_name}' assigned to Volunteer '{vid}' successfully!")
                assign_win.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Task assignment failed.\n{str(e)}")
            finally:
                cursor.close()
                conn.close()

        # Buttons
        ctk.CTkButton(button_frame, text="Cancel", fg_color="lightgray", text_color="black", hover_color="#ddd", command=assign_win.destroy).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Create Task", fg_color="#5CAD8A", hover_color="green", command=submit_task).pack(side="left", padx=10)

        assign_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), assign_win.destroy()])

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        # Calendar Button
        calendar_button = ctk.CTkButton(deadline_container, text="📅", width=40, command=open_calendar)
        calendar_button.pack(side="right")


        # Assign To
        ctk.CTkLabel(form_frame, text="Assign To", anchor="w", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 2))
        volunteer_id_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter volunteer username")
        volunteer_id_entry.pack(fill="x", pady=5)

        # Optional Event ID
        ctk.CTkLabel(form_frame, text="Event ID (optional)", anchor="w", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10, 2))
        event_id_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter Event ID (if any)")
        event_id_entry.pack(fill="x", pady=5)

        # Button Frame
        button_frame = ctk.CTkFrame(form_frame, fg_color="white")
        button_frame.pack(pady=20)

        def submit_task():
            try:
                vid = volunteer_id_entry.get()
                task_name = task_desc_entry.get()
                deadline = deadline_entry.get()
                eid = event_id_entry.get() if event_id_entry.get().isdigit() else None

                if not vid or not task_name or not deadline:
                    messagebox.showerror("Invalid Input", "Fill all required fields correctly.")
                    return

                cursor.execute("""
                    INSERT INTO tasks (Name, Deadline, EventsID)
                    VALUES (%s, %s, %s)
                """, (task_name, deadline, eid))
                task_id = cursor.lastrowid

                cursor.execute("""
                    INSERT INTO volunteer_tasks (VolunteerUsername, TaskID, task_name)
                    VALUES (%s, %s, %s)
                """, (vid, task_id, task_name))

                conn.commit()
                messagebox.showinfo("Success", f"Task '{task_name}' assigned to Volunteer '{vid}' successfully!")
                assign_win.destroy()

            except Exception as e:
                messagebox.showerror("Error", f"Task assignment failed.\n{str(e)}")
            finally:
                cursor.close()
                conn.close()

        # Buttons
        ctk.CTkButton(button_frame, text="Cancel", fg_color="lightgray", text_color="black", hover_color="#ddd", command=assign_win.destroy).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Create Task", fg_color="#5CAD8A", hover_color="green", command=submit_task).pack(side="left", padx=10)

        assign_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), assign_win.destroy()])

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))