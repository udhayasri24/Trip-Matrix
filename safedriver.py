import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import csv


def intilize_database():

# ================= Database Setup =================
    def init_db():
        conn = sqlite3.connect("safedrive.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS trips (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vehicle_number TEXT,
                    driver_name TEXT,
                    start_location TEXT,
                    end_location TEXT,
                    distance REAL,
                    fuel_used REAL,
                    date TEXT
                )''')
        conn.commit()
        conn.close()

# ================= Core Operations =================
    def add_trip():
        vehicle = vehicle_entry.get()
        driver = driver_entry.get()
        start = start_entry.get()
        end = end_entry.get()
        distance = distance_entry.get()
        fuel = fuel_entry.get()

        if not (vehicle and driver and start and end and distance):
             messagebox.showerror("Error", "Please fill all required fields!")
             return

        conn = sqlite3.connect("safedrive.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO trips (vehicle_number, driver_name, start_location, end_location, distance, fuel_used, date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (vehicle, driver, start, end, float(distance), float(fuel or 0), datetime.now().strftime("%Y-%m-%d %H:%M")))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Trip logged successfully!")
        clear_entries()
        load_trips()

    def load_trips():
         for row in tree.get_children():
          tree.delete(row)
         conn = sqlite3.connect("safedrive.db")
         cur = conn.cursor()
         cur.execute("SELECT * FROM trips")
         for row in cur.fetchall():
          tree.insert("", tk.END, values=row)
          conn.close()

    def export_csv():
     conn = sqlite3.connect("safedrive.db")
     cur = conn.cursor()
     cur.execute("SELECT * FROM trips")
     rows = cur.fetchall()
     conn.close()

    with open("trip_log.csv", "w", newline='') as f:
     writer = csv.writer(f)
     writer.writerow(["ID", "Vehicle", "Driver", "Start", "End", "Distance", "Fuel Used", "Date"])
     writer.writerows(rows)

     messagebox.showinfo("Exported", "Trip data exported to trip_log.csv")

    def clear_entries():
         for entry in [vehicle_entry, driver_entry, start_entry, end_entry, distance_entry, fuel_entry]:
             entry.delete(0, tk.END)

# ================= GUI Setup =================
root = tk.Tk()
root.title("SafeDrive – Vehicle Trip Logger")
root.geometry("950x600")
root.config(bg="#F8F9FA")

title = tk.Label(root, text="🚗 SafeDrive – Vehicle Trip Logger", font=("Arial", 20, "bold"), bg="#800000", fg="white", pady=10)
title.pack(fill=tk.X)

# ====== Input Frame ======
frame = tk.Frame(root, bg="#FFF0F0", bd=2, relief=tk.RIDGE)
frame.pack(pady=10, padx=20, fill=tk.X)

labels = ["Vehicle No", "Driver Name", "Start Location", "End Location", "Distance (km)", "Fuel Used (L)"]
entries = []

for i, text in enumerate(labels):
    tk.Label(frame, text=text, bg="#FFF0F0", font=("Arial", 10, "bold")).grid(row=0, column=i, padx=8, pady=5)
    e = tk.Entry(frame, width=12)
    e.grid(row=1, column=i, padx=5)
    entries.append(e)

vehicle_entry, driver_entry, start_entry, end_entry, distance_entry, fuel_entry = entries

tk.Button(frame, text="Add Trip", bg="#800000", fg="white", command=add_trip).grid(row=1, column=6, padx=10)
tk.Button(frame, text="Export CSV", bg="#004080", fg="white", command=export_csv).grid(row=1, column=7, padx=10)

# ====== Trip Display ======
columns = ("ID", "Vehicle", "Driver", "Start", "End", "Distance", "Fuel", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings", height=18)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(padx=20, pady=10, fill=tk.BOTH)

load_trips()
init_db()

root.mainloop()
