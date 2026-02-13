import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from db_config import get_connection
import tkinter as tk
from tkinter import ttk

def view_all_events():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT ID, Name, Location, Date, amt_required, status, ngoID 
            FROM events
        """)
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("No Events", "There are no events to display.")
            return

        view_win = ctk.CTkToplevel()
        view_win.title("All Events")
        view_win.geometry("950x450")

        # Title with custom green background
        title_frame = ctk.CTkFrame(view_win, fg_color="#6BBF59")  # custom green
        title_frame.pack(fill="x")

        ctk.CTkLabel(title_frame, text="All Events", font=("Arial", 18, "bold"), text_color="white").pack(pady=10)

        import tkinter.ttk as ttk
        style = ttk.Style()
        style.theme_use("default")

        # Column header styling: black bg and white text
        style.configure("Treeview.Heading",
                        background="black",
                        foreground="white",
                        font=("Arial", 12, "bold"))

        # Treeview base styling: gridlines feel using borders and alt row colors
        style.configure("Treeview",
                        background="white",
                        fieldbackground="white",
                        foreground="black",
                        rowheight=25,
                        bordercolor="#CCCCCC",
                        borderwidth=1,
                        font=("Arial", 11))

        style.map("Treeview", background=[("selected", "#A0CFA5")])  # light green highlight on selection

        # Frame for Treeview + scrollbar
        tree_frame = ctk.CTkFrame(view_win)
        tree_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("ID", "Name", "Location", "Date", "Amount Required", "Status", "NGO ID")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor="center")

        # Alternating row colors
        for i, row in enumerate(rows):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            tree.insert("", "end", values=row, tags=(tag,))

        tree.tag_configure("evenrow", background="white")
        tree.tag_configure("oddrow", background="#F0F0F0")  # light grey

        tree.pack(side="left", expand=True, fill="both")

        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        view_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), view_win.destroy()])

    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch events.\n{str(e)}")

def view_top_sponsors():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            SELECT s.ID, s.Name, SUM(s.Amount) AS amt_contributed, s.VIP
            FROM sponsors s
            GROUP BY s.ID, s.Name, s.VIP
            ORDER BY amt_contributed DESC
            LIMIT 3;
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("Info", "No sponsors found.")
            return

        top_win = ctk.CTkToplevel()
        top_win.title("Top Sponsors")
        top_win.geometry("600x300")

        # Custom green background for heading
        title_frame = ctk.CTkFrame(top_win, fg_color="#6BBF59")
        title_frame.pack(fill="x")

        ctk.CTkLabel(title_frame, text="Top Sponsors", font=("Arial", 16, "bold"), text_color="white").pack(pady=10)

        import tkinter.ttk as ttk
        style = ttk.Style()
        style.theme_use("default")

        # Column header styling: black bg and white text
        style.configure("Treeview.Heading",
                        background="black",
                        foreground="white",
                        font=("Arial", 12, "bold"))

        # Treeview styling: alternating rows, selected row highlight
        style.configure("Treeview",
                        background="white",
                        fieldbackground="white",
                        foreground="black",
                        rowheight=25,
                        bordercolor="#CCCCCC",
                        borderwidth=1,
                        font=("Arial", 11))

        style.map("Treeview", background=[("selected", "#A0CFA5")])

        # Frame for Treeview
        tree_frame = ctk.CTkFrame(top_win)
        tree_frame.pack(expand=True, fill="both", padx=10, pady=10)

        columns = ("ID", "Name", "Amount Contributed", "VIP Status")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=140, anchor="center")

        for i, row in enumerate(rows):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            tree.insert("", "end", values=row, tags=(tag,))

        tree.tag_configure("evenrow", background="white")
        tree.tag_configure("oddrow", background="#F0F0F0")  # light grey

        tree.pack(side="left", expand=True, fill="both")

        # Scrollbar if needed
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        top_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), top_win.destroy()])

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch sponsors\n{str(e)}")

def update_sponsor_contribution():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        update_win = ctk.CTkToplevel()
        update_win.title("Add Contribution")
        update_win.geometry("400x300")

        try:
            bg_image = Image.open("images/login.jpg")
            bg_image = bg_image.resize((400, 300))
            bg_img = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(400, 300))
            bg_label = ctk.CTkLabel(update_win, image=bg_img, text="")
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Could not load background image: {e}")
            update_win.configure(bg_color="#b3e6ff")

        form_frame = ctk.CTkFrame(update_win, fg_color="#ffffff", width=300, height=240, corner_radius=10)
        form_frame.place(relx=0.5, rely=0.5, anchor="center")
        form_frame.pack_propagate(False) 

        title_label = ctk.CTkLabel(form_frame, text="Add Amount", font=("Arial", 16, "bold"))
        title_label.pack(pady=(10, 5))

        ctk.CTkLabel(form_frame, text="Sponsor ID").pack()
        sponsor_id_entry = ctk.CTkEntry(form_frame)
        sponsor_id_entry.pack(pady=5)

        ctk.CTkLabel(form_frame, text="Contributing Amount").pack()
        amount_entry = ctk.CTkEntry(form_frame)
        amount_entry.pack(pady=5)

        def submit_addition():
            try:
                sponsor_id = sponsor_id_entry.get()
                add_amount = amount_entry.get()

                if not sponsor_id.isdigit() or not add_amount.isdigit() or int(add_amount) <= 0:
                    messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
                    return

                cursor.execute("SELECT Amount FROM sponsors WHERE ID = %s", (sponsor_id,))
                result = cursor.fetchone()

                if result is None:
                    messagebox.showwarning("Not Found", "Sponsor ID not found.")
                    return

                current_amount = result[0]
                new_amount = current_amount + int(add_amount)

                cursor.execute("UPDATE sponsors SET Amount = %s WHERE ID = %s", (new_amount, sponsor_id))
                conn.commit()

                messagebox.showinfo("Success", f"New Total Contribution: ₹{new_amount}")
                update_win.destroy()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        ctk.CTkButton(form_frame, text="Add Contribution", command=submit_addition, fg_color="green").pack(pady=15)

        update_win.protocol("WM_DELETE_WINDOW", lambda: [cursor.close(), conn.close(), update_win.destroy()])

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))

def openECheckWindow(form_data):
    echeck_window = tk.Toplevel()
    echeck_window.title("eCheck Confirmation")
    echeck_window.geometry("500x400")
    echeck_window.configure(bg="white")

    title = tk.Label(echeck_window, text="eCheck Summary", font=("Helvetica", 16, "bold"), bg="white")
    title.pack(pady=10)

    table_frame = tk.Frame(echeck_window, bg="white")
    table_frame.pack(pady=10)

    # Tabular data display
    for i, (label, value) in enumerate(form_data.items()):
        tk.Label(table_frame, text=label + ":", font=("Helvetica", 10, "bold"), bg="white", anchor="w", width=20).grid(row=i, column=0, sticky="w")
        tk.Label(table_frame, text=value, bg="white", width=30, anchor="w").grid(row=i, column=1, sticky="w")

    # Thank you message
    tk.Label(echeck_window, text="\nThank you for your contribution!\nYour support means a lot to us.\n- From Team NGO",
             font=("Helvetica", 12), bg="white", fg="#3399ff", pady=20).pack()


def openPayment():
    window = tk.Toplevel()
    window.title("Change Payment Method")
    window.geometry("800x500")
    window.configure(bg="white")

    # Store form data
    form_data = {
        "First Name": "",
        "Last Name": "",
        "Card Number": "",
        "Exp Date": "",
        "Contribution Amount": "",
        "Street Address": "",
        "Suite": "",
        "City": "",
        "State": "",
        "Zip": "",
        "Country": ""
    }

    # Title
    title = tk.Label(window, text="Change Payment Method", font=("Helvetica", 16, "bold"), bg="white")
    title.pack(pady=10)

    # Toggle buttons (Credit Card / eCheck)
    toggle_frame = tk.Frame(window, bg="white")
    toggle_frame.pack()

    def echeck_clicked():
        # Fill form_data before opening new page
        form_data["First Name"] = first_name_entry.get()
        form_data["Last Name"] = last_name_entry.get()
        form_data["Card Number"] = card_entry.get()
        form_data["Exp Date"] = f"{exp_month.get()}/{exp_year.get()}"
         # Example hardcoded value
        form_data["Street Address"] = address_entry.get()
        form_data["Suite"] = suite_entry.get()
        form_data["City"] = city_entry.get()
        form_data["State"] = state_entry.get()
        form_data["Zip"] = zip_entry.get()
        form_data["Country"] = country_combo.get()

        openECheckWindow(form_data)

    credit_btn = tk.Button(toggle_frame, text="Credit Card", width=20, bg="#3399ff", fg="white")
    echeck_btn = tk.Button(toggle_frame, text="eCheck", width=20, command=echeck_clicked)
    credit_btn.pack(side="left")
    echeck_btn.pack(side="left")

    # Main form frame
    form_frame = tk.Frame(window, bg="white")
    form_frame.pack(pady=20, padx=30, fill="both", expand=True)

    # Left: Card Info
    left_frame = tk.Frame(form_frame, bg="white")
    left_frame.grid(row=0, column=0, padx=20, sticky="n")

    tk.Label(left_frame, text="Card Number", bg="white").pack(anchor="w")
    card_entry = tk.Entry(left_frame, width=25)
    card_entry.pack()

    tk.Label(left_frame, text="Exp. Date (MM / YY)", bg="white", pady=5).pack(anchor="w")
    exp_frame = tk.Frame(left_frame, bg="white")
    exp_frame.pack(anchor="w")
    exp_month = tk.Entry(exp_frame, width=5)
    exp_month.pack(side="left", padx=5)
    exp_year = tk.Entry(exp_frame, width=5)
    exp_year.pack(side="left")

    tk.Label(left_frame, text="First Name", bg="white", pady=5).pack(anchor="w")
    first_name_entry = tk.Entry(left_frame, width=25)
    first_name_entry.pack()

    tk.Label(left_frame, text="Last Name", bg="white", pady=5).pack(anchor="w")
    last_name_entry = tk.Entry(left_frame, width=25)
    last_name_entry.pack()

    tk.Checkbutton(left_frame, text="Default Credit Card", bg="white").pack(pady=10)

    # Right: Billing Info
    right_frame = tk.Frame(form_frame, bg="white")
    right_frame.grid(row=0, column=1, padx=20, sticky="n")

    tk.Label(right_frame, text="Billing Information", font=("Helvetica", 10, "bold"), bg="white").pack(anchor="w")

    tk.Label(right_frame, text="Country", bg="white", pady=5).pack(anchor="w")
    country_combo = ttk.Combobox(right_frame, values=["United States", "India"], width=30)
    country_combo.pack()

    tk.Label(right_frame, text="Street Address", bg="white", pady=5).pack(anchor="w")
    address_entry = tk.Entry(right_frame, width=35)
    address_entry.pack()

    tk.Label(right_frame, text="Suite/Apt (Optional)", bg="white", pady=5).pack(anchor="w")
    suite_entry = tk.Entry(right_frame, width=35)
    suite_entry.pack()

    tk.Label(right_frame, text="City", bg="white", pady=5).pack(anchor="w")
    city_entry = tk.Entry(right_frame, width=35)
    city_entry.pack()

    tk.Label(right_frame, text="State/Province", bg="white", pady=5).pack(anchor="w")
    state_entry = tk.Entry(right_frame, width=35)
    state_entry.pack()

    tk.Label(right_frame, text="Zip/Postal Code", bg="white", pady=5).pack(anchor="w")
    zip_entry = tk.Entry(right_frame, width=35)
    zip_entry.pack()

    # Save/Back buttons
    button_frame = tk.Frame(window, bg="white")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Save", bg="#3399ff", fg="white", width=15).pack(side="left", padx=10)
    tk.Button(button_frame, text="Back", width=15).pack(side="left", padx=10)
