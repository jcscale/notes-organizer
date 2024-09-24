import customtkinter as ctk

class Card(ctk.CTkFrame):
    def __init__(self, master, title, description):
        super().__init__(master)

        self.title_label = ctk.CTkLabel(self, text=title)
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.description_label = ctk.CTkLabel(self, text=description)
        self.description_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        