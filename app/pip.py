import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

library = simpledialog.askstring("Library", "Enter name of a library to download")
try:
  install(library)
except Exception as e:
  messagebox.showerror("Error", e)
else:
  messagebox.showinfo("Info", f"Successfully installed {library}.")
