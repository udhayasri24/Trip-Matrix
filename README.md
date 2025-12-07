#Trip Matrix 
"Trip Matrix is a Python desktop application designed to record, manage, and export vehicle trip details. The system provides a simple Tkinter interface where users can enter vehicle number, driver name, start and end locations, distance traveled, and fuel used. Each entry is automatically saved with the current date, making trip logging fast and reliable. The application uses an SQLite database for secure offline storage. When a trip is added, the system validates the inputs, stores the data in the trips table, clears the entry fields, and refreshes the on-screen trip display. All stored trips are shown in a Treeview table, allowing users to easily review and manage their travel history."

A built-in Export to CSV feature allows users to export all trip records into a file named trip_log.csv. This is useful for reports, analysis, documentation, or fuel-tracking purposes. The project also demonstrates essential programming concepts such as GUI design, database handling, input validation, and file operations.

Key Features

Add and store trip details

Auto-generated date for every entry

SQLite database for offline storage

View trips in a GUI table

Export records to CSV

Simple, user-friendly interface

Technologies Used


Python, Tkinter, SQLite, CSV Module, Datetime

How to Run

1. Install Python 3

2. Open the project folder

3. Run the command:

python safedrive.py

Author
Chinthala Udhayasri
