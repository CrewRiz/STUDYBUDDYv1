import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
from config import TUTOR_ASSISTANT_ID, NOTES_ASSISTANT_ID, logging
from api_client import APIClient
from utils import save_file, load_file

class StudyBuddyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Buddy")
        self.geometry("800x700")
        self.api_client = APIClient()
        self.create_start_menu()

    def create_start_menu(self):
        self.clear_window()
        frame = ttk.Frame(self)
        frame.pack(expand=True)

        ttk.Label(frame, text="Welcome to Study Buddy!", font=('Helvetica', 16)).pack(pady=20)
        ttk.Button(frame, text="Take Notes", command=lambda: self.create_interface(NOTES_ASSISTANT_ID)).pack(pady=10)
        ttk.Button(frame, text="Start Tutoring", command=lambda: self.create_interface(TUTOR_ASSISTANT_ID)).pack(pady=10)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_interface(self, assistant_id):
        self.clear_window()
        is_tutor = (assistant_id == TUTOR_ASSISTANT_ID)

        output_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Helvetica', 14, 'bold'), height=15)
        output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        input_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=('Helvetica', 12), height=10)
        input_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Submit", command=lambda: self.submit_input(input_area, output_area, assistant_id)).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=lambda: self.clear_interface(input_area, output_area)).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save", command=lambda: save_file(output_area.get("1.0", tk.END))).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Load", command=lambda: self.load_input(input_area)).pack(side=tk.LEFT, padx=5)

        if is_tutor:
            ttk.Button(button_frame, text="Upload Document", command=self.upload_document).pack(side=tk.LEFT, padx=5)
        else:
            ttk.Button(button_frame, text="Save Summary", command=lambda: save_file(output_area.get("1.0", tk.END), "txt")).pack(side=tk.LEFT, padx=5)

        ttk.Button(button_frame, text="Back to Menu", command=self.create_start_menu).pack(side=tk.LEFT, padx=5)

        self.status_label = ttk.Label(self, text="Status: Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(fill=tk.X, padx=10, pady=5)

    def submit_input(self, input_area, output_area, assistant_id):
        content = input_area.get("1.0", tk.END).strip()
        if content:
            self.update_status("Processing...")
            threading.Thread(target=self._process_input, args=(content, output_area, assistant_id)).start()
        else:
            messagebox.showwarning("Warning", "Please enter some text to process.")

    def _process_input(self, content, output_area, assistant_id):
        try:
            self.api_client.add_message(content)
            run_id = self.api_client.run_conversation(assistant_id)

            while True:
                run_status = self.api_client.get_run_status(run_id)
                if run_status.status in ['completed', 'failed']:
                    break
                time.sleep(1)

            if run_status.status == 'failed':
                raise Exception("Assistant run failed.")

            messages = self.api_client.get_messages()
            assistant_message = next((m for m in messages.data if m.role == 'assistant'), None)
            if assistant_message:
                response = assistant_message.content[0].text.value
                self.update_output(output_area, response)
            else:
                raise Exception("No response from assistant.")
        except Exception as e:
            logging.error(f"Error in _process_input: {e}")
            self.update_output(output_area, f"Error: {str(e)}")
        finally:
            self.update_status("Ready")

    def clear_interface(self, input_area, output_area):
        input_area.delete("1.0", tk.END)
        output_area.delete("1.0", tk.END)
        self.api_client.create_thread()  # Start a new conversation thread
        self.update_status("Ready")

    def load_input(self, input_area):
        content = load_file()
        input_area.delete("1.0", tk.END)
        input_area.insert(tk.END, content)

    def upload_document(self):
        file_id = self.api_client.upload_file(filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf")]))
        if file_id:
            messagebox.showinfo("Success", "File uploaded successfully.")
        else:
            messagebox.showerror("Error", "Failed to upload file.")

    def update_output(self, output_area, content):
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, content)

    def update_status(self, status):
        self.status_label.config(text=f"Status: {status}")