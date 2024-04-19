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
        self.var_include_subfolders = tk.BooleanVar(value=True)

        self.create_widgets()


    def create_widgets(self):
        # Widgets for folder selection
        lbl_select_folder = tk.Label(self, text="Select Folder:")
        lbl_select_folder.grid(row=0, column=0, padx=10, pady=10)

        ent_folder_path = tk.Entry(self, textvariable=self.var_folder_path, state="disabled")
        ent_folder_path.grid(row=1, columnspan=2, column=0, sticky="ew", padx=10, pady=0)

        btn_browse_folder = tk.Button(self, text="Browse", command=self.select_folder)
        btn_browse_folder.grid(row=0, column=1, padx=10, pady=10)
        # Empty row
        self.grid_rowconfigure(2, minsize=20)

        # Options for renaming
        lbl_mode = tk.Label(self, text="Rename Mode:")
        lbl_mode.grid(row=4, column=0, padx=10, pady=10)

        optmen_mode = tk.OptionMenu(self, self.var_mode, *self.mode_options.keys())
        optmen_mode.grid(row=4, column=1, padx=10, pady=10)

        lbl_new_name = tk.Label(self, text="Your Name:")
        lbl_new_name.grid(row=5, column=0, padx=10, pady=10)

        ent_new_name = tk.Entry(self, textvariable=self.var_new_name)
        ent_new_name.grid(row=5, column=1, sticky="ew", padx=10, pady=0)

        # Rename button
        btn_rename = tk.Button(self, text="Rename Files", command=self.rename_files)
        btn_rename.grid(row=6, columnspan=2, pady=20)

        # Checkbox for subfolders
        chk_include_subfolders = tk.Checkbutton(self, text="Include Subfolders", variable=self.var_include_subfolders)
        chk_include_subfolders.grid(row=7, column=1, padx=10, sticky="e")

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        self.var_folder_path.set(folder_selected)

    def rename_files(self):
        folder_path = self.var_folder_path.get()

        target_files = self.get_target_files(folder_path, self.var_include_subfolders.get())
        for old_file_path in target_files:
            new_filename = self.get_new_name(os.path.basename(old_file_path))
            new_file_path = os.path.join(os.path.dirname(old_file_path), new_filename)
            os.rename(old_file_path, new_file_path)

    def get_target_files(self, folder_path, include_subfolders=False):
        target_files = []
        if include_subfolders:
            # walk only includes files, so no need to check if it is a file
            for root, _, files in os.walk(folder_path):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    target_files.append(file_path)
        else:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename) 
                if os.path.isfile(file_path):
                    target_files.append(file_path)
                    
        return target_files



    def get_new_name(self, filename):
        var_mode = self.mode_options[self.var_mode.get()]
        if var_mode == "prefix":
            return self.add_prefix(filename)
        elif var_mode == "suffix":
            return self.add_suffix(filename)
        elif var_mode == "replace":
            return self.replace_whole(filename)

        return filename
    
    def add_prefix(self, filename):
        return self.var_new_name.get() + filename

    def add_suffix(self, filename):
        return filename + self.var_new_name.get()

    def replace_whole(self, filename):
        pass

