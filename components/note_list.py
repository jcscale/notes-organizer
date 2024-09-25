import customtkinter as ctk
from components.card import Card

class NoteList(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values

        for i, value in enumerate(self.values):
            print(value)
            card = Card(self, title=value[1], description=value[2], on_click=lambda v=value: self.on_card_click(v))
            card.pack(padx=10, pady=10, fill="both", expand=True)
    
    def on_card_click(self, value):
        new_window = ctk.CTkToplevel(self)
        new_window.title(value[1])
        new_window.geometry("500x200")
        
        title = ctk.CTkLabel(new_window, text=value[1])
        title.grid(row=0, column=0, padx=20, pady=3, sticky="w")

        description = ctk.CTkLabel(new_window, text=value[2])
        description.grid(row=1, column=0, padx=20, pady=3, sticky="w")