import customtkinter as ctk
from components.card import Card

class NoteList(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values

        for i, value in enumerate(self.values):
            card = Card(self, title=value, description="This is a note")
            card.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="ew")