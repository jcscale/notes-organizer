import customtkinter as ctk
from components.note_list import NoteList

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure the row and column of the MainFrame
        self.grid_rowconfigure(0, weight=0)  # Button row
        self.grid_rowconfigure(1, weight=1)  # NoteList row
        self.grid_columnconfigure(0, weight=1)

        self.button = ctk.CTkButton(self, text="Add note", command=self.on_add_note)
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.notes = []
        for i in range(10):
            self.notes.append(f"Note {i}")

        self.note_list = NoteList(self, "Notes", values=self.notes)
        self.note_list.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    def on_add_note(self):
        print("Add note")