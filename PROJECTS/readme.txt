Project Name: Multi-Level File Organizer System
Developer: Ali Raza Saleem (BSCS Student)
Date: March 21, 2026 (Eid-ul-Fitr)

🚀 Overview
In this project, I moved from basic syntax to building a functional System. This system automates the boring task of manual file sorting by using Python's power to interact with the Windows Operating System.

🛠️ The Tech Stack
Language: Python 3.14

Library 1 (os): Used for directory scanning, path joining, and existence checks.

Library 2 (shutil): Used for high-level file operations (moving files across directories).

📋 Key Components Developed
Directory Scanner: A script that lists every file in a given path.

Folder Creator: A smart builder that checks for existing folders before creating new ones to avoid errors.

The Mover: A basic implementation of moving a single file from source to destination.

The Organizer (Main Asset): A complex script using nested loops and dictionary mapping to sort .txt and .csv files into their respective homes.

🧠 Logic Highlights
Safety First: Added os.path.isfile() to ensure the script doesn't try to move folders into themselves.

Case Sensitivity: Used .lower() for extensions to catch both Data.CSV and data.csv.

Path Resilience: Used raw strings (r"") to handle Windows backslashes correctly.