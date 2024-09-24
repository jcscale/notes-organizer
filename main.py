import customtkinter as ctk
from views.main_frame import MainFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Notes Organizer")
        self.geometry("350x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

app = App()
app.mainloop()