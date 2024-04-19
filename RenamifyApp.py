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
            "Replace": "replace"
        }
        
        # Variables
        self.var_folder_path = tk.StringVar(value="C:/Your Path")
        self.var_mode = tk.StringVar(value="Add Prefix")
        self.var_new_name = tk.StringVar(value="New Name")
        self.var_include_subfolders = tk.BooleanVar(value=True)
        self.var_replace_extension = tk.BooleanVar(value=False)

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
        self.var_mode.trace_add("write", self.show_hide_options)  # Call a method to show/hide options based on var_mode

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

        # Checkbox for if extensions should be replaced
        # Widget is hidden unless in "replace" / "suffix" mode
        self.chk_replace_extension = tk.Checkbutton(self, text="Replace Extension", variable=self.var_replace_extension)

    def show_hide_options(self, *args):
        # Show / Hide the checkboxes if mode is "replace" / "suffix"
        mode = self.mode_options[self.var_mode.get()]
        if mode == "replace" or mode == "suffix":
            self.chk_replace_extension.grid(row=8, column=1, padx=10, sticky="e")
        else:
            self.chk_replace_extension.grid_remove()


    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        self.var_folder_path.set(folder_selected)

    def rename_files(self):
        folder_path = self.var_folder_path.get()

        target_files = self.get_target_files(folder_path, self.var_include_subfolders.get())
        for index, old_file_path in enumerate(target_files):
            file_name, file_extension = os.path.splitext(old_file_path)
            new_filename = self.get_new_name(os.path.basename(file_name), file_extension, index)
            new_file_path = os.path.join(os.path.dirname(old_file_path), new_filename)
            
            # Check if the new file path already exists
            # Happens if user tries to change name that's the same
            if os.path.exists(new_file_path):
                continue    
            
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



    def get_new_name(self, old_filename, file_extension, index):
        var_mode = self.mode_options[self.var_mode.get()]
        if var_mode == "prefix":
            return self.add_prefix(old_filename, file_extension)
        elif var_mode == "suffix":
            return self.add_suffix(old_filename, file_extension)
        elif var_mode == "replace":
            return self.replace_whole(file_extension, f" ({index})")

        return old_filename
    
    def add_prefix(self, old_filename, file_extension):
        return self.var_new_name.get() + old_filename + file_extension

    def add_suffix(self, old_filename, file_extension):
        user_input = self.var_new_name.get()
        if self.var_replace_extension.get():
            suffix, new_extension = os.path.splitext(user_input)
            return old_filename + suffix + new_extension
        else:
            return old_filename + self.var_new_name.get() + file_extension



    def replace_whole(self, file_extension, suffix=""):
        user_input = self.var_new_name.get()
        if self.var_replace_extension.get():
            new_name, new_extension = os.path.splitext(user_input)
            return new_name + str(suffix) + new_extension
        else:
            return user_input + str(suffix) + file_extension

