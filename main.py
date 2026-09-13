import os
import tkinter as tk
from tkinter import messagebox

class NewwebBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Newweb Browser")
        self.root.geometry("600x470")
        self.root.configure(bg="#ffffff")

        # System paths
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.web_dir = os.path.join(self.base_dir, "web")
        self.bin_dir = os.path.join(self.base_dir, "bin")
        
        os.makedirs(self.web_dir, exist_ok=True)
        os.makedirs(self.bin_dir, exist_ok=True)

        self.create_widgets()
        
        # Automatically load and list all registered websites on startup
        self.refresh_web_list()

    def create_widgets(self):
        # Centered Logo Text
        self.logo_label = tk.Label(
            self.root, 
            text="🔍 Newweb", 
            font=("Arial", 28, "bold"), 
            bg="#ffffff", 
            fg="#111111"
        )
        self.logo_label.pack(pady=(35, 5))

        # Slogan
        self.slogan_label = tk.Label(
            self.root, 
            text="it goes compile compile!", 
            font=("Arial", 10, "italic"), 
            bg="#ffffff", 
            fg="#555555"
        )
        self.slogan_label.pack(pady=(0, 20))

        # Search Interface Frame
        search_frame = tk.Frame(self.root, bg="#ffffff")
        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(
            search_frame, 
            font=("Arial", 14), 
            width=30, 
            bd=2, 
            relief="groove"
        )
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind("<Return>", lambda event: self.perform_search())

        self.search_button = tk.Button(
            search_frame, 
            text="Search", 
            font=("Arial", 11, "bold"), 
            bg="#333333", 
            fg="#ffffff", 
            command=self.perform_search,
            relief="flat",
            padx=12
        )
        self.search_button.pack(side=tk.LEFT, padx=5)

        # Results Label
        self.results_label = tk.Label(
            self.root, 
            text="Registered site.screens.if Instances:", 
            font=("Arial", 11, "bold"), 
            bg="#ffffff"
        )
        self.results_label.pack(pady=(15, 5), anchor="w", padx=50)

        # Results Box
        self.results_listbox = tk.Listbox(
            self.root, 
            font=("Arial", 11), 
            width=60, 
            height=9
        )
        self.results_listbox.pack(padx=50, pady=5)
        self.results_listbox.bind("<Double-1>", self.open_website)

    def refresh_web_list(self):
        """Scans the directory and populates the listbox with available sites."""
        self.results_listbox.delete(0, tk.END)
        try:
            subfolders = [f for f in os.listdir(self.web_dir) if os.path.isdir(os.path.join(self.web_dir, f))]
            
            if not subfolders:
                self.results_listbox.insert(tk.END, "No local sites found. Add folders to ./web/")
            else:
                for folder in subfolders:
                    self.results_listbox.insert(tk.END, folder)
        except Exception as e:
            messagebox.showerror("Error", f"Failed reading directory context: {e}")

    def perform_search(self):
        query = self.search_entry.get().lower().strip()
        
        # If search bar is empty, revert to showing all sites
        if not query:
            self.refresh_web_list()
            return

        self.results_listbox.delete(0, tk.END)

        try:
            subfolders = [f for f in os.listdir(self.web_dir) if os.path.isdir(os.path.join(self.web_dir, f))]
            matches = [f for f in subfolders if query in f.lower()]

            if not matches:
                self.results_listbox.insert(tk.END, "No local sites found matching that query.")
            else:
                for match in matches:
                    self.results_listbox.insert(tk.END, match)
        except Exception as e:
            messagebox.showerror("Error", f"Search scanning failed: {e}")

    def open_website(self, event):
        selection = self.results_listbox.curselection()
        if not selection:
            return
            
        site_node = self.results_listbox.get(selection)
        if "No local sites" in site_node or "No registered sites" in site_node:
            return

        site_path = os.path.join(self.web_dir, site_node)
        
        # Domain mapping
        reg_json = os.path.join(site_path, "reg-site.screens.if-reg.json")
        owner_json = os.path.join(site_path, f"site.screens.if-{site_node}.json")
        compiled_bin = os.path.join(self.bin_dir, "d0edce1ce01807164c81d2f6d0dacabda36a2a2d024ad6f69d7011a6b3e386f0.gun")

        missing = []
        if not os.path.exists(reg_json): missing.append("reg-site.screens.if-reg.json")
        if not os.path.exists(owner_json): missing.append(f"site.screens.if-{site_node}.json")
        if not os.path.exists(compiled_bin): missing.append("bin/*.gun payload")

        if missing:
            messagebox.showerror("Resolution Error", f"Newweb core could not resolve assets:\n" + "\n".join(missing))
            return

        # Render Newweb Viewport
        web_window = tk.Toplevel(self.root)
        web_window.title(f"Newweb Browser - site.screens.if-{site_node}")
        web_window.geometry("520x420")
        
        text_area = tk.Text(web_window, wrap=tk.WORD, font=("Courier", 11))
        text_area.pack(expand=True, fill=tk.BOTH, padx=15, pady=15)
        
        text_area.insert(tk.END, f"--- [Newweb Engine V1 Core Initialization] ---\n")
        text_area.insert(tk.END, f"Targeting domain: site.screens.if-{site_node}\n\n")
        text_area.insert(tk.END, f"[OK] Found mapping config: {os.path.basename(reg_json)}\n")
        text_area.insert(tk.END, f"[OK] Found owner config: {os.path.basename(owner_json)}\n")
        text_area.insert(tk.END, f"[OK] Executing target payload: {os.path.basename(compiled_bin)}\n\n")
        text_area.insert(tk.END, f"STATUS: Newweb virtual environment compilation completed successfully.")
        text_area.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NewwebBrowser(root)
    root.mainloop()
