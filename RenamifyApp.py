import tkinter as tk
from tkinter import filedialog
import os

class RenamifyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Renamify")
        self.resizable(False, False)

        self.mode_options = {
            "Add Prefix": "prefix",
            "Add Suffix": "suffix",
            "Replace Existing": "replace"
        }
        
        # Variables
        self.var_folder_path = tk.StringVar(value="C:/Your Path")
        self.var_mode = tk.StringVar(value="Add Prefix")
        self.var_new_name = tk.StringVar(value="New Name")

        self.create_widgets()


    def create_widgets(self):
        # Widgets for folder selection
        lbl_select_folder = tk.Label(self, text="Select Folder:")
        lbl_select_folder.grid(row=0, column=0, padx=10, pady=10)

        self.ent_folder_path = tk.Entry(self, textvariable=self.var_folder_path, state="disabled")
        self.ent_folder_path.grid(row=1, columnspan=2, column=0, sticky="ew", padx=10, pady=0)

        btn_browse_folder = tk.Button(self, text="Browse", command=self.select_folder)
        btn_browse_folder.grid(row=0, column=1, padx=10, pady=10)
        # Empty row
        self.grid_rowconfigure(2, minsize=20)

        # Options for renaming
        lbl_mode = tk.Label(self, text="Rename Mode:")
        lbl_mode.grid(row=3, column=0, padx=10, pady=10)

        self.optmen_mode = tk.OptionMenu(self, self.var_mode, *self.mode_options.keys())
        self.optmen_mode.grid(row=3, column=1, padx=10, pady=10)

        lbl_new_name = tk.Label(self, text="Your Name:")
        lbl_new_name.grid(row=4, column=0, padx=10, pady=10)

        self.ent_new_name = tk.Entry(self, textvariable=self.var_new_name)
        self.ent_new_name.grid(row=4, column=1, sticky="ew", padx=10, pady=0)

        # Rename button
        btn_rename = tk.Button(self, text="Rename Files", command=self.rename_files)
        btn_rename.grid(row=5, columnspan=2, pady=20)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        self.var_folder_path.set(folder_selected)

    def rename_files(self):
        var_mode = self.mode_options[self.var_mode.get()]
        if var_mode == "prefix":
            self.add_prefix()
        elif var_mode == "suffix":
            self.add_suffix()
        elif var_mode == "replace":
            self.replace_whole()
    
    def add_prefix(self):
        folder_path = self.var_folder_path.get()
        prefix = self.var_new_name.get()
        if folder_path and prefix:
            for filename in os.listdir(folder_path):
                if os.path.isfile(os.path.join(folder_path, filename)):
                    new_filename = prefix + filename
                    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            # Update the entry with the new folder path after renaming
            self.var_folder_path.set(folder_path)
        else:
            print("Folder path and prefix are required.")

    def add_suffix(self):
        pass

    def replace_whole(self):
        pass

