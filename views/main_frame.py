import customtkinter as ctk
from components.note_list import NoteList
from services.note_service import NoteService
from components.new_window import NewWindow

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure the row and column of the MainFrame
        self.grid_rowconfigure(0, weight=0)  # Button row
        self.grid_rowconfigure(1, weight=1)  # NoteList row
        self.grid_columnconfigure(0, weight=1)

        self.button = ctk.CTkButton(self, text="Add note", command=self.add_note_window)
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.refresh_notes()
    
    def refresh_notes(self):
        if hasattr(self, "note_list"):
            self.note_list.destroy()
        self.note_list = NoteList(self, "Notes", main_frame=self)  # Pass main_frame reference
        self.note_list.refresh_notes()
        self.note_list.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def add_note_window(self):
        new_window = NewWindow(self, title="Add note")
        # new_window.reset_lift_and_focus()

        self.textbox = ctk.CTkTextbox(new_window, corner_radius=0, height=350, border_spacing=10)
        self.textbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        save_button = ctk.CTkButton(new_window, text="Save", command=self.on_add_note)
        save_button.grid(row=1, column=0)
    
    def on_add_note(self):
        text_box_balue = self.textbox.get("0.0", "end")
        data = {
            "title": "New note",
            "description": text_box_balue
        }
        NoteService().add_note(data)
        self.refresh_notes()

    def get_note(self):
        pass