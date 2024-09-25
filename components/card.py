import customtkinter as ctk

class Card(ctk.CTkFrame):
    def __init__(self, master, title, description, on_click=None):
        super().__init__(master)
        
        # Create and place the title label inside the inner frame
        self.title_label = ctk.CTkLabel(self, text=title, font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=3, sticky="w")
        
        # Create and place the description label inside the inner frame
        self.description_label = ctk.CTkLabel(self, text=description, font=("Arial", 12))
        self.description_label.grid(row=1, column=0, padx=10, pady=3, sticky="w")
        
        # Store the on_click callback
        self.on_click = on_click
        
        # Bind the click event to the card
        self.bind("<Button-1>", self.handle_click)
        self.title_label.bind("<Button-1>", self.handle_click)
        self.description_label.bind("<Button-1>", self.handle_click)

    def handle_click(self, event):
        if self.on_click:
            self.on_click()
        