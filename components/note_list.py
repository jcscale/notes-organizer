import customtkinter as ctk
from components.card import Card
from components.new_window import NewWindow
from services.note_service import NoteService

class NoteList(ctk.CTkScrollableFrame):
    def __init__(self, master, title):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)

        self.refresh_notes()
    
    def refresh_notes(self):
        # Get all notes from the database
        self.notes = NoteService().get_all_notes()
        
        for i, value in enumerate(self.notes):
            card = Card(self, id=value[0], title=value[1], description=value[2], on_click=lambda v=value: self.on_card_click(v))
            card.pack(padx=10, pady=10, fill="both", expand=True)
    
    # Callback function for the card click event
    def on_card_click(self, value):
        new_window = NewWindow(self.master, title=value[1])
        # new_window.reset_lift_and_focus()

        edit_button = ctk.CTkButton(new_window, text="Edit", command=lambda: self.edit_note(value[1]))
        edit_button.grid(row=0, column=0)

        delete_button = ctk.CTkButton(new_window, text="Delete", command=lambda: self.on_delete_note(value[0]))
        delete_button.grid(row=0, column=1)

        save_button = ctk.CTkButton(new_window, text="Save")
        save_button.grid(row=0, column=2)
        
        title = ctk.CTkLabel(new_window, text=value[1])
        title.grid(row=1, column=0, padx=20, pady=3, sticky="w")

        # description = ctk.CTkLabel(new_window, text=value[2])
        # description.grid(row=2, column=0, padx=20, pady=3, sticky="w")

        textbox = ctk.CTkTextbox(new_window, corner_radius=0, height=350, border_spacing=10)
        textbox.grid(row=3, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        textbox.insert("0.0", value[2])
    
    def edit_note(self, title):
        print(title)
    
    def on_delete_note(self, id):
        NoteService().delete_note(id)

