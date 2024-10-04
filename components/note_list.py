import customtkinter as ctk
from components.card import Card
from components.new_window import NewWindow
from services.note_service import NoteService

class NoteList(ctk.CTkScrollableFrame):
    def __init__(self, master, title, main_frame):
        super().__init__(master, label_text=title)
        self.main_frame = main_frame  # Store the reference to MainFrame
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

        title = ctk.CTkLabel(new_window, text=value[1])
        title.grid(row=0, column=0, padx=20, pady=3, sticky="w")

        textbox = ctk.CTkTextbox(new_window, corner_radius=0, height=350, border_spacing=10)
        textbox.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        textbox.insert("0.0", value[2])

        edit_button = ctk.CTkButton(new_window, text="Update", command=lambda: self.on_update_note(value, textbox.get("0.0", "end")))
        edit_button.grid(row=2, column=0)

        delete_button = ctk.CTkButton(new_window, text="Delete", command=lambda: self.on_delete_note(value[0], new_window))
        delete_button.grid(row=2, column=1)

        save_button = ctk.CTkButton(new_window, text="Save")
        save_button.grid(row=2, column=2)
        
    def edit_note(self, title):
        print(title)

    def on_update_note(self, data, new_data):
        updated_data = {
            "id": data[0],
            "title": data[1],
            "description": new_data
        }
        NoteService().update_note(updated_data)
        self.main_frame.refresh_notes()
    
    def on_delete_note(self, id, new_window):
        NoteService().delete_note(id)
        self.main_frame.refresh_notes()
        new_window.destroy()

