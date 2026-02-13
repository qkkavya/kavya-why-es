import customtkinter as ctk
import mysql.connector
from tkinter import messagebox

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@123",
    database="ngos"
)
cursor = conn.cursor()

def show_feedback_for_beneficiary(ben_id):
    print(f"Received BenID: {ben_id} (type: {type(ben_id)})")

    feedback_window = ctk.CTkToplevel()
    feedback_window.title(f"Feedback for Beneficiary ID: {ben_id}")
    feedback_window.geometry("600x400")

    try:
        cursor.execute("""
            SELECT Rating, Comment
            FROM feedback
            WHERE NGOid = %s
        """, (ben_id,))
        feedbacks = cursor.fetchall()
        print(f"Fetched feedbacks: {feedbacks}")
    except Exception as e:
        print(f"Error fetching feedbacks: {e}")
        feedbacks = []

    if not feedbacks:
        label = ctk.CTkLabel(feedback_window, text="No feedback available.", font=("Arial", 13, "italic"))
        label.pack(pady=20)
    else:
        heading = ctk.CTkLabel(feedback_window, text="Feedbacks Submitted by Beneficiaries:", font=("Arial", 15, "bold"))
        heading.pack(pady=10)

        for i, (rating, comment) in enumerate(feedbacks, start=1):
            stars = "⭐" * int(rating)
            feedback_text = f"{i}. {stars} ({rating}/5)\n    \"{comment}\""
            feedback_label = ctk.CTkLabel(
                feedback_window,
                text=feedback_text,
                anchor="w",
                justify="left",
                wraplength=550,
                font=("Arial", 12)
            )
            feedback_label.pack(anchor="w", padx=20, pady=8)





def show_requests_page():
    app = ctk.CTk()
    app.title("NGO - View & Manage Beneficiary Requests")
    app.geometry("1100x600")

    table_frame = ctk.CTkScrollableFrame(app, width=1050, height=400)
    table_frame.pack(pady=20)

    headers = ["Request ID", "Beneficiary ID", "NGO ID", "Request", "Date", "Status", "Update Status", "Feedback"]
    for col, header in enumerate(headers):
        label = ctk.CTkLabel(table_frame, text=header, font=("Arial", 12, "bold"))
        label.grid(row=0, column=col, padx=10, pady=5)

    cursor.execute("SELECT * FROM reqs")
    requests = cursor.fetchall()

    status_vars = []
    req_ids = []

    for i, row in enumerate(requests):
        req_id, ben_id, ngo_name, req_text, req_date, status = row[:6]

        req_ids.append(req_id)

        for j, val in enumerate(row):
            label = ctk.CTkLabel(table_frame, text=str(val))
            label.grid(row=i+1, column=j, padx=10, pady=2)

        # Dropdown for status
        status_var = ctk.StringVar(value=status)
        status_menu = ctk.CTkOptionMenu(table_frame, variable=status_var, values=["Pending", "Accepted", "Rejected", "Resolved"])
        status_menu.grid(row=i+1, column=6)
        status_vars.append(status_var)

        # View Feedback Button
        feedback_btn = ctk.CTkButton(
            table_frame,
            text="View Feedback",
            command=lambda ben_id=ben_id: show_feedback_for_beneficiary(ben_id)


        )
        feedback_btn.grid(row=i+1, column=7, padx=5)

    def update_statuses():
        for idx, var in enumerate(status_vars):
            new_status = var.get()
            req_id = req_ids[idx]
            cursor.execute("UPDATE reqs SET Status = %s WHERE ReqID = %s", (new_status, req_id))
        conn.commit()
        messagebox.showinfo("Success", "Statuses updated!")

    update_btn = ctk.CTkButton(app, text="Update Statuses", command=update_statuses)
    update_btn.pack(pady=10)

    def go_back():
        app.destroy()
        import main  # Replace with your main file/module
        main.main()

    back_btn = ctk.CTkButton(app, text="Back", command=go_back)
    back_btn.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    show_requests_page()
