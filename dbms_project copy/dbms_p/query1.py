import tkinter as tk
from tkinter import ttk
import mysql.connector

def show_requests():
    for row in tree.get_children():
        tree.delete(row)

    conn = mysql.connector.connect(user='root', password='Tendu@123', database='ngos')
    cursor = conn.cursor()
    query = '''
        SELECT reqs.Req, reqs.Date, reqs.Status,
               beneficiaries.ID, beneficiaries.Name,
               ngos.ID, ngos.Name
        FROM reqs
        JOIN beneficiaries ON reqs.BeneficiaryID = beneficiaries.ID
        JOIN ngos ON reqs.NGOID = ngos.ID;
    '''
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        tree.insert("", "end", values=row)

    cursor.close()
    conn.close()

root = tk.Tk()
root.title("All Requests")

btn = tk.Button(root, text="Show All Requests", command=show_requests)
btn.pack()

columns = ("Req", "Date", "Status", "BeneficiaryID", "BeneficiaryName", "NGOID", "NGOName")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(fill="both", expand=True)

root.mainloop()