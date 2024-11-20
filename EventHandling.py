import tkinter as tk
import webbrowser
import subprocess
from NAData import NADataHandling

class MultiPurposeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project App")

        window_width = 300
        window_height = 200
        self.root.geometry(f"{window_width}x{window_height}")

        # NADataHandling inicializálás
        self.datahandler = NADataHandling()

        self.button1 = tk.Button(root, text="Launch Apps\nfor School", command=self.open_studies)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(root, text="Personal Projects", command=self.open_personal_projects)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(root, text="Personal Time", command=self.open_own_time)
        self.button3.pack(pady=10)

    def open_studies(self):
        items = self.datahandler.NAgetStudy()
        self.open_items(items)

    def open_personal_projects(self):
        items = self.datahandler.NAgetProjects()
        self.open_items(items)

    def open_own_time(self):
        items = self.datahandler.NAgetOwnTime()
        self.open_items(items)

    def open_items(self, items):
        for item in items:
            if item.startswith("http"):
                webbrowser.open(item)
            else:
                try:
                    subprocess.Popen(item, shell=True)
                except Exception as e:
                    print(f"Couldn't open {item}: {e}")

